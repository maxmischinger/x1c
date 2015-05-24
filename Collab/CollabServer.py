from socket import *
import _thread

a = socket(AF_INET, SOCK_STREAM)
a.bind(("",8080))
a.listen(5)
sockets=[]
ips={}
M=True
LOCK=_thread.allocate_lock()

def listener():
    while M:
        socket, ip = a.accept()
        print ("Received a connection from ",ip[0])
        LOCK.acquire()
        sockets.append(socket)
        ips[socket] = ip[0]
        LOCK.release()

def receiver():
    while M:
        tmp=sockets
        for socket in tmp:
            try:
                msg = socket.recv(1024)
                print (msg,)
                if not msg:
                    LOCK.acquire()
                    sockets.remove(socket)
                    LOCK.release()
                    continue
            except:
                continue
def list():
    tmp=ips
    for a in ips:
        print(,ips[a],)

def shutdown():
    answer = input("Sure? [y/n] ")
    if answer != "y":
        return
    M = False
    a.close()
    

def shell():		
    while M:
        cmd = input()
        if cmd == "shutdown":
            shutdown()
        elif cmd == "list":
            list()

_thread.start_new_thread(listener, ())
_thread.start_new_thread(receiver, ())
_thread.start_new_thread(shell, ())
while M:
    pass
print("Server Down")




