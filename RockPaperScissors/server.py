#Cài đặt quản lý hàng đợi 
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
# === Common Imports ===
import queue
import socket
import select
import sys

# Base server file for Rock-Paper-Scissors project
# Logic will be implemented in feature branches

def main():
    pass  # TODO: Implement server logic in feature branches

if __name__ == "__main__":
    main()
#Xử lý vòng lặp chính (select & I/O) (feature/socket-event-loop)
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