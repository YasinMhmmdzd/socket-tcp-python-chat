from socket import *
from colorama import Fore
connection = socket(AF_INET , SOCK_STREAM)
ip = input("Input your ip : ")
port = input("input your port : ")
user_name = input("Input Your username : ").encode()
connection.connect((ip , int(port)))
print(Fore.GREEN + 'connected')
s_name = connection.recv(1024)
connection.send(user_name)
print(Fore.BLUE + str(s_name) + Fore.GREEN + " online")
print("")
while True:
    print("")
    data = connection.recv(1024)
    data = str(data)
    print(Fore.YELLOW + data.decode())
    pm = input(Fore.BLUE + ">>>")
    connection.send(pm.encode())

connection.close()
