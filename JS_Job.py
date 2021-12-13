from Env.Flow_Shop_Environment.FS_Job import Job
import copy

class Job(Job):
    def __init__(self,idx,handling_time,handling_machine):
        super().__init__(idx,handling_time)
        self.handling_machine=copy.copy(handling_machine)

    def finish(self):
        self.Cur_processed+=self.handling_time[0]
        del self.handling_time[0]

    def update_site(self):
        self.Cur_site=self.handling_machine[0]

    def judge_wether_end(self):
        if len(self.handling_machine)==1 or self.handling_machine==[]:
            self.J=True
            return False
        else:
            return True

    def finished_move(self):
        del self.handling_machine[1]
        if self.handling_machine==[] or len(self.handling_machine)==1:
            self.J = True

    def next_machine(self):
            return self.handling_machine[1]

