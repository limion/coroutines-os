from syscall import SystemCall

class KillTask(SystemCall):
    def __init__(self,tid):
        self.tid = tid

    def handle(self):
        task = self.sched.taskmap.get(self.tid)
        if task:
            task.target.close()
            self.task.sendval = True
        else:
            self.task.sendval = False
            self.sched.schedule(self.task)

        self.sched.schedule(self.task)
  