from django.dispatch import receiver
from vidstream import *
import tkinter as tk
import socket
import threading
import requests

local_ip_address = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

def start_listenting():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
    
    
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()
    
    
def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'), 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()
    
    
def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0, 'end-1c'), 6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()
    
# Gui

window = tk.Tk()
window.title("NeuralNine Call v0.0.1 Alpha")
window.geometry('300x200')

label_target_ip = tk.Lable(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen =  tk.Button(window, text="Start Listeing", width=50, command=start_listenting)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera =  tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen =  tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio =  tk.Button(window, text="Start Audio Streem", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()




#if __name__ == '__main__':
 #   run()