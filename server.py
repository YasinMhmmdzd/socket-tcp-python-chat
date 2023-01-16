from socket import *
from colorama import Fore
server = socket(AF_INET , SOCK_STREAM)
ip = input("Input your ip : ")
port = input("input your port : ")
user_name = input("Input your username : ").encode()
server.bind((ip , int(port)))
server.listen(1)
print(Fore.GREEN + 'server running on port 1010')
client , addr = server.accept()
print(Fore.BLUE + "connected to " + str(addr))
client.send(user_name)
c_name = client.recv(1024)
print(Fore.YELLOW + str(c_name) + Fore.GREEN + " online")
print("")
while True:
    print("")
    pm = input(Fore.BLUE + ">>>")
    client.send(pm.encode())
    rec_msg = client.recv(1024)
    rec_msg = str(rec_msg)
    print(Fore.YELLOW + rec_msg)

client.close()
