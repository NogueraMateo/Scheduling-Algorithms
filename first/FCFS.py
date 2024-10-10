from abc import ABC, abstractmethod

class FCFSInterface(ABC):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def start_processing(self):
        pass

    @abstractmethod
    def _order_queue(self):
        pass

    @abstractmethod
    def _excecute_process(self):
        pass

    @abstractmethod
    def _calculate_metrics(self):
        pass

    @abstractmethod
    def _read_file(self, filename: str):
        pass