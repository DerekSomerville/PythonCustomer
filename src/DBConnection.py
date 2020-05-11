import sqlite3
class DBConnection:

    dbFileName = "resource/Database/applicationDB.db";
    inMemoryDatabase = ":memory:";
    sqlLiteUrl = dbFileName;

    def createConnection(self):
        try:
            url = "jdbc:sqlite:" + self.sqlLiteUrl;
            connection = sqlite3.connect(self.dbFileName)
        except sqlite3.Error as sqlExp:
            print("An error occurred:", sqlExp.args[0])
        return connection

def main():
    connection = DBConnection()
    connection.createConnection()

if __name__ == "__main__":
    main()
