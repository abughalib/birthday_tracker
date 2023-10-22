from cryptidy import asymmetric_encryption as aes
from ..utils import vars


def decrypt_message(encrypt_msg: bytes):

    private_key = vars.get_private_key()

    _, original = aes.decrypt_message(encrypt_msg, private_key)

    return original
