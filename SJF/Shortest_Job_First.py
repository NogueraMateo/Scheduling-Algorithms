class Process:

    def __init__(self, tag: str, arrival_time: int, burst_time: int):
        
        self._tag: str = tag
        self._arrival_time: int     = arrival_time
        self._burst_time: int       = burst_time
        self._completion_time: int  = 0
        self._waiting_time: int     = 0
        self._response_time: int    = 0
        self._is_completed: bool = False

    def info(self):
        print(f"Tag: {self._tag}   AT: {self._arrival_time}  BT: {self._burst_time}   CT: {self._completion_time}   WT: {self._waiting_time}    RT: {self._response_time}")


class SJF:

    def __init__(self, filename: str):
        self._ready_queue: list[Process] = []
        self._current_process: int = 0
        self._time: int = 0

        self._avg_completion_time: float = 0.0
        self._avg_waiting_time: float = 0.0
        self._avg_response_time: float = 0.0

        self._read_file(filename)
    

    def _start_processing(self):
        for i in range(len(self._ready_queue)):
            self._execute_process(self._next_process())
        
        self._calculate_metrics()


    def _read_file(self, filename: str):
        
        with open(f"./pruebas/{filename}", "r") as f:

            lines = f.read().splitlines()

            for i in range(len(lines)):
                if i == 0:
                    continue
                
                tag, at, bt = lines[i].split("        ")
                self._ready_queue.append(Process(tag, int(at.strip()), int(bt.strip())))
            

    def _is_at_same(self):
        first_number: int = 0
        for i in range(len(self._ready_queue)):
            if i == 0:
                first_number = self._ready_queue[i]._arrival_time
                continue
            
            if first_number != self._ready_queue[i]._arrival_time:
                return False

        return True


    def _next_process(self) -> Process:
        available_processes = [p for p in self._ready_queue if p._arrival_time <=  self._time and not p._is_completed]
        if len(available_processes) > 1:
            available_processes.sort(key= lambda p: (p._burst_time, int(p._tag[1:])))
        return available_processes[0]


    def _execute_process(self, p: Process):
        p._response_time = self._time
        p._waiting_time = self._time - p._arrival_time
        p._completion_time = self._time + p._burst_time

        self._time += p._burst_time
        p._is_completed = True
    
    
    def _calculate_metrics(self) -> None:
        total_processes: int = len(self._ready_queue)

        for p in self._ready_queue:
            self._avg_completion_time += p._completion_time
            self._avg_waiting_time += p._waiting_time
            self._avg_response_time += p._response_time
        
        self._avg_completion_time /= total_processes
        self._avg_waiting_time /= total_processes
        self._avg_response_time /= total_processes


    def get_metrics(self):
        print(f"First Come First Serve:\n\n")
        for p in self._ready_queue:
            p.info()
        

def main():
    sjf = SJF("prueba5.txt")
    sjf._start_processing()
    sjf.get_metrics()
            

if __name__ == '__main__':
    main()







