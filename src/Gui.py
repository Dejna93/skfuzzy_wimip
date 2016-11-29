# coding=UTF-8
import os
import Tkinter as tk


thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

LARGE_FONT = ("Verdana", 12)


class Gui(tk.Tk ):


    def __init__(self, *args,**kwargs):

        tk.Tk.__init__(self,*args, **kwargs)
        tk.Tk.wm_title(self,"Sterownik ogrzewania domu")

        container = tk.Frame(self)

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)


        self.frames  = {}

        for F in (StartPage, ControlPage):
            page_name = F.__name__
            frame = F(parent= container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0, sticky="NSEW")

        self.show_frame("StartPage")


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def quit(self):
        tk.Tk.destroy()

class StartPage(tk.Frame):

    def __init__(self,parent , controller):
        tk.Frame.__init__(self,parent)


class ControlPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


app = Gui()
app.minsize(width=400, height=400)
app.mainloop()



