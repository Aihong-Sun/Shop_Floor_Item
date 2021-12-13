import copy

class Job:
    def __init__(self,idx,handling_time):
        self.index=idx
        self.handling_time=copy.copy(handling_time)
        self.start=0
        self.end=0
        self.total_PT=sum(handling_time)
        self.Cur_processed=0
        self.Cur_PT=None
        self.Cur_site=0
        self.J=False
        self.arrive=0

    def finish(self):
        self.Cur_processed+=self.handling_time[0]
        del self.handling_time[0]

    def handling(self,start):
        self.start=start
        self.Cur_PT=self.handling_time[0]
        self.end=self.start+ self.Cur_PT

    def judge_wether_end(self):
        if self.J:
            return False
        else:
            return True

    def next_machine(self):
        return self.Cur_site+1