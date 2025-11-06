import queue
import socket
import select
import sys
#xử lý hàng đợi 
class Qu:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
#khỏi tạo server và xử lý tham số 
def usage():
    print('USAGE: python server.py <ADDRESS> <PORT> <MAXQUEUE> <BUFFERSIZE>')
    exit(0)

address = '127.0.0.1'

if len(sys.argv) > 1:
    if sys.argv[1].lower() in ('-h', '--help'):
        usage()
    else:
        address = sys.argv[1]
else:
    usage()

maxQueue = 2
bufferSize = 1024

if len(sys.argv) > 2:
    if sys.argv[2].isdigit():
        port = int(sys.argv[2])
        if port < 1000 or port > 65535:
            usage()
else:
    usage()

if len(sys.argv) > 3:
    if sys.argv[3].isdigit():
        maxQueue = int(sys.argv[3])
        if maxQueue < 1 or maxQueue > 999:
            usage()

if len(sys.argv) > 4:
    if sys.argv[4].isdigit():
        bufferSize = int(sys.argv[4])
        if bufferSize < 32 or bufferSize > 99999:
            usage()
#Quản lý phòng và kết nối client
roomCount = 0
cQ = Qu()
clientQueue = {}

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((address, port))
serverSocket.listen(5)

inputs = [serverSocket]
output = []
messageQueue = {}

startGame = False
playerOne = ''
playerTwo = ''
winner = -1
wait = None
#xử lý vòng lặp chính
while inputs:
    inputfd, outputfd, exceptfd = select.select(inputs, output, inputs)

    for fd in inputfd:
        if fd is serverSocket:
            clientConnection, clientAddress = fd.accept()

            if roomCount < maxQueue:
                status = 'ready'
                inputs.append(clientConnection)

                messageQueue[clientConnection] = queue.Queue()
                messageQueue[clientConnection].put(status + str(roomCount))
                output.append(clientConnection)

                roomCount += 1

                if roomCount == maxQueue:
                    startGame = True

            else:
                status = 'queue'
                clientQueue[clientConnection] = queue.Queue()
                cQ.enqueue(clientConnection)
                messageQueue[clientConnection] = queue.Queue()
                messageQueue[clientConnection].put(status)
                output.append(clientConnection)
#logi trò chơi 
        else:
            data = fd.recv(bufferSize).decode()

            if data:

                if startGame:
                    if '1' in data:
                        playerOne = data[:1]
                        if wait is None:
                            wait = fd
                    else:
                        playerTwo = data[:1]
                        if wait is None:
                            wait = fd

                    if playerOne and playerTwo:
                        if playerOne == 'R' and playerTwo == 'R': winner = 0
                        elif playerOne == 'R' and playerTwo == 'P': winner = 2
                        elif playerOne == 'R' and playerTwo == 'S': winner = 1
                        elif playerOne == 'P' and playerTwo == 'R': winner = 1
                        elif playerOne == 'P' and playerTwo == 'P': winner = 0
                        elif playerOne == 'P' and playerTwo == 'S': winner = 2
                        elif playerOne == 'S' and playerTwo == 'R': winner = 2
                        elif playerOne == 'S' and playerTwo == 'P': winner = 1
                        elif playerOne == 'S' and playerTwo == 'S': winner = 0
                    else:
                        messageQueue[fd].put('wait')
                        if fd not in output:
                            output.append(fd)
                else:
                    messageQueue[fd].put('wait')
                    if fd not in output:
                        output.append(fd)

                    if '1' in data:
                        playerOne = data[:1]
                        if wait is None:
                            wait = fd
                    else:
                        playerTwo = data[:1]
                        if wait is None:
                            wait = fd

                if winner != -1:
                    messageQueue[fd].put(winner)
                    if fd not in output:
                        output.append(fd)

                    wait.send(str(winner).encode())

                    wait = None
                    startGame = False
                    playerOne = ''
                    playerTwo = ''
                    winner = -1
                    roomCount = 2

                else:
                    print('Server received a message. Adding to messageQueue')
                    messageQueue[fd].put(data)

                    if fd not in output:
                        output.append(fd)
            else:
                print('A client has disconnected. Cleaning output list and messageQueue')

                if fd in output:
                    output.remove(fd)

                inputs.remove(fd)
                del messageQueue[fd]

                fd.close()

                roomCount -= 1
                try:
                    if cQ.size() >= 1:
                        nextClient = cQ.dequeue()

                        inputs.append(nextClient)
                        status = 'ready'
                        messageQueue[nextClient] = queue.Queue()
                        messageQueue[nextClient].put(status)
                        output.append(nextClient)

                        roomCount += 1
                except Exception:
                    pass

    for fd in outputfd:
        try:
            if roomCount > 0:
                message = messageQueue[fd].get_nowait()
                fd.send(str(message).encode())
        except queue.Empty:
            output.remove(fd)

    for fd in exceptfd:
        inputs.remove(fd)
        del messageQueue[fd]

        if fd in output:
            output.remove(fd)

        fd.close()

serverSocket.close()
