from socket import *
import random

# 准备好要发送的数据, ‘\0’，为结束
messages = ['Modern',
            'Chinese',
            'trace',
            'their',
            'origins',
            'to',
            'a',
            'cradle',
            'of',
            'civilization',
            'in',
            'the',
            'fertile',
            'basin',
            'of',
            'the',
            'Yellow',
            'River',
            'in',
            'the',
            'North',
            'China',
            'Plain',
            '\0']

def send_with_length(clientSocket, mes: []):
    length = len(mes)
    length_bytes = length.to_bytes(4, byteorder='big')
    clientSocket.sendall(length_bytes + mes)

if __name__ == '__main__':
    # 服务器的IP地址或主机名
    serverName = '127.0.0.1'
    # 服务器端口号
    serverPort = 12000
    # 创建客户套接字，使用IPv4协议，TCP协议
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # 三次握手，建立TCP连接
    clientSocket.connect((serverName, serverPort))
    # 设置mes编号
    mes_idx = 1
    for mes in messages:
        # 输出发送的消息
        print('client sent mes{}: {}'.format(mes_idx, mes))
        # 发送mes
        send_with_length(clientSocket, mes.encode('UTF-8'))
        # 消息标号加一
        mes_idx += 1
    # 关闭socket
    clientSocket.close()
