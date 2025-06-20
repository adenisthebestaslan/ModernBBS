import hostsetup
from hostsetup import login
import psycopg2
from tkinter import filedialog, messagebox
import os


def uploadfile():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()

        filename = file_path.split("/")[-1]
        conn = login(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS uploaded_files (
                id SERIAL PRIMARY KEY,
                filename TEXT,
                file_data BYTEA
            );
        """)
        cur.execute("INSERT INTO uploaded_files (filename, file_data) VALUES (%s, %s)",
                        (filename, psycopg2.Binary(file_data)))
        conn.commit()

        cur.close()
        conn.close()

        messagebox.showinfo("Success", f"Uploaded: {filename}")
    except Exception as e:
        print(f'Error: {e}')

def download_file(filename, output_dir):
    conn = login(r"C:\Users\adena\OneDrive\Desktop\Python Projects\ModernBBS\hostsetup\configfile.xml")
    cur = conn.cursor()
    cur.execute("SELECT filename, file_data FROM uploaded_files WHERE filename = %s", (filename,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        filename, file_data = row

        # Make sure path is valid
        os.makedirs(output_dir, exist_ok=True)
        full_path = os.path.join(output_dir, filename)
        print("file data", file_data)
        with open(full_path, 'wb') as f:
            f.write(file_data)

        print("Downloaded:", full_path)
    else:
        print("File not found.")

if __name__ == "__main__":
    # Get absolute path of 'hostsetup' directory
    base_dir = os.path.dirname(__file__)  # script's directory
    output_path = os.path.join(base_dir, "hostsetup")
    download_file(r"Screenshot 2025-06-13 132953.png", output_path)
