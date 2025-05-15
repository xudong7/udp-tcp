from socket import *

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    # 创建服务器套接字，使用IPv4协议，UDP协议
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定端口号和套接字
    serverSocket.bind(('', serverPort))
    # 可以设置超时时间
    # 提示信息
    print("The server is ready to receive")
    # 进程一直运行，等待分组到达

    while (True):
        # 接收报文
        message, clientAddress = serverSocket.recvfrom(2048)
        # 处理 将报文转换为大写
        modifiedMessage = message.decode().upper()
        print(f"Received message: {modifiedMessage} from {clientAddress}")
        # 发送报文
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    serverSocket.close()
    print("Server closed")