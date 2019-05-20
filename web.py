import socketserver
import sqlfile
import webbrowser


# import socket.socket


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote".format(self.client_address[0]))
        datas = self.data.split(b'\r\n')
        value = ''
        for i in range(len(datas) - 1, -1, -1):
            if b'value' in datas[i]:
                value = str(datas[i], encoding='utf-8').split('=')[-1]
                print(value)
                break
        self.request.sendall(self.getResponse())
        self.request.sendall(bytes(str(sqlfile.select(value)), encoding='utf-8'))

    def getResponse(self):
        # 构造响应数据
        response_start_line = b'HTTP/1.1 200 OK\r\n'
        response_headers = b'Server: My server\r\n' \
                           b'access-control-allow-origin:*\r\n'
        # response_body = b'<h1>Python HTTP Test</h1>'
        return response_start_line + response_headers + b'\r\n'


if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 9000

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
