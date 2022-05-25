from syscall import SystemCall


class WaitTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid

    def handle(self):
        result = self.sched.waitforexit(self.task,self.tid)
        self.task.sendval = result
        # If waiting for a non-existent task,
        # return immediately without waiting
        if not result:
            self.sched.schedule(self.task)
