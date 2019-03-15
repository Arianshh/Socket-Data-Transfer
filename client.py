import socket
from pathlib import Path

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.7', 1234))
ext = ''
with open('received_file', 'wb') as received_data:
    while True:
        ext_data = True
        print('Receiving data...')
        while True:
            if ext_data:
                ext = s.recv(3)
                ext = ext.decode('utf-8')
                ext_data = False
            data = s.recv(1024)
            if not data:
                break
            received_data.write(data)

        received_data.close()
        p = Path('received_file')
        p.rename(p.with_suffix('.' + ext))

        s.close()
