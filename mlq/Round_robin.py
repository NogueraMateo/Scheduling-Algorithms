from Pcb import PCB
from Process import Process

class ProcessExpropiatedException(Exception):
    pass


class ProcessFinishedException(Exception):
    pass


class RoundRobin:

    def __init__(self, quantum: int, processes: list[Process], time: int = 0, isFair: bool = True):
        self.__quantum: int = quantum
        self.__time: int = time 
        self.__initial_time: int = time
        self.__queue: list[Process] = processes
        self.__current_process_started: int = 0
        self.__current_process_index: int = 0
        self.__avg_ct: float = 0.0
        self.__avg_wt: float = 0.0
        self.__avg_rt: float = 0.0

    
    def start_processing(self):
        self.__order_queue()
        next_process = self.__next_process()

        while next_process is not None:

            try:
                
                self.__excecute_process(next_process)

            except ProcessExpropiatedException:
                print(f"Expropiated {next_process.get_tag()} at time {self.__time}")
                next_process = self.__next_process()
                

    def get_time(self) -> int:
        return self.__time


    def __excecute_process(self, p: Process) -> None:
        self.__current_process_started = self.__time
        self.__current_process_index = self.__queue.index(p)
        remaining_time = self.__state_restore(p)
        
        for i in range(self.__quantum):
            
            self.__time += 1
            remaining_time -= 1

            if remaining_time == 0:
                self.__state_save(p)
                self.__mark_process_done(p)
                raise ProcessExpropiatedException

            if i == self.__quantum - 1:
                self.__state_save(p)
                raise ProcessExpropiatedException


    def __next_process(self) -> Process:
        try:
            if self.__time == self.__initial_time:
                return self.__queue[0]

            for i in range(len(self.__queue) - self.__current_process_index + 1):
                p = self.__queue[self.__current_process_index + i +1]
                if not p.get_pcb().is_done():
                    return p

            raise IndexError        
        except IndexError:
            for p in self.__queue:
                if not p.get_pcb().is_done():
                    return p
                continue
        
        return None
    
    
    def __order_queue(self) -> None:
        if self.__queue[-1].get_tag().startswith("p"):
            self.__queue.sort(key= lambda p: (p.get_pcb().get_at(), int(p.get_tag()[1:])))
        else:
            self.__queue.sort(key= lambda p: (p.get_pcb().get_at(), p.get_tag()))
        print("Queue ordered in the following order: ")
        for p in self.__queue:
            print(p.get_info())

    
    def __state_save(self, p: Process) -> None:
        pcb = p.get_pcb()
        time_excecuted = self.__time - self.__current_process_started
        pcb.set_et(self.__time)
        pcb.set_te(pcb.get_te() + time_excecuted)

        if pcb.get_rt() < 0:
            pcb.set_rt(self.__current_process_started)

    
    def __state_restore(self, p: Process) -> None:
        pcb = p.get_pcb()
        return pcb.get_bt() - pcb.get_te()


    def __mark_process_done(self, p: Process) -> None:
        pcb = p.get_pcb()
        pcb.set_done()

        pcb.set_ct(self.__time)
        pcb.set_wt(pcb.get_ct() - pcb.get_at() - pcb.get_bt())
        pcb.set_tat(pcb.get_ct() - pcb.get_at())
    

    def __calculate_metrics(self):
        pass
    

    def get_metrics(self):
        for p in self.__queue:
            print(p.get_info())
