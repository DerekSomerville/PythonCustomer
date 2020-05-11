from DataSourceInterface import DataSourceInterface
from DBConnection import DBConnection

class DatabaseGetData(DataSourceInterface):

    dbConnector = DBConnection()
    connection = None

    def __init__(self):
        self.connection = self.dbConnector.createConnection()

    def setDBConnector(self,dbConnector):
        self.dbConnector = dbConnector
        self.connection = dbConnector.createConnection()

    def generateSelectStatement(self,tableName,fieldNames):
        return "Select * from " + tableName

    def getData(self,tableName,fieldNames):
        sqlData = []
        selectStatement = self.generateSelectStatement(tableName,fieldNames)
        selectCursor = self.connection.cursor()
        selectCursor.execute(selectStatement)
        for row in selectCursor:
            sqlData.append(row)
        selectCursor.close()
        return sqlData
