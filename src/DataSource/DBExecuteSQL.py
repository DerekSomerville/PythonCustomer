import sqlite3
from src.DataSource.DBConnection import DBConnection
from src.Utilities.ErrorLogging import ErrorLogging

class DBExecuteSQL(object):

    dbConnector = DBConnection()
    errorLogging = ErrorLogging()
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
            try:
                self.connection = self.dbConnector.createConnection()
            except sqlite3.Error as sqlExp:
                self.errorLogging.writeToLog("DBExecuteSQL.getConnection","An error occurred:" + sqlExp.args[0])
        return self.connection

    def executeSQLCommand(self,sqlCommand):
        try:
            executeCursor = self.getConnection().cursor()
            executeCursor.execute(sqlCommand)
            executeCursor.close()
        except sqlite3.Error as sqlExp:
            self.errorLogging.writeToLog("DBExecuteSQL.executeSQLCommand","An error occurred:" + sqlExp.args[0])
            self.errorLogging.writeToLog("DBExecuteSQL.executeSQLCommand","With command:" + sqlCommand)
            raise
        self.getConnection().commit()

    def insertData(self, sqlCommand, dataRows):
        insertDataCursor = self.getConnection().cursor()
        try:
            insertDataCursor.executemany(sqlCommand,dataRows)
        except sqlite3.Error as sqlExp:
            self.errorLogging.writeToLog("DBExecuteSQL.insertData","An error occurred:" + sqlExp.args[0])
        insertDataCursor.close()
        self.getConnection().commit()

    def executeSqlSelect(self,selectCommand):
        sqlData = []
        try:
            selectCursor = self.getConnection().cursor()
            selectCursor.execute(selectCommand)
            sqlData = selectCursor.fetchall()
        except sqlite3.Error as sqlExp:
            self.errorLogging.writeToLog("DBExecuteSQL.executeSqlSelect","An error occurred:" + sqlExp.args[0])
            self.errorLogging.writeToLog("DBExecuteSQL.executeSqlSelect","With command:" + selectCommand)
            raise
        selectCursor.close()
        return sqlData

    def getListOfTables(self):
        return self.executeSqlSelect("SELECT name FROM sqlite_master WHERE type='table';")

    def switchToInMemory(self):
        self.dbConnector.setInMemory()
        self.connection = None
