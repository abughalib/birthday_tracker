from cryptidy import asymmetric_encryption
from ..utils import vars

def encrypt_string(text: str) -> bytes:

    ''' Encrypt Message 
        @param text string

        @return string

        Encrypted String with UTF-8 Encoding, it may fail some day
    '''

    encrypted_byt = asymmetric_encryption.encrypt_message(text, vars.get_public_key())

    return encrypted_byt
