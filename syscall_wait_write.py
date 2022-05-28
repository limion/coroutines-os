from syscall import SystemCall


class WaitWrite(SystemCall):
    def __init__(self,f):
        self.f = f

    def handle(self):
        fd = self.f.fileno()
        self.sched.waitforwrite(self.task,fd)
