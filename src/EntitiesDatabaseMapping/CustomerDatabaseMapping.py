from src.Entities.Customer import Customer
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DBSetup import DBSetup
from src.DataSource.DatabaseGetData import DatabaseGetData
from src.DataSource.DBExecuteSQL import DBExecuteSQL
from src.DataSource.DataSourceConstants import *
from src.Utilities.ErrorLogging import ErrorLogging

class CustomerDatabaseMapping:

    errorLogging = ErrorLogging()
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

    def validateDataFromFileHeader(self, header):
        return header == self.dataSourceFields

    def getCustomerDataFromFile(self):
        customerFileReader = ReadCSVFile()
        customerData = customerFileReader.getFileData(ENTITIES_FOLDER,self.customerTableName + ".csv")
        header = customerData.pop(0)
        if not self.validateDataFromFileHeader(header):
            self.errorLogging.writeToLog("CustomerDatabaseMapping.getCustomerDataFromFile","An error occurred:" + sqlExp.args[0])
        return customerData

    def customerCreateTable(self):
        try:
            self.dbSetup.dropTable(self.customerTableName)
            self.dbSetup.createTable(self.customerTableName,self.dataSourceFields)
        except:
            self.errorLogging.writeToLog("CustomerDatabaseMapping.customerCreateTable","An error occurred:" + sys.exc_info()[0])

    def customerPopulateDataSource(self):
        customerInsertSql = self.dbSetup.generateInsertStatement(self.customerTableName,self.dataSourceFields)
        customerData = self.getCustomerDataFromFile()
        try:
            self.dbSetup.populateEntity(customerInsertSql,customerData)
        except:
            self.errorLogging.writeToLog("CustomerDatabaseMapping.customerCreateTable","An error occurred:" + sys.exc_info()[0])

    def customerDataBaseSetup(self):
        self.customerCreateTable()
        self.customerPopulateDataSource()

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
