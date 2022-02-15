import _thread
import json
import socket
import time

from th_encryp import edcoder


class ConnectExample:
    MESSAGE_EXIST = 1
    user_id = "sj"
    user_id_dst = "bzp"
    # ip = "inlets.fun"
    ip = "127.0.0.1"

    def __init__(self):
        print('init')

    def heart(self):
        ip_port = (self.ip, 9999)
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.settimeout(10)

        publish = {'user_id': self.user_id}

        while True:
            time.sleep(0.5)
            server.sendto(self.user_id.encode("utf-8"), ip_port)
            info = server.recvfrom(4096)
            if len(info[0]) == 1:
                if info[0][0] == self.MESSAGE_EXIST:
                    _client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    _client.connect((self.ip, 8889))
                    j = json.dumps(publish)
                    j = j.encode('utf-8')
                    buffer = list(j)
                    edcoder(buffer, len(buffer))
                    _client.send(bytes(buffer))
                    msg = _client.recvfrom(4096)
                    msg = msg[0]
                    buffer = list(msg)
                    edcoder(buffer, len(buffer))
                    buffer = bytes(buffer)
                    buffer = buffer.decode('utf-8')
                    print(buffer)
                    _client.close()
            else:
                print("udp read empty")

    def sender(self):
        sender = {'sender': self.user_id, 'receiver': self.user_id_dst, 'body': ['message0']}
        while True:
            msg = input()
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.ip, 8888))
            sender['body'][0] = msg
            j = json.dumps(sender)
            buffer = j.encode('utf-8')
            buffer = list(buffer)
            edcoder(buffer, len(buffer))
            client.send(bytes(buffer))
            client.close()

    ''' 建立连接 '''
    def start_connect(self):
        _thread.start_new_thread(self.heart, ())
        _thread.start_new_thread(self.sender, ())

    ''' 发送消息 '''
    def send_message(self, msg_send):
        pass
