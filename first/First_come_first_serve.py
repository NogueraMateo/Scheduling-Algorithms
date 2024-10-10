from FCFS import FCFSInterface

class Process:

    def __init__(self, tag: str, arrival_time: int, burst_time: int):
        
        self._tag: str = tag
        self._arrival_time: int     = arrival_time
        self._burst_time: int       = burst_time
        self._completion_time: int  = 0
        self._waiting_time: int     = 0
        self._response_time: int    = 0


    def info(self):
        print(f"Tag: {self._tag}   AT: {self._arrival_time}  BT: {self._burst_time}   CT: {self._completion_time}   WT: {self._waiting_time}    RT: {self._response_time}")


class FCFS(FCFSInterface):

    def __init__(self, filename: str):
        self._ready_queue: list[Process] = []
        self._current_process: int = 0
        self._time: int = 0

        self._avg_completion_time: float = 0.0
        self._avg_waiting_time: float = 0.0
        self._avg_response_time: float = 0.0

        self._read_file(filename)
    
    
    def start_processing(self):
        self._order_queue()
        for p in self._ready_queue:
            self._excecute_process()
        
        self._calculate_metrics()

    
    def _order_queue(self):
        self._ready_queue.sort(key= lambda p: p._arrival_time)

    
    def _excecute_process(self):
        
        process = self._ready_queue[self._current_process]
        process._response_time = self._time
        process._waiting_time = self._time - process._arrival_time

        self._time += process._burst_time

        process._completion_time = self._time
        
        self._current_process += 1
    
    
    def _calculate_metrics(self):

        total_processes: int = len(self._ready_queue)

        for p in self._ready_queue:
            self._avg_completion_time += p._completion_time
            self._avg_waiting_time += p._waiting_time
            self._avg_response_time += p._response_time
        
        self._avg_completion_time /= total_processes
        self._avg_waiting_time /= total_processes
        self._avg_response_time /= total_processes

    
    def _read_file(self, filename):
        
        with open(f"./pruebas/{filename}", "r") as f:

            lines = f.read().splitlines()
            for i in range(len(lines)):
                
                if i == 0:
                    continue
                
                tag, at, bt = lines[i].split("           ")
            
                self._ready_queue.append(Process(tag, int(at.strip()), int(bt.strip())))
                            
    
    def get_metrics(self):
        print(f"First Come First Serve:\n\n")
        for p in self._ready_queue:
            p.info()
        
        

def main():
    fcfs = FCFS("prueba1.txt")
    fcfs.start_processing()
    fcfs.get_metrics()


if __name__ == '__main__':
    main()