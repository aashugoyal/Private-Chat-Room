import socket
import tkinter
import threading
host=input("Enter host: ")
port=input("Enter port: ")
if not port:
    port=33000
else:
    port=int(port)
buff=1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
def receive():
    while True:
        try:
            msg=s.recv(buff).decode("utf-8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break
def send(event=None):
    msg =my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf-8"))
    if msg== "{quit}":
        s.close()
        top.quit()
def close():
    s.close()
    top.quit()
    exit()
top=tkinter.Tk()
top.title("Private Chat Room")
msg_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("Type your name here")
scrollbar=tkinter.Scrollbar(msg_frame)
msg_list=tkinter.Listbox(msg_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill = tkinter.BOTH)
msg_list.pack()
msg_frame.pack()
entry_field=tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button= tkinter.Button(top, text="Send", command=send)
quit_button=tkinter.Button(top, text="QUIT",fg="Black", bg="Red", command=close)
send_button.pack()
quit_button.pack()
receive_thread=threading.Thread(target=receive)
receive_thread.start()
tkinter.mainloop()