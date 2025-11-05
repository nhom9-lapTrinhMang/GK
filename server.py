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
