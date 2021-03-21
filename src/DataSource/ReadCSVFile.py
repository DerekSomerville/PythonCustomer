import csv
import subprocess
from pathlib import Path

class ReadCSVFile :

    filePathPrefix = str(Path("../../resource/").resolve())
    def getFileData(self, directory,  fileName):
        fileData = []
        with open(self.filePathPrefix + "/" + directory + fileName,'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self,directory, fileName, numerOfLines):
        return self.getFileData(directory, fileName)[-1*numerOfLines]
