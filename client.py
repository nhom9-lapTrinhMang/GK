def getinput():
    options = ('R', 'P', 'S')
    while True:
        clientInput = input("Enter R, P, or S: ").upper()
        if clientInput in options:
            return clientInput

def usage():
    print('USAGE: python client.py <ADDRESS> <PORT> <BUFFERSIZE>')
    exit(0)

if len(sys.argv) > 1:
    if sys.argv[1].lower() in ('-h', '--help'):
        usage()
    else:
        if len(sys.argv) > 2:
            address = sys.argv[1]
            if sys.argv[2].isdigit():
                port = int(sys.argv[2])
                if port < 1000 or port > 65535:
                    usage()
        else:
            usage()

        if len(sys.argv) > 3:
            if sys.argv[3].isdigit():
                bufferSize = int(sys.argv[3])
                if bufferSize < 32 or bufferSize > 99999:
                    usage()
        else:
            bufferSize = 1024
else:
    usage()
#  Logic game client 
target = (address, port)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(target)

status = clientSocket.recv(bufferSize).decode()
player = '-1'

if '0' in status:
    player = '1'
elif '1' in status:
    player = '2'

print(status)

if 'queue' in status:
    while status == 'queue':
        print('The room is full, you have been added to the queue.')
        status = clientSocket.recv(bufferSize).decode()
    print(status)
    print('You are now connected!')

isPlaying = True

while isPlaying:
    clientInput = getinput()

    if clientInput:
        clientSocket.send((clientInput + str(player)).encode())
        result = clientSocket.recv(bufferSize).decode()

        if 'wait' in result:
            print('Waiting for your opponent!')
            result = clientSocket.recv(bufferSize).decode()
            result = clientSocket.recv(bufferSize).decode()

        if '0' in result:
            print('The match was a draw!')
        elif '1' in result and player == '1':
            print('You won!')
        elif '1' in result and player == '2':
            print('You lost!')
        elif '2' in result and player == '1':
            print('You lost!')
        elif '2' in result and player == '2':
            print('You Won!')

        print('Disconnecting to make room for other players. Thank you for playing SPEED-RPS!')

        clientSocket.close()
        isPlaying = False
