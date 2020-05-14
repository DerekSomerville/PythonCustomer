from src.Entities.Customer import Customer
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DBSetup import DBSetup
from src.DataSource.DatabaseGetData import DatabaseGetData
from src.DataSource.DBExecuteSQL import DBExecuteSQL

class CustomerDatabaseMapping:

    customerTableName = Customer.dataSourceName

    emailAddressPosition = 0
    firstNamePosition = 1
    lastNamePosition = 2
    passwordPosition = 3

    dataSourceFields = ["emailAddress","firstName","lastName","password"]

    dbSetup = DBSetup()
    dataSource = DatabaseGetData()

    def createCustomer(self, customerDetails):
        customer = Customer(
            customerDetails[self.emailAddressPosition],
            customerDetails[self.firstNamePosition],
            customerDetails[self.lastNamePosition],
            customerDetails[self.passwordPosition]
        )
        return customer
    

    def getCustomerDataFromFile(self):
        customerFileReader = ReadCSVFile()
        return customerFileReader.getFileData("Entities/",self.customerTableName + ".csv")

    def customerDataBaseSetup(self):
        self.dbSetup.dropTable(self.customerTableName)
        self.dbSetup.createTable(self.customerTableName,self.dataSourceFields)
        customerInsertSql = self.dbSetup.generateInsertStatement(self.customerTableName,self.dataSourceFields)
        customerData = self.getCustomerDataFromFile()
        self.dbSetup.populateEntity(customerInsertSql,customerData)

    def getCustomerData(self):
        return self.dataSource.getData(self.customerTableName,self.dataSourceFields)

    def createAllCustomers(self):
        allCustomers = []
        allCustomerData = self.getCustomerData()
        for customerRow in allCustomerData:
            customer = self.createCustomer(customerRow)
            allCustomers.append(customer)
        return allCustomers

def main():
    dbExecuteSQL = DBExecuteSQL()
    #dbExecuteSQL.switchToInMemory()
    customerDatabaseMapping = CustomerDatabaseMapping()
    customerDatabaseMapping.customerDataBaseSetup()
    print(customerDatabaseMapping.getCustomerData())
    allCustomers = customerDatabaseMapping.createAllCustomers()
    print(len(allCustomers))
    print(dbExecuteSQL.getListOfTables())

if __name__ == "__main__":
    main()
