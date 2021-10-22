import sqlite3
from src.Utilities.ErrorLogging import ErrorLogging
class DBConnection:

    db_file_name = "resource/Database/application_db.db";
    in_memory_database = ":memory:";
    sql_lite_url = db_file_name;
    error_logging = ErrorLogging()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def set_in_memory(self):
        self.sql_lite_url = self.in_memory_database

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.sql_lite_url)
        except sqlite3.Error as sql_exp:
            self.error_logging.write_to_log("DBConnection.create_connection","An error occurred:" + sql_exp.args[0])
        return connection

def main():
    connection = DBConnection()
    connection.create_connection()

if __name__ == "__main__":
    main()
