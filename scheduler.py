from select import select
from task import Task
from syscall import SystemCall
from queue import Queue

class Scheduler:
    """OS process scheduler"""

    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}
        self.exit_waiting = {}
        self.read_waiting = {}
        self.write_waiting = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def exit(self,task):
        print(f"Task {task.tid} terminated")
        del self.taskmap[task.tid]
        # Get tasks waiting for this to exit back to life
        for task in self.exit_waiting.pop(task.tid,[]):
            self.schedule(task)

    def waitforexit(self,task,waittid):
        if waittid in self.taskmap:
            self.exit_waiting.setdefault(waittid,[]).append(task)
            return True
        else:
            return False        

    def waitforread(self,task,fd):
        self.read_waiting[fd] = task
       
    def waitforwrite(self,task,fd):
        self.write_waiting[fd] = task

    def schedule(self, task):
        self.ready.put(task)

    def iopoll(self,timeout):
        if self.read_waiting or self.write_waiting:
            r,w,e = select(self.read_waiting, self.write_waiting,[],timeout)
            for fd in r: 
                self.schedule(self.read_waiting.pop(fd))
            for fd in w: 
                self.schedule(self.write_waiting.pop(fd))

    def iotask(self):
        while True:
            if self.ready.empty():
                self.iopoll(None) # If sockets arrays are not empty it blocks until some socket will be ready
            else:
                self.iopoll(0) # Never blocks
            yield
   

    def mainloop(self):
        self.new(self.iotask()) # Launch I/O polls
        while self.taskmap:
            task = self.ready.get()
            try:
                # result can contain an instance of the SystemCall subclass
                result = task.run()
                if isinstance(result,SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)
