import socket
import select
import sys

NUMBER_LENGTH = 3
IP = "127.0.0.1"
port = 5678
first = True

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((IP, port))

serverSocket.listen()

socketsAndUsers = [serverSocket]

clients = {}

def recieve_message(clientSocket):
    try:
        name = clientSocket.recv(NUMBER_LENGTH)

        if not len(name):
            return False
        messageLength = int(name.decode("utf-8").strip())
        return {"Input Number": name, "data": clientSocket.recv(messageLength)}
    except:
        return False

while True:
    readSockets, _, exceptionSockets = select.select(socketsAndUsers, [], socketsAndUsers)

    for notifiedSocket in readSockets:

        if notifiedSocket == serverSocket:
            clientSocket, clientAddress = serverSocket.accept()
            user = recieve_message(clientSocket)
            if user is False:
                continue
            socketsAndUsers.append(clientSocket)
            if len(clients) < 4:
                clients[clientSocket] = user
                newPlayer = f"player {user['data'].decode('utf-8')} is ready to play"
                print(newPlayer)
            else:
                print("Max players in game!")
        else:
            message = recieve_message((notifiedSocket))
            user = clients[notifiedSocket]
            #print(message['data'].decode('utf-8'))
            for clientSocket in clients:
                if clientSocket != notifiedSocket:
                    try:
                        clientSocket.send(message['data'])
                    except TypeError as er:
                        sys.exit(0)
    for notifiedSocket in exceptionSockets:
        socketsAndUsers.remove(notifiedSocket)
        del clients[notifiedSocket]
