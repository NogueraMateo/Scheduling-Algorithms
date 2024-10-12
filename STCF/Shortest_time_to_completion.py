import sys
sys.path.append("/STCF/")
from Process import Process
from Pcb import PCB

class ProcessExpropiatedException(Exception):
    pass

class STCF:

    def __init__(self, filename: str):
        self._ready_queue: list[Process] = []
        self._time: int = 0
        self._current_proc_started: int = 0
        self._avg_completion_time: float = 0.0
        self._avg_waiting_time: float = 0.0
        self._avg_response_time: float = 0.0

        self._read_file(filename)


    def start_processing(self) -> None:
        next_process = self._next_process()

        while next_process is not None:

            try:
                
                self._excecute_process(next_process)

            except ProcessExpropiatedException:
                next_process = self._next_process()
        
        self._calculate_metrics()
    
    
    def _excecute_process(self, p: Process) -> None:
        # Waiting time is the difference between the last time the process was expropiated and the time started executing again
        # but if the proces hasn't executed even once the waiting time is the difference between the current time and the arrival time
        p._response_time = self._time if p._response_time < 0 else p._response_time
        remaining_time = p._burst_time - p.get_pcb().get_time_excecuted()
        
        self._current_proc_started = self._time

        for i in range(p._burst_time - p.get_pcb().get_time_excecuted()):

            if self._has_to_leave(p) or remaining_time == 0:
                self._state_save(p)
                print(f"{p._tag} Expropiated at time {self._time}")
                raise ProcessExpropiatedException

            self._time += 1    
            remaining_time -= 1

            if remaining_time == 0:
                p.is_done = True
                p._completion_time = self._time


    def _has_to_leave(self, p: Process) -> bool:
        return self._next_process() != p

    
    def _next_process(self) -> Process:
        available_procesess = [p for p in self._ready_queue if p._arrival_time <= self._time and not p.is_done]
        if (len(available_procesess) > 1):
            available_procesess.sort(key= lambda p: (p._burst_time, int(p._tag[1:])))
        
        try:
            print(f"Try returning a process")
            available_procesess[0].info()
            return available_procesess[0]
        except IndexError:
            return None



    def _state_save(self, p: Process) -> None:
        process_pcb = p.get_pcb()
        process_pcb.set_expropiation_time(self._time)
        current_te = process_pcb.get_time_excecuted()
        process_pcb.set_time_excecuted(current_te + (self._time - self._current_proc_started))  


    def _state_restore(self, p: Process) -> PCB:
        return p.get_pcb()


    def _read_file(self, filename: str) -> None:
        
        with open(f"./pruebas/{filename}", "r") as f:
            lines = f.read().splitlines()

            for i in range(len(lines)):
                if i == 0:
                    continue
            
                tag, at, bt = lines[i].split("        ")
                
                self._ready_queue.append(Process(tag, int(at.strip()), int(bt.strip())))

        for p in self._ready_queue:
            print(p.info())

    
    def _calculate_metrics(self) -> None:
        for p in self._ready_queue:
            p._waiting_time = (p._completion_time - p._arrival_time) - p._burst_time

    
    def get_metrics(self):
        print(f"Shortest time-to-completion first:\n\n")
        for p in self._ready_queue:
            p.info()


def main():
    stcf = STCF("prueba6.txt")
    stcf.start_processing()
    stcf.get_metrics()


if __name__ == '__main__':
    main()