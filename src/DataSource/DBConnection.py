import sqlite3
from src.Utilities.ErrorLogging import ErrorLogging
class DBConnection:

    dbFileName = "resource/Database/applicationDB.db";
    inMemoryDatabase = ":memory:";
    sqlLiteUrl = dbFileName;
    errorLogging = ErrorLogging()

    def setInMemory(self):
        self.sqlLiteUrl = self.inMemoryDatabase

    def createConnection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.sqlLiteUrl)
        except sqlite3.Error as sqlExp:
            self.errorLogging.writeToLog("DBConnection.createConnection","An error occurred:" + sqlExp.args[0])
        return connection

def main():
    connection = DBConnection()
    connection.createConnection()

if __name__ == "__main__":
    main()
