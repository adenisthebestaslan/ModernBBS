
import tkinter as tk
import ttkbootstrap
from ttkbootstrap import ttk
from creation import ChatinfoBBS
import xml.etree.ElementTree as ET
from submitmessage import Submitchatroom
from tkinter import PhotoImage
from tkinter import font
from PIL import Image, ImageTk
import settingsreader
import subprocess
# from hostsetup import downloaduploadfile
subprocess.Popen(['python', r'hostsetup\downloding.py'])
theme = settingsreader.readsettings(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\userconfig.xml")
print("read settings:".upper(), theme)
# lightmode 
root = ttkbootstrap.Window(themename=theme)

def createchatroom(name,filepath,configpath):
    tree = ET.parse(filepath)
    # parse our file
    xml_root = tree.getroot()
    #get our root
    for chatroom in xml_root.findall('chatrooms/chatroom'):
        #for each chatroom in the chatrooms
       x_elem = chatroom.find('xpos')
       #find the x element
       print(f"{x_elem},x")
       #print the x element
       y_elem = chatroom.find('ypos')
       # find the y positon
       print(f"{y_elem},x")
       #print the y posioton
       xpos = int(x_elem.text) if x_elem is not None and x_elem.text is not None else 0
       #x pos is not  a x_element and if x is existing and it is text. if not, it is 0
       ypos = int(y_elem.text) if y_elem is not None and y_elem.text is not None else 0
       #y pos is not  a y_element and if y is existing and it is text. if not, it is 0
       print(f"Creating chatroom at position ({xpos}, {ypos})")
       name = chatroom.find('name').text
       #x pos is not  a x_element and if x is existing and it is text. if not, it is 0
       messages = ChatinfoBBS(name,configpath)
       #logs in and grabs messages in a list, connecting with name of table and configfile path
       print(messages)
       # print messages
       textbox = tk.Text(root, height=10, width=30, font=('Helvetica', 12))
       #makes text
       
       textbox.place(x=xpos, y=ypos)
       #places the textbox at x and y
       def update_messages():
           textbox.delete("1.0", "end")
           new_messages = ChatinfoBBS(name, configpath)
           print(f"Updating messages for {name}: {new_messages}")
           bold_font = font.Font(textbox, textbox.cget("font"))
           bold_font.configure(weight="bold")
           textbox.tag_configure("(--)", font=bold_font)

           
           for item in new_messages:
                item_str = str(item) if not isinstance(item, str) else item
                #if its a string
                if "*" in item_str:
                    #if it contains a bold marker
                    newlist = item_str.split('*', 1)
                    #split it from a *
                    print(f"newlist: {newlist}")
                    # print our new list
                    Partone = newlist[0]
                    #part one is new list's 0
                    Parttwo = newlist[1] if len(newlist) > 1 else ""
                    #part two is newlist 1 IF its more than 1.
                    textbox.insert("end", f"{Partone}", ("(--)",))
                    #make part 1 bold
                    textbox.insert("end", f"{Parttwo} \n")
                    #put part 2
 
               
                else:
                    textbox.insert("end", f"{item} \n")
                    #insert it normally
           root.after(2000, update_messages)
           # update every 2 seconds

       NameChatroom = ttk.Entry(root)
       #create window
       NameChatroom.insert(0, 'name')
       #insert the chat room
       NameChatroom.place(x=xpos, y=ypos-100)
       #place it
       MessageChatroom = ttk.Entry(root)
       # make sure its here
       MessageChatroom.insert(0, '...')
       #put the 
       MessageChatroom.place(x=xpos, y=ypos-120)
    submit_button = ttk.Button(root, text='Submit', command=lambda: [Submitchatroom(NameChatroom.get(), MessageChatroom.get(), configpath, name), update_messages()])  
    submit_button.place(x=xpos, y=int(ypos)-30)
        
def createimages(filepath):
    tree = ET.parse(filepath)
    #tree is the xml page filepath
    xml_root = tree.getroot()
    # get our root
    for image in xml_root.findall('images/image'):
        #for image in images
        print(image)
        
        x_elem = image.find('xpos')
        print(f"{x_elem},x")
        y_elem = image.find('ypos')
        path = image.find('path').text
        #get x and y
        img = Image.open(path)
        # open the path
        photo = ImageTk.PhotoImage(img)
        #naje a unage
        
        label = ttk.Label(root, image=photo)
        #make  a label
        label.image = photo
        # add a image to the label
        label.grid(row=0, column=1, padx=20, pady=20)
        #add it to our grid and pad it our
def backgrounds(filepath):
    tree = ET.parse(filepath)
    # parse the filepath
    print("..")
    xml_root = tree.getroot()
    # get root
    print("...")
    for item in xml_root.findall('backgrounds/item'):
        #for item in Backgrounds
        print("....")
        colour_elem = item.find('colour')
        #find coulour
        print(".....")
        if colour_elem is not None and colour_elem.text:
            #if the element exists and its text
            print("......")
            print(f"colour: {colour_elem.text}")
            root.configure(background=colour_elem.text)
            #set coulour to chosen one
            






createchatroom("messages",r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\chatrooms.xml",r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml")
backgrounds(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\chatrooms.xml")
root.mainloop()


