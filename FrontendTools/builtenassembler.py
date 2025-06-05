import tkinter as tk
import ttkbootstrap
from ttkbootstrap import ttk
from creation import ChatinfoBBS
import xml.etree.ElementTree as ET
from submitmessage import Submitchatroom
from tkinter import PhotoImage
from tkinter import font
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
       messages = ChatinfoBBS(name,configpath)
       print(messages)
       textbox = tk.Text(root, height=10, width=30, font=('Helvetica', 12))
       textbox.place(x=xpos, y=ypos)
       def update_messages():
           textbox.delete("1.0", "end")
           new_messages = ChatinfoBBS(name, configpath)
           print(f"Updating messages for {name}: {new_messages}")
           bold_font = font.Font(textbox, textbox.cget("font"))
           bold_font.configure(weight="bold")
           textbox.tag_configure("(--)", font=bold_font)

           
           for item in new_messages:
                item_str = str(item) if not isinstance(item, str) else item
                if "*" in item_str:
                    newlist = item_str.split('*', 1)
                    print(f"newlist: {newlist}")
                    Partone = newlist[0]
                    Parttwo = newlist[1] if len(newlist) > 1 else ""
                    textbox.insert("end", f"{Partone}", ("(--)",))
                    textbox.insert("end", f"{Parttwo} \n")
 
 
               
                else:
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

def backgrounds(filepath):
    tree = ET.parse(filepath)
    print("..")
    xml_root = tree.getroot()
    print("...")
    for item in xml_root.findall('backgrounds/item'):
        print("....")
        colour_elem = item.find('colour')
        print(".....")
        if colour_elem is not None and colour_elem.text:
            print("......")
            print(f"colour: {colour_elem.text}")
            root.configure(background=colour_elem.text)






createchatroom("messages",r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\chatrooms.xml",r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml")
backgrounds(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\chatrooms.xml")
root.mainloop()



