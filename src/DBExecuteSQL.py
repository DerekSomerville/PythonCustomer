import sqlite3
from DBConnection import DBConnection

class DBExecuteSQL(object):

    dbConnector = DBConnection()
    connection = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBExecuteSQL, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def setDbConnector(self,dbConnector):
        self.dbConnector = dbConnector
        self.connection = None

    def getConnection(self):
        if self.connection == None:
            self.connection = self.dbConnector.createConnection()
        return self.connection

    def executeSQLCommand(self,sqlCommand):
        try:
            executeCursor = self.getConnection().cursor()
            executeCursor.execute(sqlCommand)
            executeCursor.close()
        except sqlite3.Error as sqlExp:
            print("executeSQLCommand:An error occurred:", sqlExp.args[0])
            print("With command:", sqlCommand)
            raise
        self.getConnection().commit()

    def insertData(self, sqlCommand, dataRows):
        insertDataCursor = self.getConnection().cursor()
        try:
            insertDataCursor.executemany(sqlCommand,dataRows)
        except sqlite3.Error as sqlExp:
            print("An error occurred in populateEntity:", sqlExp.args[0])
        insertDataCursor.close()
        self.getConnection().commit()

    def executeSqlSelect(self,selectCommand):
        sqlData = []
        try:
            selectCursor = self.getConnection().cursor()
            selectCursor.execute(selectCommand)
            sqlData = selectCursor.fetchall()
        except sqlite3.Error as sqlExp:
            print("executeSqlSelect:An error occurred:", sqlExp.args[0])
            print("With select statement:", selectCommand)
            raise
        selectCursor.close()
        return sqlData

    def getListOfTables(self):
        return self.executeSqlSelect("SELECT name FROM sqlite_master WHERE type='table';")

    def switchToInMemory(self):
        self.dbConnector.setInMemory()
        self.connection = None
