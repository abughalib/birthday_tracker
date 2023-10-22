from ..constants import PUBLIC_KEY, PRIVATE_KEY
import os


def get_public_key():
    public_key = os.environ.get(PUBLIC_KEY)

    return public_key


def get_private_key():
    private_key = os.environ.get(PRIVATE_KEY)

    return private_key
