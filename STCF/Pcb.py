import sys
sys.path.append("/STCF/")

class PCB:

    def __init__(self):
        self._expropiation_time: int = 0
        self._time_excecuted: int = 0
    
    
    def get_expropiation_time(self) -> int:
        return self._expropiation_time
    
    
    def get_time_excecuted(self) -> int:
        return self._time_excecuted
    

    def set_expropiation_time(self, new_et: int) -> None:
        self._expropiation_time = new_et
    

    def set_time_excecuted(self, new_te: int) -> None:
        self._time_excecuted = new_te
