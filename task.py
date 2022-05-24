class Task:
    """A task is a wrapper around a coroutine"""

    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid  # Task ID
        self.target = target  # Target coroutine
        self.sendval = None  # Value to send

    def run(self):
        """run() executes the task to the next yield (a trap)
        It emulates execution of a programm by CPU until the next trap"""
        return self.target.send(self.sendval)
