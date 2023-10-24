from ..messaging import email
from ..models.db_query_mode import UserInfoQuery

def test_send_email():

    ''' Test Single Message '''

    test_email = "abughalib64@gmail.com"

    birthday_list = [
        UserInfoQuery(
            "Abu Ghalib",
            "CSE",
            "abughalib64@gmail.com",
            "abughalib@example.org",
            "9323432325",
            "PERSONAL_MAIL"
        )
    ]

    message_text, message_html = email.get_email_format(birthday_list)

    email.send_mail(message_text, message_html, [test_email], [])
    
