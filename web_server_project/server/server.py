import socket
import threading

class WebServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.routes = {}

    def add_route(self, path, handler):
        self.routes[path] = handler

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024).decode('utf-8')
        if not request_data:
            client_socket.close()
            return
            
        request_line = request_data.split('\n')[0]
        try:
            method, path, _ = request_line.split(' ')
        except ValueError:
            client_socket.close()
            return

        if path in self.routes:
            response_body = self.routes[path](request_data)
            response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
        else:
            response_body = "Not Found"
            response = f"HTTP/1.1 404 Not Found\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"

        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        
        while True:
            client, _ = server_socket.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()
