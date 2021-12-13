

class Machine:
    def __init__(self,idx):
        self.index=idx
        self.IB=[]      #输入缓冲区
        self.OB=[]      #输出缓冲区
        self.Processed=[]
        self.using_time=[]
        self.arrive=[]
        self.start=0
        self.end=0

    def handling(self,job):
        st=self.arrive[self.IB.index(job)]
        del self.arrive[self.IB.index(job)]
        if st<=self.end:
            job.handling(self.end)
        else:
            job.handling(st)
        self.end=job.end
        self.IB.remove(job)
        self.OB.append(job)
        job.finish()
        self.using_time.append([job.start,job.end])
        self.Processed.append(job.index)

    def put_into_job(self,job,arrive_t):
        self.arrive.append(arrive_t)
        self.IB.append(job)

    def sequence_handling(self,t):
        Ji=0
        if self.IB!=[]:
            while Ji<len(self.IB):
                if self.end+self.IB[Ji].handling_time[0]<t:
                    self.handling(self.IB[Ji])
                Ji+=1

    def pick_up_job(self,job):
        self.OB.remove(job)

