import _thread
import json
import socket
import time

MESSAGE_EXIST = 1

user_id = "bzp"
user_id_dst = "sj"
# ip = "inlets.fun"
ip = "192.168.31.76"


def heart():
    ip_port = (ip, 9999)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.settimeout(10)

    publish = {'user_id': user_id}
    while True:
        time.sleep(0.5)
        server.sendto(user_id.encode("utf-8"), ip_port)
        info = server.recvfrom(4096)
        if len(info[0]) == 1:
            if info[0][0] == MESSAGE_EXIST:
                _client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                _client.connect((ip, 8889))
                j = json.dumps(publish)
                _client.send(j.encode('utf-8'))
                msg = _client.recvfrom(4096)
                msg = msg[0].decode('utf-8')
                print(msg)
                _client.close()
        else:
            print("udp read empty")


_thread.start_new_thread(heart, ())

print("input")

sender = {'sender': user_id, 'receiver': user_id_dst,
          'body': ['message2']}

while True:
    msg = input()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 8888))
    sender['body'][0] = msg
    j = json.dumps(sender)
    client.send(j.encode('utf-8'))
    client.close()
