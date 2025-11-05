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
