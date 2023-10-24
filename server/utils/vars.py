import os
import logging
from ..constants import (
    PUBLIC_KEY,
    PRIVATE_KEY,
    PERSONAL_MAIL_SENDER,
    PERSONAL_MAIL_SENDER_PASSWORD,
    PERSONAL_EMAIL_SENDER_NAME,
)


def get_public_key() -> str:
    public_key_path = os.environ.get(PUBLIC_KEY)

    public_key = ""

    if public_key_path:
        try:
            with open(public_key_path, "r") as file:
                public_key = file.read()

        except Exception as e:
            logging.log(
                msg=f"{public_key_path} file content not found, Error: {e}", level=2
            )
    else:
        logging.log(msg=f"{PUBLIC_KEY} not defined", level=1)

    return public_key


def get_private_key() -> str:
    private_key_path = os.environ.get(PRIVATE_KEY)
    private_key = ""

    if private_key_path:
        try:
            with open(private_key_path) as file:
                private_key = file.read()
        except Exception as e:
            logging.log(
                msg=f"{private_key_path} file content not found, Error: {e}", level=2
            )
    else:
        logging.log(msg=f"{PRIVATE_KEY} not defined", level=1)

    return private_key


def get_app_email() -> str:
    sender_email = os.environ.get(PERSONAL_MAIL_SENDER)

    if sender_email:
        return sender_email

    logging.log(msg=f"{PERSONAL_MAIL_SENDER} not defined", level=1)

    return ""


def get_email_sender_name() -> str:
    sender_name = os.environ.get(PERSONAL_EMAIL_SENDER_NAME)
    if sender_name:
        return sender_name

    logging.log(msg=f"{PERSONAL_EMAIL_SENDER_NAME} not defined", level=1)


def get_app_email_password() -> str:
    sender_app_password = os.environ.get(PERSONAL_MAIL_SENDER_PASSWORD)

    if sender_app_password:
        return sender_app_password

    logging.log(msg=f"{PERSONAL_MAIL_SENDER_PASSWORD} not defined", level=1)

    return ""
