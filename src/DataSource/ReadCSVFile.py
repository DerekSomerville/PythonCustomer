import csv
import subprocess
import os

class ReadCSVFile :

    filePathPrefix = "resource/"

    def fixWorkingDirectory(self):
        currentWorkingDirectory = os.getcwd()
        while "test" in currentWorkingDirectory or "src" in currentWorkingDirectory:
            os.chdir("../")
            currentWorkingDirectory = os.getcwd()

    def getFileData(self, directory,  fileName):
        self.fixWorkingDirectory()
        fileData = []
        with open(self.filePathPrefix + directory + fileName,'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self,directory, fileName, numerOfLines):
        return self.getFileData(directory, fileName)[-1*numerOfLines]
