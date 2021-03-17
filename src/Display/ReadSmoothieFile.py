import csv
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

def Smoothie_Menu():
    readCSVFile = ReadCSVFile()
    smoothie_Menu = readCSVFile.getFileData(ENTITIES_FOLDER, "Smoothies" + ".csv")
    return smoothie_Menu

