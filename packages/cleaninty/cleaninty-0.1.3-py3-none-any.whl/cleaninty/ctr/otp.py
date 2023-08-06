from struct import pack, unpack
import hashlib, typing

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec

from . import certificate, keys
from . import digitalsignature as digsign
from .exception import ClassInitError
from .constants import _load_p9_keys, _p9_pubnums

__all__ = [
	"OTP",
	"CTCert"
]

_load_p9_keys()

class OTP:
	def __init__(self, data: typing.SupportsBytes):
		data = bytes(data)[:0x100]
		orig_data = data

		if len(data) != 0x100:
			raise ClassInitError("Need 256 bytes for full OTP")

		segments = unpack("<II16sBB6s4s32s60s16s80s32s", data)

		if segments[0] != 0xDEADB00F:
			data = keys._decrypt_otp(orig_data, False)
			if data:
				segments = unpack("<II16sBB6s4s32s60s16s80s32s", data)

		if segments[0] != 0xDEADB00F:
			data = keys._decrypt_otp(orig_data, True)
			if data:
				segments = unpack("<II16sBB6s4s32s60s16s80s32s", data)

		if segments[0] != 0xDEADB00F:
			raise ClassInitError("OTP invalid start")

		self._otp_dec_data = data if data else orig_data

		self._device_id = segments[1]
		self._base_movable_keyY = segments[2]
		self._otp_version = segments[3]
		self._otp_system_type = segments[4]
		self._soc_date = segments[5]
		self._ct_cert_expiration = segments[6]
		self._ct_cert_privk = int.from_bytes(segments[7], 'big') & ((1 << 233) - 1)
		self._ct_cert_signature = segments[8]
		self._hash = segments[11]

		self._lfcs_id, self._supplementary_id = unpack("<QQ", self._base_movable_keyY)

		if hashlib.sha256(self._otp_dec_data[:0xE0]).digest() != self._hash:
			raise ClassInitError("OTP SHA256 verification failed")

		self._otp_enc_data = keys._encrypt_otp(self._otp_dec_data, self.is_dev)
		self._console_keys_x = keys._gen_console_keys(self._otp_dec_data[0x90:0xAC], self.is_dev)
		self._console_keys_x = self._console_keys_x if self._console_keys_x else (None,)*64

	def __bytes__(self):
		return self._otp_dec_data

	def __len__(self):
		return len(self._otp_dec_data)

	def gen_console_keys(self) -> bool:
		if self._console_keys_x.count(None) == 30:
			return True
		self._console_keys_x = keys._gen_console_keys(self._otp_dec_data[0x90:0xAC], self.is_dev)
		self._console_keys_x = self._console_keys_x if self._console_keys_x else (None,)*64
		return self._console_keys_x.count(None) == 30

	@property
	def otp_dec(self) -> bytes:
		return self._otp_dec_data

	@property
	def otp_enc(self) -> bytes:
		return self._otp_enc_data

	@property
	def is_dev(self) -> bool:
		return self._otp_system_type != 0

	@property
	def is_n3ds(self) -> bool:
		return (self._device_id & 0x80000000) != 0

	@property
	def device_id(self) -> int:
		return self._device_id

	@property
	def otp_system_type(self) -> int:
		return self._otp_system_type

	@property
	def otp_version(self) -> int:
		return self._otp_version

	@property
	def lfcs_id(self) -> int:
		return self._lfcs_id

	@property
	def supplementary_id(self) -> int:
		return self._supplementary_id

	@property
	def console_keys_x(self) -> typing.Iterable[typing.Optional[int]]:
		return self._console_keys_x

class CTCert(certificate.Certificate):
	def __init__(self, otp: OTP):
		if not isinstance(otp, OTP):
			raise ClassInitError("CTCert excepts OTP object")

		try:
			privkey = ec.derive_private_key(otp._ct_cert_privk, ec.SECT233R1(), default_backend())
			pubkeynumbers = privkey.public_key().public_numbers()
		except Exception as e:
			raise ClassInitError("EC Key derivation error") from e

		try:
			data = pack(
				">I60s64x64sI64s4s30s30s60x",
				digsign.SignatureType.ECC_SHA256,
				otp._ct_cert_signature,
				(b"Nintendo CA - G3_NintendoCTR2" + (b"prod" if otp._otp_system_type == 0 else b"dev")),
				digsign.KeyType.ECC,
				(f"CT{otp._device_id:08X}-{otp._otp_system_type:02X}").encode(),
				(otp._ct_cert_expiration if otp._otp_version < 5 else otp._ct_cert_expiration[::-1]),
				pubkeynumbers.x.to_bytes(30, 'big'),
				pubkeynumbers.y.to_bytes(30, 'big'),
			)
		except Exception as e:
			raise ClassInitError("Packing error") from e

		super().__init__(data)

		self._is_dev = otp._otp_system_type != 0
		self._device_id = otp._device_id
		self._otp_system_type = otp._otp_system_type
		self._otp_version = otp._otp_version

		try:
			key = _p9_pubnums['CTR2_DEV'] if self._is_dev else _p9_pubnums['CTR2_PROD']
			if key is None:
				_load_p9_keys()
				key = _p9_pubnums['CTR2_DEV'] if self._is_dev else _p9_pubnums['CTR2_PROD']
			key = key.public_key(default_backend())
			self.verify(key)
		except Exception as e:
			raise ClassInitError("Could not verify CTCert") from e

		if not self.set_private_key(privkey.private_numbers()):
			raise ClassInitError("CTCert private key was not successfully loaded!")

	@property
	def is_dev(self) -> bool:
		return self._is_dev

	@property
	def is_retail(self) -> bool:
		return not self._is_dev

	@property
	def device_id(self) -> int:
		return self._device_id

	@property
	def otp_system_type(self) -> int:
		return self._otp_system_type

	@property
	def otp_version(self) -> int:
		return self._otp_version
