import sqlite3
from src.DataSource.DBConnection import DBConnection
from src.DataSource.DBExecuteSQL import DBExecuteSQL
from src.Utilities.ErrorLogging import ErrorLogging

class DBSetup:

    db_execute_sql = DBExecuteSQL()
    error_logging = ErrorLogging()

    def generate_drop_table(self,table_name):
        return "DROP TABLE IF EXISTS " + table_name

    def drop_table(self,table_name):
        sql_drop_table = self.generate_drop_table(table_name)
        try:
            self.db_execute_sql.execute_sql_command(sql_drop_table)
        except sqlite3.Error as sql_exp:
            self.error_logging.write_to_log("DBSetup.create_table","An error occurred:" + sql_exp.args[0])
            raise

    def generate_create_table_statement(self,table_name, field_names):
        sql_create_table =  "CREATE TABLE IF NOT EXISTS " + table_name + "(\n"
        counter = 0;
        field_unique = False;
        for column_name in field_names:
            if counter == 0:
                field_unique = True;
            else:
                sql_create_table += ",";

            sql_create_table += column_name + " TEXT NOT NULL ";
            if field_unique:
                sql_create_table += " UNIQUE ";
            counter += 1;
            field_unique = False;

        sql_create_table += ");";
        return sql_create_table;

    def create_table(self,table_name, field_names):
        sql_create_table = self.generate_create_table_statement(table_name,field_names)
        try:
            self.db_execute_sql.execute_sql_command(sql_create_table)
        except sqlite3.Error as sql_exp:
            self.error_logging.write_to_log("DBSetup.create_table","An error occurred:" + sql_exp.args[0])
            raise

    def generate_insert_statement(self,table_name, field_names):
        counter = 0
        sql_columns = ""
        sql_values = ""
        sql_unique_column = ""
        sql_insert = ""
        for column_name in field_names:
            if counter == 0:
                sql_unique_column = column_name
            else:
                sql_columns += ", "
                sql_values += ", "

            sql_columns += column_name
            sql_values += "?"
            counter += 1

        sql_insert = "INSERT INTO " + table_name + "(" + sql_columns + ") VALUES(" + sql_values + ") \n"
        return sql_insert

    def populate_entity(self, sql_command, data_rows):
        try:
            self.db_execute_sql.insert_data(sql_command, data_rows)
        except sqlite3.Error as sql_exp:
            self.error_logging.write_to_log("DBSetup.populate_entity","An error occurred:" + sql_exp.args[0])
            raise

def main():
    db_setup = DBSetup()

if __name__ == "__main__":
    main()
