import sys
sys.path.insert(0, r"/mnt/c/Users/Ozoniuss/Desktop/chess2/Chess/")

from Networking.network import *

import socket
from _thread import *
import pickle
from game import Game
n = Server()
if __name__ == "__main__":
    n.start_server()
    n.recieve()

# import socket
# import threading
#
# HEADER = 64
# PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER, PORT)
# FORMAT = 'utf-8'
# DISCONNECT_MESSAGE = "!DISCONNECT"
#
# SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)
#
#
# def handle_client(conn, addr):
#     print(f"[NEW CONNECTION] {addr} connected.")
#
#     connected = True
#     while connected:
#         try:
#             msg_length = conn.recv(HEADER).decode(FORMAT)
#             if msg_length:
#                 msg_length = int(msg_length)
#                 msg = conn.recv(msg_length).decode(FORMAT)
#                 if msg == DISCONNECT_MESSAGE:
#                     connected = False
#
#                     print(f"[{addr}] {msg}")
#                     conn.send("Msg received".encode(FORMAT))
#         except:
#             conn.close()
#             print(f"[{addr}] has left")
#
#     conn.close()
#
#
# def start():
#     server.listen()
#     print(f"[LISTENING] Server is listening on {SERVER}")
#     while True:
#         conn, addr = server.accept()
#         thread = threading.Thread(target=handle_client, args=(conn, addr))
#         thread.start()
#         print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
#
#
# print("[STARTING] server is starting...")
# start()



# server = '192.168.0.103' # local network
# port = 5555 # generally not used
#
# # set up a socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # AF_INET type is used for connecting to ipv4 addreses
#
# try:
#     s.bind((server, port))
# except socket.error as e:
#     print(str(e))
#
# # opens up the port, arg -- how many clients can connect
# s.listen(2)
# print("Server started, waiting for clients ... ")
#
# def threaded_clinet(conn):
#     conn.send(str.encode("Connected."))
#     reply = ''
#
#     while True:
#         try:
#             data = conn.recv(2048) # arg is number of bits we are trying to receive
#             # try to increase the size if there are problems
#
#             reply = data.decode('utf-8')
#
#             if not data:
#                 print("Disconnected.")
#                 break
#
#             else:
#                 print('Received: ', reply)
#                 print('Sending:', reply)
#
#             conn.sendall(str.encode(reply))
#         except:
#             break
#
#     print('Lost connection')
#     conn.close()
#
# while True:
#     # look for connections
#     conn, addr = s.accept()
#     print('Connected to:', addr)
#
#     start_new_thread(threaded_clinet, (conn,))
#
