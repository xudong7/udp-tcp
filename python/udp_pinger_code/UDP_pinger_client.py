# UDPPingerClient.py
from socket import *
import time

if __name__ == '__main__':
    # server ip address
    serverName = '127.0.0.1'
    # server port
    serverPort = 12000
    # create udp socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # set timeout
    clientSocket.settimeout(5)
    # set ping count
    pingCount = 10
    
    sent = 0
    received = 0
    rtt_times = []
    
    print(f'Pinging {serverName} with 32 bytes of data:')
    for seq in range(1, pingCount + 1):
        sent += 1
        # set start time
        start_time = time.time()
        # create ping message
        pingMessage = f"ping sequence={seq}".ljust(32, '0')
        # send ping message
        clientSocket.sendto(pingMessage.encode('utf-8'), (serverName, serverPort))
        # receive pong message
        try:
            # receive pong message
            message, serverAddress = clientSocket.recvfrom(1024)
            received += 1
            rtt = (time.time() - start_time) * 1000 # ms
            rtt_times.append(rtt)
            print(f'Reply from {serverAddress[0]}: bytes={len(message)} time={rtt:.2f}ms')
        except timeout:
            print('Request timed out')
        pingCount -= 1
    
    print(f'\nPing statistics for {serverName}:')
    loss_percentage = 0 if sent == 0 else ((sent - received) / sent) * 100
    print(f'    Packets: Sent = {sent}, Received = {received}, Lost = {sent - received} ({loss_percentage:.0f}% loss),')
    
    if received > 0:
        min_time = min(rtt_times)
        max_time = max(rtt_times)
        avg_time = sum(rtt_times) / len(rtt_times)
        
        print('Approximate round trip times in milli-seconds:')
        print(f'    Minimum = {min_time:.0f}ms, Maximum = {max_time:.0f}ms, Average = {avg_time:.0f}ms')
    
    
    # close socket
    clientSocket.close()
