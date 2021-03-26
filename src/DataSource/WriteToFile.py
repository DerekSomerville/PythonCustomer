from pathlib import Path

class WriteToFile:
    # Here will be the instance stored.
    file = ""
    filePath = str(Path("resource/").resolve())
    directory = ""
    fileName = ""
    def __init__(self,directory,fileName):
        self.directory = directory
        self.fileName = fileName


    def writeToFile(self,logItem):
        if self.file == "":
            self.file = open(self.filePath + "/" + self.directory+ self.fileName,"a")
        self.file.write(str(logItem) + "\n")
