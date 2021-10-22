from src.EntitiesDatabaseMapping.CustomerDatabaseMapping import CustomerDatabaseMapping

class DatabaseSetup:

    customer_database_mapping = None

    def __init__(self):
        self.customer_database_mapping = CustomerDatabaseMapping()

    def setup(self):
        self.customer_database_mapping.customer_data_base_setup()

def main():
    database_setup = DataBaseSetup()
    database_setup.setup()

if __name__ == "__main__":
    main()
