import cv2
import socket
import time
from threading import Thread

HOST = 'localhost'
PORT = 9999


class ScreenShare():
    pass;


class ScreenPlay():
    pass;


def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass


def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        t = Thread(target=rcvMsg(), args=(sock,))
        t.daemon = True
        t.start()

        while True:
            time.sleep(0.5)
            msg = input(">>>")
            if msg == '/quit':
                sock.send(msg.encode())
                break

            sock.send(msg.encode())


runChat()
