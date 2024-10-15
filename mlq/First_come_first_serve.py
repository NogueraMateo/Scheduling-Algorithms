from Process import Process


class FCFS:

    def __init__(self, proceses: list[Process], time: int):
        self._ready_queue: list[Process] = proceses
        self._current_process: int = 0
        self._time: int = time

        self.__avg_ct: float = 0.0
        self.__avg_wt: float = 0.0
        self.__avg_rt: float = 0.0
        self.__avg_tat: float = 0.0
    
    
    def start_processing(self):
        self._order_queue()
        for p in self._ready_queue:
            self._excecute_process()
        
        self._calculate_metrics()


    def get_time(self):
        return self._time

    
    def _order_queue(self):
        if self._ready_queue[-1].get_tag().startswith("p"):
            self._ready_queue.sort(key= lambda p: (p.get_pcb().get_at(), int(p.get_tag()[1:])))
        else:
            self._ready_queue.sort(key= lambda p: (p.get_pcb().get_at(), p.get_tag()))
        
        for p in self._ready_queue:
            print(p.get_info())

    
    def _excecute_process(self):
        
        process = self._ready_queue[self._current_process]
        pcb = process.get_pcb()
        pcb.set_rt(self._time)
        pcb.set_wt(self._time - pcb.get_at()) 

        self._time += pcb.get_bt()

        pcb.set_ct(self._time) 
        pcb.set_tat(pcb.get_ct() - pcb.get_at())
        
        self._current_process += 1
    
    
    def _calculate_metrics(self):

        total_processes: int = len(self._ready_queue)

        for p in self._ready_queue:
            pcb = p.get_pcb()
            self.__avg_ct += pcb.get_ct()
            self.__avg_wt += pcb.get_wt()
            self.__avg_rt += pcb.get_rt()
            self.__avg_tat += (pcb.get_ct() - pcb.get_at())
        
        self.__avg_ct /= total_processes
        self.__avg_wt /= total_processes
        self.__avg_rt /= total_processes
        self.__avg_tat /= total_processes

    
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
            print(p.get_info())