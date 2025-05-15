from socket import *

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口号和套接字
    serverSocket.bind(('', serverPort))
    # 可以设置超时时间
    # 开启监听
    serverSocket.listen(1)
    print('The server is ready to receive')
    while (True):
        # 等待接受客户端的连接
        connectionSocket, addr = serverSocket.accept()
        print(f"Connected to {addr}")
        # 接受客户端的数据
        sentence = connectionSocket.recv(2048)
        print(f"Received message: {sentence.decode()} from {addr}")
        # 数据处理 转换为小写
        capitalizedSentence = sentence.decode().lower()
        # 把结果发送回客户端
        connectionSocket.send(capitalizedSentence.encode())
        # 连接关闭
        connectionSocket.close()
    serverSocket.close()
    print("Server closed")
