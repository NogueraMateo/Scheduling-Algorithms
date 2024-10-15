from Process import Process
from Pcb import PCB
from Round_robin import RoundRobin
from First_come_first_serve import FCFS

import os

class MLQ:

    def __init__(self, filename: str):
        self.__filename: str = filename
        self.__queues : list[list[Process]] = []
        self.__time: int = 0

        self.__read_file(filename)


    def start_processing(self):
        
        for i in range(len(self.__queues)):

            if len(self.__queues[i]) > 0:
                if i == 0: 
                    rr3 = RoundRobin(3, self.__queues[i], self.__time)
                    rr3.start_processing()
                    self.__time = rr3.get_time()
                elif i == 1:
                    rr5 = RoundRobin(5, self.__queues[i], self.__time)
                    rr5.start_processing()
                    self.__time = rr5.get_time()
                elif i == 2:
                    fcfs = FCFS(self.__queues[i], self.__time)
                    fcfs.start_processing()
                    self.__time = fcfs.get_time()
                

    
    def __read_file(self, filename: str) -> None:
        
        processes: list[Process] = []

        with open(f"./mlq/pruebas/{filename}", "r") as f:
            lines = f.read().splitlines()
            max_queues = 0
            for i in range(len(lines)):
                
                if i == 0 or i == 1:
                    continue
                
                tag, bt, at, queue, priority = lines[i].split(";")
                at = int(at.strip())
                bt = int(bt.strip())
                queue = int(queue.strip())
                max_queues = queue if queue > max_queues else max_queues
                processes.append(Process(tag, at, bt, priority, queue))

        for i in range(max_queues):
            self.__queues.append([])
            
        for p in processes:
            self.__queues[p.get_pcb().get_queue() - 1].append(p)


    def get_metrics(self):
        filename = f"./mlq/results/{self.__filename}"
        folder = os.path.dirname(filename)
        if folder:
            os.makedirs(folder, exist_ok=True)

        total_wt, total_ct, total_rt, total_tat = 0, 0, 0, 0
        num_processes = 0

        with open(filename, "w") as f:
            f.write("# etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT\n")

            for queue in self.__queues:
                for p in queue:
                    pcb = p.get_pcb()

                    wt = pcb.get_wt()
                    ct = pcb.get_ct()
                    rt = pcb.get_rt()
                    tat = pcb.get_tat()

                    
                    total_wt += wt
                    total_ct += ct
                    total_rt += rt
                    total_tat += tat
                    num_processes += 1

                    
                    f.write(f"{p.get_tag()}; {pcb.get_bt()}; {pcb.get_at()}; "
                            f"{pcb.get_queue()}; {pcb.get_priority()}; {wt}; {ct}; {rt}; {tat}\n")

            avg_wt = total_wt / num_processes
            avg_ct = total_ct / num_processes
            avg_rt = total_rt / num_processes
            avg_tat = total_tat / num_processes

            f.write(f"WT={avg_wt:.2f}; CT={avg_ct:.2f}; RT={avg_rt:.2f}; TAT={avg_tat:.2f};\n")

    
def main():
    mlq = MLQ("mlq002.txt")
    mlq.start_processing()
    print("\n\n")
    mlq.get_metrics()

if __name__ == '__main__':
    main()