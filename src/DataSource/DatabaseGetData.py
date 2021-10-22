from src.DataSource.DataSourceInterface import DataSourceInterface
from src.DataSource.DBConnection import DBConnection
from src.DataSource.DBExecuteSQL import DBExecuteSQL
import sqlite3

class DatabaseGetData(DataSourceInterface):

    db_execute_sql = DBExecuteSQL()

    def generate_select_statement(self,table_name,field_names):
        return "Select * from " + table_name

    def get_data(self,table_name,field_names):
        sql_data = []
        select_statement = self.generate_select_statement(table_name,field_names)
        try:
            sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        except sqlite3.Error as sql_exp:
            print("get_data:An error occurred:", sql_exp.args[0])

        return sql_data
