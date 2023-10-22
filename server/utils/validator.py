import re
import datetime
from ..constants import (
    PHONE_REGEX,
    WORK_EMAIL_REGEX,
    PERSONAL_EMAIL_REGEX,
    PREFERRED_METHODS,
    DATE_REGEX,
)


def verify_phone(phone_str: str) -> bool:
    """Verify Phone Number
    @param phone_str string
    @return bool

    Matches PHONE_REGEX against given string
    and return bool based on if it matches or not
    """
    res = re.findall(PHONE_REGEX, phone_str)

    if len(res) == 1:
        return True

    return False


def verify_email(email: str, is_work=False) -> bool:
    """Verify Email
    @param email string
    @param is_work bool
    @return bool

    Matches EMAIL_REGEX against given string
    and return bool based on if it matches or not
    """
    if is_work:
        res = re.findall(WORK_EMAIL_REGEX, email)

        if len(res) == 1:
            return True
        return False

    res = re.findall(PERSONAL_EMAIL_REGEX, email)

    if len(res) == 1:
        return True

    return False


def verify_date(user_date: str) -> bool:
    """Verify Date
    @param user_date string
    @return bool

    Matches DATE_REGEX against given string
    and return bool based on if it matches or not
    """
    res = re.findall(DATE_REGEX, user_date)

    if len(res) == 1:
        try:
            datetime.datetime(int(res[2]), int(res[1]), int(res[0]))
            return True
        except ValueError:
            return False

    return False


def verify_pref_method(method: str) -> bool:
    """Verify Preferred Method
    @param method string
    @return bool

    Matches EMAIL REGEX against given string
    and return bool based on if it matches or not
    """
    if method in PREFERRED_METHODS:
        return True
    else:
        return False
