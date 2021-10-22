import csv
import subprocess
import os

class ReadCSVFile :

    file_path_prefix = "resource/"

    def fix_working_directory(self):
        current_working_directory = os.getcwd()
        while "test" in current_working_directory or "src" in current_working_directory:
            os.chdir("../")
            current_working_directory = os.getcwd()

    def get_file_data(self, directory,  file_name):
        self.fix_working_directory()
        file_data = []
        with open(self.file_path_prefix + directory + file_name,'rt')as data_file:
            file_reader = csv.reader(data_file)
            for row in file_reader:
                file_data.append(row)
        return file_data

    def get_last_lines(self,directory, file_name, numer_of_lines):
        return self.get_file_data(directory, file_name)[-1*numer_of_lines]
