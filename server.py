import os
import socket
from tkinter.filedialog import askopenfilename

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establishing TCP connection
# host_IP = str(socket.gethostbyname(socket.gethostname()))
s.bind(('192.168.1.100', 1234))
s.listen(5)  # connection queue

while True:
    clientSock, clientAdd = s.accept()
    print(f"Connection to {clientAdd[0]} has been established.")

    # choose file to send.
    filepath = askopenfilename()
    filepath_split = filepath.split('.')
    file_ext = filepath_split[len(filepath_split)-1]

    if len(file_ext) == 3:
        file_ext = '.' + file_ext

    clientSock.send(str.encode(file_ext))

    data = open(filepath, 'rb')
    data_size = b = os.fstat(data.fileno()).st_size
    print(filepath.split('/')[len(filepath.split('/')) - 1] + ' is being sent.')
    print(f'file size : {data_size/1000000} MB')

    data_to_bytes = data.read(1024)
    bytes_transferred = bytes(0)

    load = 0

    while data_to_bytes:
        if load % 10000 == 0:
            print(int(load*1024/data_size*100), ' % done')

        clientSock.send(data_to_bytes)
        data_to_bytes = data.read(1024)
        load += 1
    data.close()

    print('file sent.')
    clientSock.close()
