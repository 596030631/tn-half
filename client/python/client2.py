# import _thread
# import json
# import socket
# import time
#
# from client import edcoder
#
# MESSAGE_EXIST = 1
#
# user_id = "bzp"
# user_id_dst = "sj"
#
# # ip = "inlets.fun"
#
# ip = "127.0.0.1"
#
# def heart():
#     ip_port = (ip, 9999)
#     server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     server.settimeout(10)
#
#     publish = {'user_id': user_id}
#
#     while True:
#         time.sleep(0.5)
#         server.sendto(user_id.encode("utf-8"), ip_port)
#         info = server.recvfrom(4096)
#         if len(info[0]) == 1:
#             if info[0][0] == MESSAGE_EXIST:
#                 _client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                 _client.connect((ip, 8889))
#                 j = json.dumps(publish)
#                 j = j.encode('utf-8')
#                 buffer = list(j)
#                 edcoder(buffer, len(buffer))
#                 _client.send(bytes(buffer))
#                 msg = _client.recvfrom(4096)
#                 msg = msg[0]
#                 buffer = list(msg)
#                 edcoder(buffer, len(buffer))
#                 buffer = bytes(buffer)
#                 buffer = buffer.decode('utf-8')
#                 print(buffer)
#                 _client.close()
#         else:
#             print("udp read empty")
#
#
# _thread.start_new_thread(heart, ())
#
# print("input")
# sender = {'sender': user_id, 'receiver': user_id_dst, 'body': ['message0']}
#
# while True:
#     msg = input()
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect((ip, 8888))
#     sender['body'][0] = msg
#     j = json.dumps(sender)
#     buffer = j.encode('utf-8')
#     buffer = list(buffer)
#     edcoder(buffer, len(buffer))
#     client.send(bytes(buffer))
#     client.close()