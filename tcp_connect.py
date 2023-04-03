from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import webbrowser
import path_identify

url = "https://y.qq.com/"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?')[0]  # 获取请求路径，去掉参数部分
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)  # 解析参数部分，获取请求参数
        # print(f"Received command: {path}, params: {params}")
        path_identify.path_switch(path) #判断html指令中的操作，并执行执行
        # path = ''
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    # print(f"Starting server on port {port}...")
    httpd.serve_forever()


run()

#http://192.168.1.100:8000/command?param1=value1&param2=value2
#该请求将向服务器发送一个 GET 请求，请求路径为 "/command"，请求参数为 "param1=value1" 和 "param2=value2"。在服务器接收到请求并处理完请求时，将在控制台上打印出接收到的指令和参数。