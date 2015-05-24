from socket import *

a = socket(AF_INET, SOCK_STREAM)
a.connect(("localhost",8080))

while True:
    msg=input("Message: ")
    a.sendall((msg).encode())






