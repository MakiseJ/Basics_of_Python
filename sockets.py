import socket

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("baidu.com", 80))
message=input("input: ")
s.send(message.encode())
receivem=s.recv(1024)
print(receivem.decode())

