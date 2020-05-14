import sqlite3
class DBConnection:

    dbFileName = "resource/Database/applicationDB.db";
    inMemoryDatabase = ":memory:";
    sqlLiteUrl = dbFileName;

    def setInMemory(self):
        self.sqlLiteUrl = self.inMemoryDatabase

    def createConnection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.sqlLiteUrl)
        except sqlite3.Error as sqlExp:
            print("createConnection:An error occurred:", sqlExp.args[0])
        return connection

def main():
    connection = DBConnection()
    connection.createConnection()

if __name__ == "__main__":
    main()
