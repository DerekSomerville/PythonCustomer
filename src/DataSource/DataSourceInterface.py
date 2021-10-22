from abc import ABC, abstractmethod

class DataSourceInterface(ABC):

    @abstractmethod
    def get_data(self,table_name,field_names):
        pass
