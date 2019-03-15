import socket
from tkinter.filedialog import askopenfilename

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establishing TCP connection
host_IP = str(socket.gethostbyname(socket.gethostname()))
s.bind((host_IP, 1234))
s.listen(5)  # connection queue
