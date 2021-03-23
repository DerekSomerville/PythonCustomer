import csv
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

class Menu:
    def smoothieMenu(self):
        readCSVFile = ReadCSVFile()
        smoothieMenu = readCSVFile.getFileData(entitiesFolder, "Smoothies" + ".csv")
        return smoothieMenu