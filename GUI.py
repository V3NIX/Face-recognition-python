import tkinter as tk
from PIL import Image, ImageTk
rom tkinter import font
import subprocess
from tkinter import filedialog

def real_time():
    subprocess.Popen(["python", "./real_time.py"])

def image():
    subprocess.Popen(["python", "./img_rec.py"])


class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("250x400")
        self.configure(background="#f0f0f0")
        self.title("Face-APP")
        icon_image = Image.open("./source/icon.png")
        self.iconphoto(False, ImageTk.PhotoImage(icon_image))

        # Add the image from the provided code
        load = Image.open("./source/homepagepic.png")
        load = load.resize((350, 350), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.pack()

        # Add the buttons from the provided code
        button1 = tk.Button(self, text="Real-Time", fg="#ffffff", bg="#263942",width=20, height=3, command=real_time)
        button1.pack(pady=10)
        button2 = tk.Button(self, text="Browse Image", fg="#ffffff", bg="#263942",width=20, height=3, command=image)
        button2.pack(pady=10)
        button3 = tk.Button(self, text="Quit", fg="#263942", bg="#ffffff",width=20, height=3, command=self.quit)
        button3.pack(pady=10)


        # Set the window size and position
        window_width = 350
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
