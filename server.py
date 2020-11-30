import socket, sys

def main():
    number_players = 1
    number_stages = 1
    ip = '127.0.0.1'
    port = 8080
    name = []

    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:s:i:r:n:", ["players=", "stages=", "ip=", "port=", "name="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-p', '--players'):
            number_players = arg
        elif opt in ('-s', '--stages'):
            number_stages = arg
        elif opt in ('--ip'):
            ip = arg
        elif opt in ('--port'):
            port = arg
        elif opt in ('--name'):
            name = arg
        else:
            sys.exit(2)

    print('number players: {}'.format(number_players))
    print('number stages: {}'.format(number_stages))
    print('ip : {}'.format(ip))
    print('port: {}'.format(port))
    print('name: {}'.format(name))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 8080))
server_socket.listen(20)

while True:
    (clientsocket, address) = server_socket.accept()
    print("Server started at ", address)
    message = clientsocket.recv(1024)

    clientsocket.close()
    clientsocket.close()

main()