from src.DataSource.DataSourceConstants import *
from src.DataSource.WriteToFile import WriteToFile

class ErrorLogging:

    _instance = None
    writeErrorLog = WriteToFile(ERRORLOG_FOLDER,ERROR_LOG)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ErrorLogging, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def writeToLog(self,method,message):
        print("Method: ",method," Message: ",message)
        self.writeErrorLog.writeToFile(method + "," + message)

def main():
    errorLogging = ErrorLogging()
    errorLogging.writeToLog("myMethod","Hello World")

if __name__ == "__main__":
    main()
