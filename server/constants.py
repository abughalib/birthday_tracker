""" Constants

Contains all the constants values used in the entire project
"""

import re  # For date DATE_DELIMITATOR escape

# Database Configuration
DATABASE_URL = "database.db"
USER_TABLE_NAME = "users_info"
USER_TABLE_COLUMNS = [
    "full_name",
    "personal_email",
    "work_email",
    "birth_date",
    "phone",
    "preferred_method",
]
TABLE_CREATE_SCRIPT = f"""
CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME} (
    {USER_TABLE_COLUMNS[0]} BLOB,
    {USER_TABLE_COLUMNS[1]} BLOB,
    {USER_TABLE_COLUMNS[2]} BLOB,
    {USER_TABLE_COLUMNS[3]} TEXT,
    {USER_TABLE_COLUMNS[4]} BLOB,
    {USER_TABLE_COLUMNS[5]} BLOB
);
"""

# FIELD_VALIDATIONS
PHONE_REGEX = r"\b\d{10}\b"
COMPANY_DOMAIN = r"abc.com"
WORK_EMAIL_REGEX = rf"\b[\w\.]+@{COMPANY_DOMAIN}\b"
PERSONAL_EMAIL_REGEX = r"\b[\w\.]+@\w+\.\w+\b"
DATE_DELIMITATOR = "-"
DATE_REGEX = rf"\b\d{{1,2}}{re.escape(DATE_DELIMITATOR)}\d{{1,2}}{re.escape(DATE_DELIMITATOR)}\d{{4}}\b"
PREFERRED_METHODS = ("PERSONAL_EMAIL", "WORK_EMAIL", "WHATSAPP", "TEAMS", "TEXT")

# User Environment
PUBLIC_KEY = 'BIRTHDAY_TRACKER_PUBLIC_KEY'
PRIVATE_KEY = 'BIRTHDAY_TRACKER_PRIVATE_KEY'

# Email Environment
PERSONAL_MAIL_SENDER = "BIRTHDAY_TRACKER_PERSONAL_EMAIL_SENDER"
PERSONAL_MAIL_SENDER_PASSWORD = "BIRTHDAY_TRACKER_PERSONAL_EMAIL_SENDER_PASSWORD"

# Email Sender Information
PERSONAL_EMAIL_SENDER = 'abughalib64@gmail.com'
PERSONAL_EMAIL_SENDER_NAME = 'Abu Ghalib'
