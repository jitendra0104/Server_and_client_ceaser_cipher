import socket
import ceaser_cipher

def client_program():
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    num = 10

    message = input("Enter the message: ")

    while message.lower().strip() != 'bye':
        encrypted_text = ceaser_cipher.encryption_ceaser_cipher(message, num)
        client_socket.send(encrypted_text.encode())

        data = client_socket.recv(1024).decode()
        decrypted_data = ceaser_cipher.decryption_ceaser_cipher(data, num)
        print("Server:", decrypted_data)

        message = input("Enter the message: ")

    client_socket.close()

client_program()
