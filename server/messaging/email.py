import smtplib, ssl
from ..utils import vars
from typing import List
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..models.db_query_mode import UserInfoQuery
from ..constants import PERSONAL_EMAIL_SENDER, PERSONAL_EMAIL_SENDER_NAME

port = 465

email_sender = vars.get_app_email()
password = vars.get_app_email_password()


def get_email_format(birthday_list: List[UserInfoQuery]):
    tr_str = ""
    message_text = """\
      Birthday Remainder
      Name | Department
    """

    for birthday_person in birthday_list:
        tr_str += f"""
            <tr>
              <td>{birthday_person.full_name}</td>
              <td>{birthday_person.department}</td>
            </tr>
          """
        message_text += f"{birthday_person.full_name} | {birthday_person.department}\n"

    birthday_mail = f"""
    <!DOCTYPE html>
    <html>
      <head>
        <style>
          body {{
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.5;
            color: #333;
            background-color: #f2f2f2;
          }}
          h1 {{
            font-size: 24px;
            margin-bottom: 0;
            color: #c00764;
          }}
          p {{
            margin-top: 0;
          }}
          table {{
            border-collapse: collapse;
            width: 20%;
            margin-top: 20px;
          }}
          th,
          td {{
            text-align: left;
            padding: 8px;
            border-bottom: 1px solid #ddd;
          }}
          th {{
            background-color: #f2f2f2;
          }}
          .birthday {{
            color: #c00764;
            font-weight: bold;
          }}
          .regards {{
            color: blue
          }}
        </style>
      </head>
      <body>
        <h1>Birthday List</h1>
        <br/>
        <p>Dear colleagues,</p>
        <p>Today is a special day! We have the following coworkers who are celebrating their birthday:</p>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Department</th>
            </tr>
          </thead>
          <tbody>
            {tr_str}
          </tbody>
        </table>
        <br/>
        <p class="birthday">Let's all wish them a very happy birthday!</p>
        <p class="regards">Best regards,</p>
        
        <a href='mailto:{PERSONAL_EMAIL_SENDER}'>{PERSONAL_EMAIL_SENDER_NAME}</a>

      </body>
    </html>

    """

    return message_text, birthday_mail


def send_mail(message_text: str, message_html: str, to: List[str], cc: List[str]):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        print(f"Sending Email: {email_sender}")
        print(f"Sender Email Password: {password}")
        server.login(email_sender, password)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Birthday Remainder Message"
        message["From"] = email_sender
        message["To"] = ','.join(to)
        message["Cc"] = ','.join(cc)

        p1 = MIMEText(message_text, "plain")
        p2 = MIMEText(
            message_html,
            "html",
        )

        message.attach(p1)
        message.attach(p2)

        receivers = to+cc

        server.login(email_sender, password)
        server.sendmail(from_addr=email_sender, to_addrs=receivers, msg=message.as_string())
