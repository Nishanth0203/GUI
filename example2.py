#tcp client
import socket
if __name__=="__main__":
    ip="127.0.0.1"
    port=1234
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((ip,port))
    string=server.recv(1024)
    string=string.decode("utf-8")
    print(string)
    server.close()
