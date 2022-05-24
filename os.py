from scheduler import Scheduler
from syscall_get_tid import GetTid

def foo():
    '''To request the service of the scheduler, task
will use the yield statement with a value'''

    mytid = yield GetTid()
    for i in range(10):
        print("I'm foo ",mytid)
        yield

def bar():
    mytid = yield GetTid()
    for i in range(5):
        print("I'm bar ",mytid)
        yield


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()
