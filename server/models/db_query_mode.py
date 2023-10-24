
class UserInfoQuery:

    def __init__(self, full_name: str, department: str, personal_mail: str, work_mail: str, phone: str, 
                 preferred_method: str):

        self.full_name = full_name
        self.department = department
        self.personal_mail = personal_mail
        self.work_mail = work_mail
        self.phone = phone
        self.preferred_method = preferred_method

    