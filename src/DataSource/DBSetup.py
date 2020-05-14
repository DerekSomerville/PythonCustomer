import sqlite3
from src.DataSource.DBConnection import DBConnection
from src.DataSource.DBExecuteSQL import DBExecuteSQL
from src.Utilities.ErrorLogging import ErrorLogging

class DBSetup:

    dbExecuteSQL = DBExecuteSQL()
    errorLogging = ErrorLogging()

    def generateDropTable(self,tableName):
        return "DROP TABLE IF EXISTS " + tableName

    def dropTable(self,tableName):
        sqlDropTable = self.generateDropTable(tableName)
        try:
            self.dbExecuteSQL.executeSQLCommand(sqlDropTable)
        except sqlite3.Error as sqlExp:
            self.errorLogging.writeToLog("DBSetup.createTable","An error occurred:" + sqlExp.args[0])
            raise

    def generateCreateTableStatement(self,tableName, fieldNames):
        sqlCreateTable =  "CREATE TABLE IF NOT EXISTS " + tableName + "(\n"
        counter = 0;
        fieldUnique = False;
        for columnName in fieldNames:
            if counter == 0:
                fieldUnique = True;
            else:
                sqlCreateTable += ",";

            sqlCreateTable += columnName + " TEXT NOT NULL ";
            if fieldUnique:
                sqlCreateTable += " UNIQUE ";
            counter += 1;
            fieldUnique = False;

        sqlCreateTable += ");";
        return sqlCreateTable;

    def createTable(self,tableName, fieldNames):
        sqlCreateTable = self.generateCreateTableStatement(tableName,fieldNames)
        try:
            self.dbExecuteSQL.executeSQLCommand(sqlCreateTable)
        except sqlite3.Error as sqlExp:
            self.errorLogging.writeToLog("DBSetup.createTable","An error occurred:" + sqlExp.args[0])
            raise

    def generateInsertStatement(self,tableName, fieldNames):
        counter = 0
        sqlColumns = ""
        sqlValues = ""
        sqlUniqueColumn = ""
        sqlInsert = ""
        for columnName in fieldNames:
            if counter == 0:
                sqlUniqueColumn = columnName
            else:
                sqlColumns += ", "
                sqlValues += ", "

            sqlColumns += columnName
            sqlValues += "?"
            counter += 1

        sqlInsert = "INSERT INTO " + tableName + "(" + sqlColumns + ") VALUES(" + sqlValues + ") \n"
        return sqlInsert

    def populateEntity(self, sqlCommand, dataRows):
        try:
            self.dbExecuteSQL.insertData(sqlCommand, dataRows)
        except sqlite3.Error as sqlExp:
            self.errorLogging.writeToLog("DBSetup.populateEntity","An error occurred:" + sqlExp.args[0])
            raise

def main():
    dbSetup = DBSetup()

if __name__ == "__main__":
    main()
