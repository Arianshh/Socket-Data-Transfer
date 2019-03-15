import socket
from tkinter.filedialog import askopenfilename

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establishing TCP connection
# host_IP = str(socket.gethostbyname(socket.gethostname()))
s.bind(('192.168.1.7', 1234))
s.listen(5)  # connection queue

while True:
    clientSock, clientAdd = s.accept()
    print(f"Connection to {clientAdd[0]} has been established.")

    # choose file to send.
    filename = askopenfilename()
    print(filename + ' uploaded.')
    data = open(filename, 'rb')
    data_to_bytes = data.read(1024)
    while data_to_bytes:
        clientSock.send(data_to_bytes)
        data_to_bytes = data.read(1024)
    data.close()

    print('file sent.')
    clientSock.close()
