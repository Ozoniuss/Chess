import socket
import threading
from Domain.Pieces.EmptyPiece import EmptyPiece
from GUI.GUI_improved import GUI

CONFIRM_NICKNAME = 'geubfsjvnlevnselkvrn'
INVALID_NICKNAME = 'effsefesfaefsevsvssr'
CONFIRM_CONNECTION = 'egsfesfesfsefessg3g'
SECRET_MESSAGE = 'efjfiefsofesfew'

class Server:

    def __init__(self):
        self.__HOST = '127.0.0.1'
        self.__PORT = 55555
        self.__ADDR = (self.__HOST, self.__PORT)
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.__clients = {}
        self.__nicknames = set()

    def get_ADDR(self):
        return self.__ADDR

    def start_server(self):
        self.__server.bind(self.__ADDR)
        print('RUNNING ... ')
        self.__server.listen()

    @property
    def clients(self):
        return self.__clients


    def broadcast(self, message):
        for client in self.__clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(2048)
                if SECRET_MESSAGE in str(message.decode('utf-8')):
                    m = (message.decode('utf-8'))
                    m = m[len(SECRET_MESSAGE) + 1:]
                    parts = m.split(',')
                    ix = parts[0]
                    iy = parts[1]
                    nx = parts[2]
                    ny = parts[3]
                    print(ix, iy, nx, ny)
                    for c in self.__clients:
                        if c != client:
                            print(self.__clients[c])
                            c.send((SECRET_MESSAGE + m).encode('utf-8'))
                else:
                    self.broadcast(message)

            except:
                name = self.__clients[client]
                self.__clients.pop(client, None)
                client.close()
                self.broadcast(f"[{name}] has disconnected.".encode('utf-8'))
                break

    def recieve(self):
        while True:
            client, address = self.__server.accept()
            print(f'Connected with address: {str(address)} ')

            client.send(CONFIRM_NICKNAME.encode('utf-8')) # keyword
            nickname = client.recv(2048).decode('utf-8')
            while nickname in self.__nicknames:
                client.send(INVALID_NICKNAME.encode('utf-8'))  # keyword
                nickname = client.recv(2048).decode('utf-8')
            self.__clients[client] = nickname
            self.__nicknames.add(nickname)

            print(f"Nickname of the client is [{nickname}]")
            self.broadcast(f"[{nickname}] has connected.".encode('utf-8'))
            client.send(CONFIRM_CONNECTION.encode('utf-8'))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

class Client():


    def __init__(self, server: Server):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__nickname = None
        self.__server = server

        # TESTING PURPOSES ONLY
        self.table = None
        self.root = None
        self.interface = None

        self.a = 2

    @property
    def get_address(self):
        return (self.__server.get_ADDR())

    def get_server(self):
        return self.__server

    def send(self, message):
        self.__client.send(message.encode('utf-8'))

    @property
    def nickname(self):
        return self.__nickname

    def initialize_game_params(self, table, root):
        self.table = table
        self.root = root
        self.interface = GUI(self.table, self.root, self)

    def connect_to_server(self):
        self.__nickname = input('Choose a nickname >>> ')
        self.__client.connect(self.get_address)

    def receive(self):
        while True:
            try:
                message = self.__client.recv(2048).decode('utf-8')
                if message == CONFIRM_NICKNAME:
                    self.__client.send(self.__nickname.encode('utf-8'))
                elif message == INVALID_NICKNAME:
                    self.__nickname = input('Choose a different nickname dumbass >>> ')
                    self.__client.send(self.__nickname.encode('utf-8'))
                elif message == CONFIRM_CONNECTION:
                    pass

                elif SECRET_MESSAGE in message:
                    print('Has moved. Move is ' + str(message))
                    m = message
                    m = m[len(SECRET_MESSAGE):]
                    parts = m.split(',')
                    print(parts)
                    print(f'{parts[0]}-{parts[1]}-{parts[2]}-{parts[3]}')
                    ix = int(parts[0])
                    iy = int(parts[1])
                    nx = int(parts[2])
                    ny = int(parts[3])
                    print('oh ye finally')
                    self.interface.table.move_piece(ix, iy, nx, ny)
                    self.interface.update()


                else:
                    print(message)
            except Exception as e:
                print("An error occured. Disconnected.")
                print(str(e))
                break

    def chat(self):
        while True:
            try:
                msg = f'{self.__nickname}: {input("")}'
                self.__client.send(msg.encode('utf-8'))
            except Exception as e:
                print(str(e))
                break

    def start_receive_thread(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def start_chat_thread(self):
        chat_thread = threading.Thread(target=self.chat)
        chat_thread.start()

    def run_game(self):
        self.interface.run_game()
        self.root.mainloop()