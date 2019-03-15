import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.7', 1234))

with open('received_file', 'wb') as received_data:
    while True:
        print('Receiving data...')
        data = s.recv(1024)
        if not data:
            break
        received_data.write(data)
    received_data.close()
    s.close()
