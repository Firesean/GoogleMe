#! Python 3.7
# Author : Sean Morgan
# Welcome to Google me! Where we cut the TIME in half to make ME
# Search what you need and I will create a tab for you on your search!

import webbrowser
from tkinter import *


class GoogleMe:

    def __init__(self):
        # Values
        self.fireIcon_path = r"FireIcon_32x32.ico"
        self.googleMe_path = r"GoogleMe.png"
        self.window_size = (1280, 600)  # Width , Height
        self.googleMe_size = (1280, 440)  # Width , Height

        # GUI
        self.root = Tk()
        self.root.title("Google Me")
        self.root.iconbitmap(self.fireIcon_path)
        self.root.geometry("{}x{}".format(*self.window_size))
        self.root.resizable(width=False, height=False)
        self.googleMe_img = PhotoImage(file=self.googleMe_path)
        self.googleMe_display = Canvas(self.root, width=self.googleMe_size[0], height=self.googleMe_size[1])
        self.googleMe_display.create_image(0, 100, anchor=NW, image=self.googleMe_img)
        self.googleMe_entry = Entry(self.root, font="TimesNewRoman 28", width=27)
        self.googleMe_submit = Button(self.root, command=lambda: self.search_google(), width=60, height=8, text="Search"
                                      , fg="brown4", relief=GROOVE)
        # Binds
        self.root.bind("<Return>", lambda event: self.search_google(event))

        # Main
        self.create_gui()
        self.root.mainloop()

    def create_gui(self):
        self.googleMe_display.place(x=self.window_size[0]/4, y=0)
        self.googleMe_entry.place(x=320, y=self.window_size[1]/1.8)
        self.googleMe_submit.place(x=400, y=self.window_size[1]/1.5)
        self.googleMe_entry.focus()

    def search_google(self, event=None):
        search_target = self.googleMe_entry.get()
        self.googleMe_entry.delete(0, END)
        webbrowser.open("https://www.google.com/search?q={}".format(search_target))


googleMe = GoogleMe()

