from pydantic import BaseModel


class UserInfoAPI(BaseModel):
    full_name: str
    personal_email: str
    work_email: str
    birth_date: str
    phone: str
    preferred_method: str
