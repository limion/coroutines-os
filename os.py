from scheduler import Scheduler
from syscall_get_tid import GetTid
from syscall_new_task import NewTask
from syscall_wait_task import WaitTask

def foo():
    '''To request the service of the scheduler, task
will use the yield statement with a value'''

    mytid = yield GetTid()
    for i in range(10):
        print("I'm foo ",mytid)
        yield

def main():
    mytid = yield GetTid()
    print("I'm the main task", mytid)
    childtid = yield NewTask(foo())
    print("Waiting for child", childtid)
    yield WaitTask(childtid)
    print("Child done")

sched = Scheduler()
sched.new(main())
sched.mainloop()
