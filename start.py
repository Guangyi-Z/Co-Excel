#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import askopenfilename
import os
import thread

# self-contained modules
import server

class main_gui:

    def __init__(self):
        # main window
        self.root= Tk()
        self.root.title("Co-Excel")
        self.root.geometry("160x120")

        # button for choosing file
        self.button1= Button(self.root, text="Choose File", command=self.get_excel_file)
        # label for file info
        self.label1= Label(self.root, text="")
        # button for start
        self.button2= Button(self.root, text="Start", command=self.start_server)
        self.button3= Button(self.root, text="Stop", command=server.stop_server)

    def layout(self):
        self.button1.pack()
        self.label1.pack()
        self.button2.pack()
        self.button3.pack()

    def start_server(self):
        thread.start_new_thread (server.serve_not_forever, ())

    def file_chose(self):
        self.label1['text']= "File is set"

    def get_excel_file(self):
        filename = askopenfilename()

        fname_ori= './config/config.txt'
        fname_new='./config/config.txt.tmp'
        f= file(fname_ori, 'r+')
        fnew= file(fname_new, 'w')
        for line in f:
            if line.startswith('excel_file='):
                fnew.write('excel_file="' + filename + '"\n')
            else:
                fnew.write(line)
        f.close();
        fnew.close();

        os.remove(fname_ori)
        os.rename(fname_new, fname_ori)
        # notify the user that file is set
        self.file_chose()

    def start(self):
        # set up the gui layout
        self.layout()

        # open the main window
        self.root.mainloop()
        self.root.destroy()
        # stop the server
        server.stop_server()


if __name__ == '__main__':
    gui= main_gui()
    gui.start()

