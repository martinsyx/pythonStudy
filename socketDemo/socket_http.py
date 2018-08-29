import socket
form urllib.parse import urlparse

def fer_url(url):
    通过socket请求http
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path =="":
        path ="/"
    client - socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,80))
    client.send("GET {}\r\nHost:{}\r\nConnection:close".format(path,host).encode("utf8"))
    data= b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8")
    print(data)
    client.close
if __name__ == "__main__":
    get_url("http://www.baidu.com")
    # client.recv(1024)