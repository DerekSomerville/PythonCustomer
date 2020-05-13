from DataSourceInterface import DataSourceInterface
from DBConnection import DBConnection
from DBExecuteSQL import DBExecuteSQL
import sqlite3

class DatabaseGetData(DataSourceInterface):

    dbExecuteSQL = DBExecuteSQL()

    def generateSelectStatement(self,tableName,fieldNames):
        return "Select * from " + tableName

    def getData(self,tableName,fieldNames):
        sqlData = []
        selectStatement = self.generateSelectStatement(tableName,fieldNames)
        try:
            sqlData = self.dbExecuteSQL.executeSqlSelect(selectStatement)
        except sqlite3.Error as sqlExp:
            print("getData:An error occurred:", sqlExp.args[0])

        return sqlData
