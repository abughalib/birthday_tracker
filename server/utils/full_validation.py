from . import validator
from ..models.api_model import UserInfoAPI
from .mthread import ThreadWithResult


def validate_user_info(user_info: UserInfoAPI) -> bool:
    pmail_val = ThreadWithResult(
        target=validator.verify_email, args=(user_info.personal_email,)
    )

    wmail_val = ThreadWithResult(
        target=validator.verify_email, args=(user_info.work_email, True)
    )
    ph_val = ThreadWithResult(target=validator.verify_phone, args=(user_info.phone,))
    date_val = ThreadWithResult(
        target=validator.verify_date, args=(user_info.birth_date,)
    )
    pm_val = ThreadWithResult(
        target=validator.verify_pref_method, args=(user_info.preferred_method,)
    )

    pmail_val.start()
    wmail_val.start()
    ph_val.start()
    date_val.start()
    pm_val.start()

    pmail_val = pmail_val.join()
    wmail_val = wmail_val.join()
    ph_val = ph_val.join()
    date_val = date_val.join()
    pm_val = pm_val.join()

    return ((pmail_val or wmail_val or ph_val or date_val) and pm_val) or False
