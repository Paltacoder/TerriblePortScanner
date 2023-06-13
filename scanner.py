#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    print("Invalid syntax: python3 scanner.py <IP>") #Translate to IPv4
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str)(datetime.now()))
print("-" * 50)

try:
    for port in range(20, 600):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)}
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {port} is open!")
            s.close()

except KeyboardInterrupt:
    print("\nExiting of this terrible program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()