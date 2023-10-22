from datetime import datetime
from .database.user_info_table import UserInfoTable
from .utils import full_validation
from .models.api_model import UserInfoAPI
from .models.db_model import UserInfoModel
from .encryption import encrypt, decrypt


UserInfoTable = UserInfoTable()

def insert_birthday(user_info: UserInfoAPI):

    if full_validation.validate_user_info(user_info):

        user_info_values = UserInfoModel (
            encrypt.encrypt_string(user_info.full_name),
            encrypt.encrypt_string(user_info.personal_email),
            encrypt.encrypt_string(user_info.work_email),
            user_info.birth_date,
            encrypt.encrypt_string(user_info.phone),
            encrypt.encrypt_string(user_info.preferred_method)
        )


        UserInfoTable.insert(user_info_values)

        return True

    return False

def find_birthday_today():
    now = datetime.now()
    today_date = now.date()

    encrypted_data = UserInfoTable.birthday_contacts(today_date)

    decrypted_data = []

    for data in encrypted_data:
        # Decrypt all encrypted fields
        cur_data = []
        for field_value in data:
            cur_data.append(decrypt.decrypt_message(field_value))

        decrypted_data.append(cur_data)
            


