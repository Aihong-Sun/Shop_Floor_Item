
class AGV:
    def __init__(self,idx):
        self.idx=idx
        self.trace=[0]
        self.using_time=[]
        self._on=[]
        self.Current_Site=0
        self.start=0
        self.end=0

    def send_to(self,site,s,t,load=None):
        self.start=s
        self.end=self.start+t
        self.using_time.append([self.start,self.end])
        self._on.append(load)
        self.Current_Site=site
        self.trace.append(site)