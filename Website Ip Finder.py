import socket
import pyfiglet
banner = pyfiglet.figlet_format("Website Ip Finder")
print(banner)
# Enter your Target Name or instead of Ip Address
targett = input("Enter your Target: ")
a=socket.gethostbyname(targett)
print(a)