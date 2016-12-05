# coding=UTF-8
import os
import tkinter as tk
from PIL import Image,ImageTk
import datetime



thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

LARGE_FONT = ("Verdana", 12)


class Gui(tk.Tk):

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
        frame = self.frames[container]
        frame.tkraise()

    def quit(self):
        tk.Tk.destroy()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        #label frame
        self.labelFrame_1 = tk.LabelFrame(self, text="Techniologia wykonania budynku", height=200,width=340, padx=10, pady=10)
        self.labelFrame_1.grid(row=0, columnspan=8, sticky='NSWE', padx=10, pady=10)

        self.labelFrame_2 = tk.LabelFrame(self,text="Zapotrzebowanie na ciepłą wode", height=100, width=340,padx=10,pady=10)
        self.labelFrame_2.grid(row=1,sticky="NSWE",padx=10,pady=10)

        self.labelFrame_3 = tk.LabelFrame(self,text="Źródło ciepła zastosowane w budynku", height=100, width=340,padx=10,pady=10)
        self.labelFrame_3.grid(row=2, sticky="NSWE", padx=10, pady=10)

        self.labelFrame_4 = tk.LabelFrame(self, text="Strefa klimatyczna w której znajduje się budynek", height=100, width=340,
                                          padx=10, pady=10)
        self.labelFrame_4.grid(row=3, sticky="NSWE", padx=10, pady=10)
        self.labelFrame_5 = tk.LabelFrame(self, text="Procentowa termoizolacja budynku", height=100, width=340,
                                          padx=10, pady=10)
        self.labelFrame_5.grid(row=4, sticky="NSWE", padx=10, pady=10)
        self.labelFrame_6 = tk.LabelFrame(self, text="Powierzchnia grzewcza", height=100, width=340,
                                          padx=10, pady=10)
        self.labelFrame_6.grid(row=5, sticky="NSWE", padx=10, pady=10)

        self.labelFrame_7 = tk.LabelFrame(self, text="Operacje", height=100, width=340,
                                          padx=10, pady=10)
        self.labelFrame_7.grid(row=6, sticky="NSWE", padx=10, pady=10)

        #labels 1
        label_1 = tk.Label(self.labelFrame_1, text="Technologia budynku")
        label_1.grid(row=0, column=0, sticky="se")

        label_2 = tk.Label(self.labelFrame_1, text="Rok budowy")
        label_2.grid(row=1, column=0)

        label_3 = tk.Label(self.labelFrame_2 , text="Ilość osób")
        label_3.grid(row=2, column=0)

        label_4 = tk.Label(self.labelFrame_3, text="Ilość pomieszczeń")
        label_4.grid(row=0, column=0)

        label_5 = tk.Label(self.labelFrame_3, text="Ilość grzejników starego typu")
        label_5.grid(row=1, column=0)

        label_6 = tk.Label(self.labelFrame_3, text="Ilość grzejników nowoczesnych")
        label_6.grid(row=2, column=0)

        label_7 = tk.Label(self.labelFrame_3, text="Ilość pętli podłogowych (na pomieszczenie)")
        label_7.grid(row=3, column=0)

        label_8 = tk.Label(self.labelFrame_3, text="Ilość pętli ściennych (na pomieszczenie)")
        label_8.grid(row=4, column=0)

        label_9 = tk.Label(self.labelFrame_4, text="Strefa klimatyczna")
        label_9.grid(row=0, column=0)

        label_10 = tk.Label(self.labelFrame_5, text="Grubość ocieplenia fundamentow")
        label_10.grid(row=0, column=0)

        label_11 = tk.Label(self.labelFrame_5, text="Grubość ocieplenia ścian")
        label_11.grid(row=1, column=0)

        label_12 = tk.Label(self.labelFrame_5, text="Grubość wełny na dachu")
        label_12.grid(row=2, column=0)

        label_13 = tk.Label(self.labelFrame_6, text="Powierzchnia grzewcza w budynku")
        label_13.grid(row=0, column=0)

        # label_5 = tk.Label(self.labelFrame_4, text="Ilość osób")
        # label_5.grid(row=4, column=0)
        #
        # label_6 = tk.Label(self.labelFrame_5, text="Ilość osób")
        # label_6.grid(row=5, column=0)
        #
        # label_6 = tk.Label(self.labelFrame_6, text="Ilość osób")
        # label_6.grid(row=6, column=0)
        #entries
        self.rok = tk.IntVar()
        self.rok.set(2016)

        self.ilosob = tk.IntVar()
        self.ilosob.set(1)

        self.ilpom = tk.IntVar()
        self.ilpom.set(1)

        self.ilgrzenst = tk.IntVar()
        self.ilgrzenst.set(0)

        self.ilgrzent = tk.IntVar()
        self.ilgrzent.set(0)

        self.ilppodlg = tk.IntVar()
        self.ilppodlg.set(0)

        self.ilpscia = tk.IntVar()
        self.ilpscia.set(0)

        self.grofun = tk.IntVar()
        self.grofun.set(0)

        self.groscia = tk.IntVar()
        self.groscia.set(0)

        self.grwel = tk.IntVar()
        self.grwel.set(0)

        self.powcieplna = tk.IntVar()
        self.powcieplna.set(0)




        entry_1 = tk.Entry(self.labelFrame_1, textvariable=self.rok)
        entry_1.grid(row=1, column=1)

        entry_1.bind('<KeyPress>', self.input_range_validator)

        entry_2 = tk.Entry(self.labelFrame_2, textvariable=self.ilosob)
        entry_2.grid(row=2 , column=1, sticky="se")

        entry_2.bind('<KeyPress>', self.input_range_validator)

        entry_3 = tk.Entry(self.labelFrame_3, textvariable=self.ilpom)
        entry_3.grid(row=0, column=1, sticky="se")
        entry_3.bind('<KeyPress>', self.input_range_validator)

        entry_4 = tk.Entry(self.labelFrame_3, textvariable=self.ilgrzenst)
        entry_4.grid(row=1, column=1, sticky="se")
        entry_4.bind('<KeyPress>', self.validate_room)
        entry_4.bind('<FocusOut>', self.input_outfocus)


        entry_5 = tk.Entry(self.labelFrame_3, textvariable=self.ilgrzent)
        entry_5.grid(row=2, column=1, sticky="se")
        entry_5.bind('<KeyPress>', self.input_range_validator)
        entry_5.bind('<FocusOut>', self.input_outfocus)

        entry_6 = tk.Entry(self.labelFrame_3, textvariable=self.ilppodlg)
        entry_6.grid(row=3, column=1, sticky="se")
        entry_6.bind('<KeyPress>', self.input_range_validator)
        entry_6.bind('<FocusOut>', self.input_outfocus)

        entry_7 = tk.Entry(self.labelFrame_3, textvariable=self.ilpscia)
        entry_7.grid(row=4, column=1, sticky="se")
        entry_7.bind('<KeyPress>', self.input_range_validator)
        entry_7.bind('<FocusOut>', self.input_outfocus)

        entry_8 = tk.Entry(self.labelFrame_5, textvariable=self.grofun)
        entry_8.grid(row=0, column=1, sticky="se")
        entry_8.bind('<KeyPress>', self.input_range_validator)


        entry_9 = tk.Entry(self.labelFrame_5, textvariable=self.groscia)
        entry_9.grid(row=1, column=1, sticky="se")
        entry_9.bind('<KeyPress>', self.input_range_validator)

        entry_10 = tk.Entry(self.labelFrame_5, textvariable=self.grwel)
        entry_10.grid(row=2, column=1, sticky="se")
        entry_10.bind('<KeyPress>', self.input_range_validator)

        entry_11 = tk.Entry(self.labelFrame_6, textvariable=self.powcieplna)
        entry_11.grid(row=0, column=1, sticky="se")
        entry_11.bind('<KeyPress>', self.input_range_validator)
        # entry_4 = tk.Entry(self.labelFrame_4, textvariable=self.ilosob)
        # entry_4.grid(row=4, column=1, sticky="se")
        #
        # entry_5 = tk.Entry(self.labelFrame_5, textvariable=self.ilosob)
        # entry_5.grid(row=5, column=1, sticky="se")
        #
        # entry_6 = tk.Entry(self.labelFrame_6, textvariable=self.ilosob)
        # entry_6.grid(row=6, column=1, sticky="se")


        btn_1 = tk.Button(self.labelFrame_4, text="Strefy", command= lambda : self.popupstrefy())
        btn_1.grid(row=0,column=2)


        btn_2 = tk.Button(self.labelFrame_7, text="Sprawdź")
        btn_2.grid(row=0,column=0)

        self.strefa_type = ("Strefa 1", "Strefa 2", "Strefa 3","Strefa 4", "Strefa 5")

        self.type = ("Stare budownictwo", "70-85", "86-92", "93-97", "98-07" , "energooszczedny" , "niskoenegetyczny","pasywny" )

        self.var = tk.StringVar(self)
        self.var.set("Stare budownictwo")  # initial value

        self.strefa_var = tk.StringVar(self)
        self.strefa_var.set(self.strefa_type[0])

        self.option = tk.OptionMenu(self.labelFrame_1, self.var, *self.type)
        self.option.grid(row=0,column=1,sticky="we")

        strefa_opt = tk.OptionMenu(self.labelFrame_4, self.strefa_var ,*self.strefa_type)
        strefa_opt.grid(row=0,column=1,sticky="we")

    def validate_room(self,event):
        wyn = self.input_range_validator(event)
        print("eNTE")
        print(self.ilgrzenst.get())
        return  wyn

    def input_outfocus(self,event):
        entry = event.widget
        if self.sum_source() > self.ilpom.get():
            MsgPopup("Walidacja","\n\n\n\tSuma źródeł musi być mniejsza bądź równa jak ilość pomieszczeń\t\n\n\n")
            entry.focus_set()
            entry.delete(0,len(entry.get()))
            entry.insert(0,"0")



    def input_range_validator(self, event):
        if event.char in '0123456789':
            pass
        elif event.widget.get().count('.') == 0 and event.char == '.':
            pass
        elif event.keysym == "BackSpace" or event.keysym == 'Delete':
            pass
        else:
            return 'break'


    def popupstrefy(self):
        popup = ImagePopup("Strefy klimatyczne w Polsce","assets/strefy.jpg")

    def check_technology(self):
        if self.rok >= 1900 and self.rok <= datetime.now().year:
            return True
        return False


    def check_thermal(self):
        procFun = (0 if self.grofun.get() <=0 else (self.grofun.get() / 12) * 100 )
        procScian = ( 0 if self.groscia.get() <= 0 else (self.groscia.get() / 15) * 100)
        procDach = (0 if self.grwel.get() <= 0 else (self.grwel.get() / 30 ) * 100 )

        skladany = (procFun + procScian + procDach) / 300
        # SET insulation.set(skladany)

    def check_surface(self):
        powierzchnia = (1 if self.powcieplna.get() <=0 else self.powcieplna.get())
        powierzchnia ( 200 if self.powcieplna.get() > 200 else self.powcieplna.get())
        self.powcieplna.set(powierzchnia)

        # SET surface.set(powierzchnia)

    def check_zone(self):
        zone = int(self.strefa_type[-1:])

        #SET zone.set(zone)

    def check_source(self):

        if self.ilpom.get() <= self.sum_source():
            proc_g_stary = (0 if self.ilgrzenst.get() <=0 else ( self.ilgrzenst.get() / self.ilpom.get()))
            proc_g_nowy = (0 if self.ilgrzent.get() <=0 else ( self.ilgrzent.get() / self.ilpom.get()))
            proc_p_pod = (0 if self.ilppodlg.get() <=0 else ( self.ilppodlg.get() / self.ilpom.get()))
            proc_p_scia = (0 if self.ilpscia.get() <=0 else ( self.ilpscia.get() / self.ilpom.get()))

            skladany = ((proc_g_stary + proc_g_nowy + proc_p_pod + proc_p_scia) / self.ilpom.get()) * 100

            #SET sourceTermal.set(skladany)


    def sum_source(self):
        return self.ilgrzent.get() + self.ilpscia.get() + self.ilppodlg.get() + self.ilgrzenst.get()

    def check_wear(self):

        if self.ilosob.get()>=1 and self.ilosob.get() <=8:
            1
            #SET waerWater.set(self.ilosob.get())

    def check_building(self):

        yearperwar = 6
        years = self.type[1:5]
        if years.index(self.var.get()):
            value = self.rok.get() * yearperwar






class MsgPopup:

    def __init__(self,title,msg):
        popup = tk.Toplevel()
        popup.title(title)
        label = tk.Label(popup,text=msg)
        label.grid(row=0,column=0)

class ImagePopup:

    def __init__(self,title, image):
        popup = tk.Toplevel()
        popup.title(title)
        im = Image.open(os.path.abspath(image))
        img = ImageTk.PhotoImage(im)
        lb = tk.Label(popup, image=img)
        lb.image = img
        lb.grid(row=0,column=0)


class ControlPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)





app = Gui()
app.minsize(width=400, height=400)
app.mainloop()



