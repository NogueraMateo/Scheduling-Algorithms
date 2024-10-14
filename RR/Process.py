import sys
sys.path.append("./RR/")

from Pcb import PCB

class Process:
    
    def __init__(self, tag: str, at: int, bt: int):
        self.__tag: str = tag
        self.__pcb: PCB = PCB(at, bt)
    
    def get_tag(self) -> str:
        return self.__tag

    def get_pcb(self) -> PCB:
        return self.__pcb

    def get_info(self) -> str:
        return f"Tag: {self.__tag}  AT: {self.__pcb.get_at()}  BT: {self.__pcb.get_bt()}  CT: {self.__pcb.get_ct()}  WT: {self.__pcb.get_wt()}  RT: {self.__pcb.get_rt()}"
