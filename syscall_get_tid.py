from syscall import SystemCall

class GetTid(SystemCall):
    '''A First System Call'''
    
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)
