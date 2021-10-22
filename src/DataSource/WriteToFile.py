class WriteToFile:
    # Here will be the instance stored.
    file = ""
    file_path = "resource/"
    directory = ""
    file_name = ""

    def __init__(self,directory,file_name):
        self.directory = directory
        self.file_name = file_name


    def write_to_file(self,log_item):
        if self.file == "":
            self.file = open(self.file_path + self.directory+ self.file_name,"a")
        self.file.write(str(log_item) + "\n")
