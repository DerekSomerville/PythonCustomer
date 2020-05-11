from CustomerDatabaseMapping import CustomerDatabaseMapping
from DBSetup import DBSetup

class DataBaseSetup:

    dbSetup = None
    customerDatabaseMapping = None

    def __init__(self):
        self.dbSetup = DBSetup()
        self.customerDatabaseMapping = CustomerDatabaseMapping(self.dbSetup)

    def setup(self):
        self.customerDatabaseMapping.customerDataBaseSetup()

def main():
    databaseSetup = DataBaseSetup()
    databaseSetup.setup()

if __name__ == "__main__":
    main()
