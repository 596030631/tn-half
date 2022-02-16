import json
import time
from tkinter import *

from client_connect import ConnectExample


def message_arrived(msg):
    print("BBB >>> " + msg)
    bean = json.loads(msg)
    for info in bean['body']:
        text_msg_content_list.insert(
            END,
            f'{bean["sourceId"]}:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}\n{info}\n',
            'green')


conn = ConnectExample(message_arrived)
conn.start_connect()

root = Tk()
root.title("聊天室")

# 聊天框
frame_chat_content = Frame(width=400, height=300, bg='white')
frame_chat_content.grid(row=0, column=0, padx=2, pady=5)
frame_chat_content.grid_propagate(0)
text_msg_content_list = Text(frame_chat_content)
text_msg_content_list.tag_config('green', foreground='#008b00')

# 输入框
frame_chat_input = Frame(width=400, height=100, bg='white')
frame_chat_input.grid(row=1, column=0, padx=2, pady=5)
frame_chat_input.grid_propagate(0)
text_msg_input = Text(frame_chat_input)
text_msg_input.grid()
text_msg_content_list.grid()

# 底部留白
frame_chat_bottom = Frame(width=400, height=30, bg='white')
frame_chat_bottom.grid(row=2, column=0, padx=2, pady=5)
frame_chat_bottom.grid_propagate(0)

# 右部好友
frame_right = Frame(width=200, height=460, bg='white')
frame_right.grid(row=0, column=1, rowspan=3, padx=2, pady=5)


# 发送按钮
def send_message():
    msg_send = text_msg_input.get("0.0", END)
    text_msg_content_list.insert(END,
                                 f'me:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}\n{msg_send}\n',
                                 'green')
    conn.send_message(
        str(msg_send).strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').strip()
        )
    text_msg_input.delete('0.0', END)


button_send_msg = Button(frame_chat_bottom, text="发送", command=send_message)
button_send_msg.grid()

root.mainloop()
