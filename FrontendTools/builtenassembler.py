import tkinter as tk
import ttkbootstrap
from ttkbootstrap import ttk
from creation import ChatinfoBBS
import xml.etree.ElementTree as ET
from submitmessage import Submitchatroom
from tkinter import PhotoImage
from PIL import Image, ImageTk

root = ttkbootstrap.Window(themename="superhero")

def createchatroom(name,filepath,configpath):
    tree = ET.parse(filepath)
    # parse our file
    xml_root = tree.getroot()
    #get our root
    for chatroom in xml_root.findall('chatrooms/chatroom'):
        #for each chatroom in the chatrooms
       x_elem = chatroom.find('xpos')
       print(f"{x_elem},x")
       y_elem = chatroom.find('ypos')
       print(f"{y_elem},x")
       xpos = int(x_elem.text) if x_elem is not None and x_elem.text is not None else 0
       ypos = int(y_elem.text) if y_elem is not None and y_elem.text is not None else 0
       print(f"Creating chatroom at position ({xpos}, {ypos})")
       name = chatroom.find('name').text
       ChatinfoBBS(filepath,name)
       messages = ChatinfoBBS(configpath,name)
       print(messages)
       textbox = tk.Text(root, height=10, width=30, font=('Helvetica', 12))
       textbox.place(x=xpos, y=ypos)
       def update_messages():
           textbox.delete("1.0", "end")
           new_messages = ChatinfoBBS(configpath, name)
           print(f"Updating messages for {name}: {new_messages}")
           for item in new_messages:
             textbox.insert("end", f"{item} \n")
           root.after(2000, update_messages)  # update every 2 seconds

       NameChatroom = ttk.Entry(root)
       NameChatroom.insert(0, 'name')
       NameChatroom.place(x=xpos, y=ypos-100)
       MessageChatroom = ttk.Entry(root)
       MessageChatroom.insert(0, '...')
       MessageChatroom.place(x=xpos, y=ypos-120)
    submit_button = ttk.Button(root, text='Submit', command=lambda: [Submitchatroom(NameChatroom.get(), MessageChatroom.get(), configpath, name), update_messages()])  
    submit_button.place(x=xpos, y=int(ypos)-30)
        
def createimages(filepath):
    tree = ET.parse(filepath)
    xml_root = tree.getroot()
    for image in xml_root.findall('images/image'):
        print(image)
        
        x_elem = image.find('xpos')
        print(f"{x_elem},x")
        y_elem = image.find('ypos')
        path = image.find('path').text
        img = Image.open(path)
        photo = ImageTk.PhotoImage(img)
        
        label = ttk.Label(root, image=photo)
        label.image = photo
        label.grid(row=0, column=1, padx=20, pady=20)





root.mainloop()
