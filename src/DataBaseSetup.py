from src.CustomerDatabaseMapping import CustomerDatabaseMapping
from src.DBSetup import DBSetup

class DataBaseSetup:

    customerDatabaseMapping = None

    def __init__(self):
        self.customerDatabaseMapping = CustomerDatabaseMapping()

    def setup(self):
        self.customerDatabaseMapping.customerDataBaseSetup()

def main():
    databaseSetup = DataBaseSetup()
    databaseSetup.setup()

if __name__ == "__main__":
    main()
