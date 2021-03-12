import csv
import subprocess
from pathlib import Path

from src.DataSource.ReadInterface import ReadInterface


class ReadCSVFile(ReadInterface):

    filePathPrefix = str(Path("../resource/").resolve())
    def getConfig(self, directory,  fileName):
        fileData = []
        with open(self.filePathPrefix + "/" + directory + fileName,'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)

        return fileData

    def getLastLines(self,directory, fileName, numerOfLines):
        return self.getConfig(directory, fileName)[-1*numerOfLines]

