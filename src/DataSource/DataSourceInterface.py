from abc import ABC, abstractmethod

class DataSourceInterface(ABC):

    @abstractmethod
    def getData(self,tableName,fieldNames):
        pass
