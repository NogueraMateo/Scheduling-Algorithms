class PCB:

    def __init__(self, at: int, bt: int):
        self.__arrival_time: int = at
        self.__burst_time: int = bt
        self.__completion_time: int = 0
        self.__waiting_time: int = 0
        self.__response_time: int = -1
        self.__expropiation_time: int = 0
        self.__time_excecuted: int = 0
        self.__is_done: bool = False

    
    def get_at(self):
        return self.__arrival_time
    
    def get_bt(self):
        return self.__burst_time
    
    def get_ct(self):
        return self.__completion_time
    
    def get_wt(self):
        return self.__waiting_time
    
    def get_rt(self):
        return self.__response_time
    
    def get_et(self):
        return self.__expropiation_time
    
    def get_te(self):
        return self.__time_excecuted
    
    def is_done(self):
        return self.__is_done

    def set_ct(self, ct: int):
        self.__completion_time = ct

    def set_wt(self, wt: int):
        self.__waiting_time = wt
    
    def set_rt(self, rt: int):
        self.__response_time = rt
    
    def set_et(self, et: int):
        self.__expropiation_time = et
    
    def set_te(self, te: int):
        self.__time_excecuted = te
    
    def set_done(self):
        self.__is_done = True