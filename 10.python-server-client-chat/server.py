import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()

PORT = 5556

s.bind((HOST_NAME, PORT))

s.listen(4)
client, address = s.accept()
while True:
    message = input('Server:')
    client.send(bytes(message,'utf-8'))
    message_from_client = client.recv(50)
    print(message_from_client.decode('utf-8'))

