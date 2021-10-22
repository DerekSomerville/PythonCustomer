from src.DataSource.DataSourceConstants import *
from src.DataSource.WriteToFile import WriteToFile

class ErrorLogging:

    _instance = None
    write_error_log = WriteToFile(ERRORLOG_FOLDER,ERROR_LOG)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ErrorLogging, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def write_to_log(self,method,message):
        print("Method: ",method," Message: ",message)
        self.write_error_log.write_to_file(method + "," + message)

def main():
    error_logging = ErrorLogging()
    error_logging.write_to_log("my_method","Hello World")

if __name__ == "__main__":
    main()
