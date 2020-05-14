from src.DataSource.DataSourceInterface import DataSourceInterface
from src.DataSource.DBConnection import DBConnection
from src.DataSource.DBExecuteSQL import DBExecuteSQL
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
