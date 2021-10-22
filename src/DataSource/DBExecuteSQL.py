import sqlite3
from src.DataSource.DBConnection import DBConnection
from src.Utilities.ErrorLogging import ErrorLogging

class DBExecuteSQL(object):

    db_connector = DBConnection()
    error_logging = ErrorLogging()
    connection = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBExecuteSQL, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def set_db_connector(self,db_connector):
        self.db_connector = db_connector
        self.connection = None

    def get_connection(self):
        if self.connection == None:
            try:
                self.connection = self.db_connector.create_connection()
            except sqlite3.Error as sql_exp:
                self.error_logging.write_to_log("DBExecuteSQL.get_connection","An error occurred:" + sql_exp.args[0])
        return self.connection

    def execute_sql_command(self,sql_command):
        try:
            execute_cursor = self.get_connection().cursor()
            execute_cursor.execute(sql_command)
            execute_cursor.close()
        except sqlite3.Error as sql_exp:
            self.error_logging.write_to_log("DBExecuteSQL.execute_sql_command","An error occurred:" + sql_exp.args[0])
            self.error_logging.write_to_log("DBExecuteSQL.execute_sql_command","With command:" + sql_command)
            raise
        self.get_connection().commit()

    def insert_data(self, sql_command, data_rows):
        insert_data_cursor = self.get_connection().cursor()
        try:
            insert_data_cursor.executemany(sql_command,data_rows)
        except sqlite3.Error as sql_exp:
            self.error_logging.write_to_log("DBExecuteSQL.insert_data","An error occurred:" + sql_exp.args[0])
        insert_data_cursor.close()
        self.get_connection().commit()

    def execute_sql_select(self,select_command):
        sql_data = []
        try:
            select_cursor = self.get_connection().cursor()
            select_cursor.execute(select_command)
            sql_data = select_cursor.fetchall()
        except sqlite3.Error as sql_exp:
            self.error_logging.write_to_log("DBExecuteSQL.execute_sql_select","An error occurred:" + sql_exp.args[0])
            self.error_logging.write_to_log("DBExecuteSQL.execute_sql_select","With command:" + select_command)
            raise
        select_cursor.close()
        return sql_data

    def get_list_of_tables(self):
        return self.execute_sql_select("SELECT name FROM sqlite_master WHERE type='table';")

    def switch_to_in_memory(self):
        self.db_connector.set_in_memory()
        self.connection = None
