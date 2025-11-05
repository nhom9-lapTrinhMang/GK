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