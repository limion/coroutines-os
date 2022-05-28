from socket import AF_INET, SOCK_DGRAM, socket
from scheduler import Scheduler
from syscall_get_tid import GetTid
from syscall_wait_read import WaitRead
from syscall_wait_write import WaitWrite

def server(port):
    mytid = yield GetTid()
    print("Server starting",mytid)
    sock = socket(AF_INET ,SOCK_DGRAM)
    sock.bind(("",port))
    while True:
        yield WaitRead(sock)
        message, client_address = sock.recvfrom(2048)
        text = message.decode()
        print(text," from ", client_address, mytid)
        yield WaitWrite(sock)
        sock.sendto(text.upper().encode(), client_address)
        


def heartbeat():
    """Idle task"""
    while True:
        #print(".",end="")
        yield

sched = Scheduler()
sched.new(heartbeat())
sched.new(server(14000))
sched.mainloop()