import csv
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

class ReadSmoothieFile:
    def smoothieFile(self):
        readCSVFile = ReadCSVFile()
        smoothieMenu = readCSVFile.getFileData(entitiesFolder, "Smoothies" + ".csv")
        return smoothieMenu