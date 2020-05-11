import sqlite3
from DBConnection import DBConnection

class DBSetup:

    dbConnector = DBConnection()
    connection = None

    def __init__(self):
        self.connection = self.dbConnector.createConnection()

    def setDBConnector(self,dbConnector):
        self.dbConnector = dbConnector
        self.connection = dbConnector.createConnection()

    def generateDropTable(self,tableName):
        return "DROP TABLE IF EXISTS " + tableName

    def dropTable(self,tableName):
        sqlDropTable = self.generateDropTable(tableName)
        createDropCursor = self.connection.cursor()
        createDropCursor.execute(sqlDropTable)
        self.connection.commit()
        createDropCursor.close()

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
        createTableCursor = self.connection.cursor()
        createTableCursor.execute(sqlCreateTable)
        self.connection.commit()
        createTableCursor.close()

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
        populateEntityCursor = self.connection.cursor()
        populateEntityCursor.executemany(sqlCommand,dataRows)
        self.connection.commit()
        populateEntityCursor.close()

def main():
    dbSetup = DBSetup()

if __name__ == "__main__":
    main()
