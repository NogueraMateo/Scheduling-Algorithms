import sys
sys.path.append("/STCF/")
from Pcb import PCB

class Process:

    def __init__(self, tag: str, at: int, bt: int):
        self._tag: str = tag
        self._pcb: PCB = PCB()
        self._burst_time: int = bt
        self._arrival_time: int = at
        
        self._completion_time: int = 0
        self._waiting_time: int = 0
        self._response_time: int = -1
        self.is_done: bool = False


    def get_pcb(self) -> PCB:
        return self._pcb


    def info(self):
        print(f"Tag: {self._tag}   AT: {self._arrival_time}  BT: {self._burst_time}   CT: {self._completion_time}   WT: {self._waiting_time}    RT: {self._response_time}")
