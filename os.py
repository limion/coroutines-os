from scheduler import Scheduler

def foo():
    while True:
        print("I'm foo")
        yield

def bar():
    while True:
        print("I'm bar")
        yield


sched = Scheduler()
sched.new(foo())
sched.new(bar())
sched.mainloop()