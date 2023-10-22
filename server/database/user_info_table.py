from ..models.db_model import UserInfoModel
from ..constants import (
    USER_TABLE_NAME,
    USER_TABLE_COLUMNS,
    DATABASE_URL,
    TABLE_CREATE_SCRIPT,
)
import sqlite3


class UserInfoTable:

    """User Info Table

    initialize the sqlite3 database, if in case it fails to create a table
    or fails to connect to the database it would panic and exit the program
    """

    def __init__(self):
        """User Info Table Constructor
        @param table_name string
        @param field_len usize
        @returns self

        Initializes UserInfoTable, crates a table and initialize connection
        """

        self.table_name = USER_TABLE_NAME
        self.fields_len = len(USER_TABLE_COLUMNS)

        try:
            self.connection = sqlite3.connect(DATABASE_URL)
        except Exception as e:
            print(f"Cannot connected to DB: {e}")
            exit(0)

        cursor = self.connection.cursor()

        try:
            cursor.execute(TABLE_CREATE_SCRIPT)
        except Exception as e:
            print(f"Cannot execute: {TABLE_CREATE_SCRIPT}, Error: {e}")

    def insert_into_database(self, field_values: UserInfoModel) -> bool:
        """Insert Into Database Table
        @param field_values UserInfoModel
        @returns bool

        If the insert is success it returns True
        and if not then False
        """
        cursor = self.connection.cursor()

        try:
            cursor.execute(
                f"""
                    INSERT INTO {self.table_name} VALUES (
                        '{field_values.full_name}'
                        '{field_values.personal_mail}'
                        '{field_values.work_email}',
                        '{field_values.birth_date}',
                        '{field_values.phone}',
                        '{field_values.preferred_method}'
                        );"""
            )

        except Exception as e:
            print(f"Cannot Insert: {field_values}, Error: {e}")
            return False

        self.connection.commit()

        return True
