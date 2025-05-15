from socket import *

if __name__ == '__main__':
    # 服务器的IP地址或主机名
    serverName = '127.0.0.1'
    # 服务器端口号
    serverPort = 12000
    # 创建客户套接字，使用IPv4协议，TCP协议
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # 三次握手，建立TCP连接
    clientSocket.connect((serverName, serverPort))
    # 输入任意字符串
    sentence = input('Input uppercase sentence:')
    # 发送任意字符串
    clientSocket.send(sentence.encode())
    # 接受任意字符串
    modifiedSentence = clientSocket.recv(2048)
    # 输入结果
    print('From Server: ', modifiedSentence.decode())
    # 关闭socket
    clientSocket.close()

