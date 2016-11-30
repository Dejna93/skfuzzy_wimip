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
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)


        self.frames  = {}

        for F in (StartPage, ControlPage):
            page_name = F.__name__
            frame = F(parent= container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, container):
        print "ok"
        frame = self.frames[container]
        frame.tkraise()

    def quit(self):
        tk.Tk.destroy()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.labelFrame_1 = tk.LabelFrame(self, text="Input 1 ", height=200, padx=10, pady=10)
        self.labelFrame_1.grid(row=0, columnspan=8, sticky='NSWE', padx=10, pady=10)

        self.type = ("Stare budownictwo", "70-85", "86-92", "93-97", "98-07" , "energooszczedny" , "niskoenegetyczny","pasywny" )



        label_1 = tk.Label(self.labelFrame_1, text="Wprowadz typ budynku")
        label_1.grid(row=0, column=0,sticky="se")
        self.var = tk.StringVar(self)
        self.var.set("Stare budownictwo")  # initial value

        option = tk.OptionMenu(self.labelFrame_1, self.var, *self.type)
        option.grid(row=0,column=1)
        self.rok = tk.IntVar()
        self.rok.set(2016)
        label_2 = tk.Label(self.labelFrame_1 , text="Rok budowy")
        entry_2 = tk.Entry(self.labelFrame_1, textvariable= self.rok)
        label_2.grid(row=1,column=0)
        entry_2.grid(row=1, column=1)

        #self.buildingType = tk.OptionMenu(self,var , "Stare budownictwo", "70-85" , "86-92" , "93-97" , "98-07" , "energooszczedny" , "niskoenegetyczny" , "pasywny")

    #def valideYear(self, year ):

       # if self.var

class ControlPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


app = Gui()
app.minsize(width=400, height=400)
app.mainloop()



