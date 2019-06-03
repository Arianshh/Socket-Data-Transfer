import socket
from pathlib import Path

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
s.connect(('192.168.1.100', 1234))
=======
s.connect(('', 1234))
>>>>>>> parent of fd2fa14... Add progressive bar to server
ext = ''
ext_data = True

with open('Received_Files/received_file', 'wb') as received_data:
    print('Receiving data...')
    while True:
        if ext_data:
            ext = s.recv(4)
            ext = ext.decode('utf-8')
            if ext[0] == '.':
                ext = ext[1:]
            print(f"File Ext : {ext} extracted.")
            ext_data = False
        data = s.recv(1024)
        if not data:
            break
        received_data.write(data)

    received_data.close()
    p = Path('Received_Files/received_file')
    p.rename(p.with_suffix('.' + ext))

    s.close()
