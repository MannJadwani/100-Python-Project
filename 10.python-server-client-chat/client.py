import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()

PORT = 5556

s.connect((HOST_NAME, PORT))

# msg = s.recv(10)
# print(msg)

while True:
    message = s.recv(50)
    print(message.decode('utf-8'))
    message_to_send = input('Client:')
    s.send(bytes(message_to_send,'utf-8'))

