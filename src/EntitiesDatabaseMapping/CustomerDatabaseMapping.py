from src.Entities.Customer import Customer
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DBSetup import DBSetup
from src.DataSource.DatabaseGetData import DatabaseGetData
from src.DataSource.DBExecuteSQL import DBExecuteSQL
from src.DataSource.DataSourceConstants import *
from src.Utilities.ErrorLogging import ErrorLogging

class CustomerDatabaseMapping:

    error_logging = ErrorLogging()
    customer_table_name = Customer.data_source_name

    email_address_position = 0
    first_name_position = 1
    last_name_position = 2
    password_position = 3

    data_source_fields = ["email_address","first_name","last_name","password"]

    db_setup = DBSetup()
    data_source = DatabaseGetData()

    def create_customer(self, customer_details):
        customer = Customer(
            customer_details[self.email_address_position],
            customer_details[self.first_name_position],
            customer_details[self.last_name_position],
            customer_details[self.password_position]
        )
        return customer

    def validate_data_from_file_header(self, header):
        return header == self.data_source_fields

    def get_customer_data_from_file(self):
        customer_file_reader = ReadCSVFile()
        customer_data = customer_file_reader.get_file_data(ENTITIES_FOLDER,self.customer_table_name + ".csv")
        header = customer_data.pop(0)
        if not self.validate_data_from_file_header(header):
            print("CustomerDatabaseMapping.get_customer_data_from_file","Not validate_data_from_file_header")
        return customer_data

    def customer_create_table(self):
        try:
            self.db_setup.drop_table(self.customer_table_name)
            self.db_setup.create_table(self.customer_table_name,self.data_source_fields)
        except:
            print("CustomerDatabaseMapping.customer_create_table","An error occurred:" )

    def customer_populate_data_source(self):
        customer_insert_sql = self.db_setup.generate_insert_statement(self.customer_table_name,self.data_source_fields)
        customer_data = self.get_customer_data_from_file()
        try:
            self.db_setup.populate_entity(customer_insert_sql,customer_data)
        except:
            print("CustomerDatabaseMapping.customer_create_table","An error occurred:" )

    def customer_data_base_setup(self):
        self.customer_create_table()
        self.customer_populate_data_source()

    def get_customer_data(self):
        return self.data_source.get_data(self.customer_table_name,self.data_source_fields)

    def create_all_customers(self):
        all_customers = []
        all_customer_data = self.get_customer_data()
        for customer_row in all_customer_data:
            customer = self.create_customer(customer_row)
            all_customers.append(customer)
        return all_customers

def main():
    db_execute_sql = DBExecuteSQL()
    #db_execute_sql.switch_to_in_memory()
    customer_database_mapping = CustomerDatabaseMapping()
    customer_database_mapping.customer_data_base_setup()
    print(customer_database_mapping.get_customer_data())
    all_customers = customer_database_mapping.create_all_customers()
    print(len(all_customers))
    print(db_execute_sql.get_list_of_tables())

if __name__ == "__main__":
    main()
