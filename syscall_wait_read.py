from syscall import SystemCall 

class WaitRead(SystemCall):
    def __init__(self,f):
        self.f = f

    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforread(self.task,fd)