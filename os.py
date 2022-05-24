from scheduler import Scheduler

def foo():
    for i in range(10):
        print("I'm foo")
        yield

def bar():
    for i in range(5):
        print("I'm bar")
        yield


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()
