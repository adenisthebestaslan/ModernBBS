import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from downloaduploadfile import download_file
from downloaduploadfile import uploadfile

import psycopg2
import hostsetup
from hostsetup import login
def downloadnupdate():
        conn = login(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml")
        cur = conn.cursor()

        cur.execute(f"""
        SELECT filename FROM uploaded_files
        ORDER BY  id ASC;
        """)
        rows = cur.fetchall()
        print(rows)
        
        for item in rows:
            textbox.insert(tk.END, f"Downloaded: {item}\n")
        file = MessageChatroom.get()
        download_file(file, r"C:\Users\adena\OneDrive\Desktop\Python Projects\userdownloads")



app = ttk.Window(themename="superhero")

textbox = tk.Text(app, height=10, width=30, font=('Helvetica', 12))
textbox.place(x=800, y=400)
# button = ttk.Button(app, text="download", bootstyle=PRIMARY, command=lambda: download_file("Screenshot 2025-06-13 132953.png", r"ModernBBS\hostsetup\hostsetup"))
button = ttk.Button(app, text="download", bootstyle=PRIMARY, command=lambda: downloadnupdate())

button.place(x=800, y=650)

button = ttk.Button(app, text="upload", bootstyle=PRIMARY, command=lambda: uploadfile())
button.place(x=800, y=700)

MessageChatroom = ttk.Entry(app)
MessageChatroom.place(x=800, y=740)
# button.pack(pady=20)
app.mainloop()
