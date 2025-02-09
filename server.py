import socket
import ceaser_cipher

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    num = 10
    print("Server is listening...")
    conn, address = server_socket.accept()
    print(f"Connection from {address}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        decrypted_data = ceaser_cipher.decryption_ceaser_cipher(data, num)
        print("Client:", decrypted_data)

        data = input('Enter the message: ')
        encrypted_data = ceaser_cipher.encryption_ceaser_cipher(data, num)
        conn.send(encrypted_data.encode())

    conn.close()

server_program()
