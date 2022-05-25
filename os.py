from scheduler import Scheduler
from syscall_get_tid import GetTid
from syscall_kill_task import KillTask
from syscall_new_task import NewTask

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

def newfoo():
    mytid = yield GetTid()
    print("I'm gonna create a new task foo, kill it and exit", mytid)
    newtid = yield NewTask(foo())
    print(f"Done {newtid}, now let's kill it", mytid)
    yield KillTask(newtid)
    print(f"Done {newtid}, exit", mytid)


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.new(newfoo())
sched.mainloop()
