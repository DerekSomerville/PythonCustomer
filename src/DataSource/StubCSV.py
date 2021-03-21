from src.DataSource.ReadInterface import ReadInterface


class StubCSV(ReadInterface):

    def getConfig(self, directory, fileName):
        stubData = [['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234']]
        return stubData
