import datetime


class UserInfoModel:
    def __init__(
        self,
        full_name: bytes,
        personal_mail: bytes,
        work_email: bytes,
        birth_date: str,
        phone: bytes,
        preferred_method: bytes,
    ):
        def convert_date(birth_date):
            birth_date.split("-")
            fm_date = datetime.date(
                int(birth_date[2]), int(birth_date[1]), int(birth_date[0])
            )

            return fm_date

        self.full_name = full_name
        self.personal_mail = personal_mail
        self.work_email = work_email
        self.birth_date = convert_date(birth_date)
        self.phone = phone
        self.preferred_method = preferred_method

    def get_full_name(self):
        return self.full_name

    def get_personal_email(self):
        return self.personal_mail

    def get_work_email(self):
        return self.work_email

    def get_phone(self):
        return self.phone

    def get_preferred_method(self):
        return self.get_preferred_method
