#!/usr/bin/env python
#usage: python2.7 hostname_json.py

# Python Program to Get IP Address
import socket
import json

json_list = []
client_panel = {}
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
#print("Your Computer Name is:" + hostname)
#print("Your Computer IP Address is:" + IPAddr)
client_panel.update({'Hostname': hostname, 'IPaddress': IPAddr})
json_list.append(client_panel)
print(json.dumps(json_list, indent=3))
