from socket import AF_INET, SOCK_DGRAM, socket
from scheduler import Scheduler
from syscall_new_task import NewTask
from syscall_get_tid import GetTid


def handle_client(sock):
    mytid = yield GetTid()
    print("Client handler ID:",mytid)
    message, client_address = sock.recvfrom(2048) #This thing will block the loop until client connection
    text = message.decode()
    print(text," from ", client_address, mytid)
    yield
    sock.sendto(text.upper().encode(), client_address)
    print("Client handler done", mytid)

def server(port):
    mytid = yield GetTid()
    print("Server starting",mytid)
    sock = socket(AF_INET ,SOCK_DGRAM)
    sock.bind(("",port))
    while True:
        yield NewTask(handle_client(sock))


def heartbeat():
    while True:
        mytid = yield GetTid()
        print("Idle task", mytid)
        yield

sched = Scheduler()
sched.new(heartbeat())
sched.new(server(14000))
sched.mainloop()