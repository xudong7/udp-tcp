import socket
import random
from socket import *

# 先获取到头长度4字节，然后根据头长度获取到数据
def recv_with_length(connectionSocket):
    length_bytes = b''
    while len(length_bytes) < 4:
        chunk = connectionSocket.recv(4 - len(length_bytes))
        if not chunk:
            return None
        length_bytes += chunk
    
    mes_length = int.from_bytes(length_bytes, byteorder='big')
    
    mes = b''
    while len(mes) < mes_length:
        chunk = connectionSocket.recv(mes_length - len(mes))
        if not chunk:
            return None
        mes += chunk
    return mes

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 设置端口重用，以便服务能迅速重启
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定端口号和套接字
    serverSocket.bind(('', serverPort))
    # 开启监听
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        connectionSocket, addr = serverSocket.accept()
        # 设置mes编号
        mes_idx = 1
        # 不断处理客户端的请求
        while True:
            # 接受客户端的数据
            sentence_bytes = recv_with_length(connectionSocket)
            if sentence_bytes is None:
                print('Client disconnected')
                break
            
            # 将字节数据解码为字符串
            sentence = sentence_bytes.decode('utf-8')
            
            # 输出客户端发来的数据
            print('server get mes{}: {}'.format(mes_idx, sentence))
            # 若以\0为结束，则停止监听
            if sentence.endswith('\0'):
                print('server end listening from client')
                break
            mes_idx += 1
        # 连接关闭
        connectionSocket.close()
