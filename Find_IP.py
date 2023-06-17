
import socket

def myip():
    """ Display  your system IP"""
    
    hostname=socket.gethostname()
    IPAddr=socket.gethostbyname(hostname)
    return IPAddr

myip()