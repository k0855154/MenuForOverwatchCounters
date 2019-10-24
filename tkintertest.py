import tkinter as tk           # python 3
from tkinter import font  as tkfont # python 3
import tkinter.ttk
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HeroPicker, Home, HeroInfo, PageOne, PageTwo, Ana, Ashe,Baptiste, Bastion,Brigitte,DVa,Doomfist,Genji,Hanzo,Junkrat,Lucio,McCree,Mei,Mercy,Moira,Orisa,Pharah,Reaper,Reinhardt,Roadhog,Sigma,Soldier76,Sombra,Symmetra,Torbjorn,Tracer,Widowmaker,Winston,WreakingBall,Zarya,Zenyatta):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class HeroInfo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hero Information", font=controller.title_font)
        label.grid(row = 0, column = 0)
        controller.title("Hero Info")
        homebutton = tk.Button(self, text="Home",fg="Black",
                            command=lambda: controller.show_frame("Home"))
        controller.geometry("750x400")

        button1 = tk.Button(self, text="Ana",fg="Green",
                            command=lambda: controller.show_frame("Ana"))
        button2 = tk.Button(self, text="Ashe",fg="Red",
                            command=lambda: controller.show_frame("Ashe"))
        button3 = tk.Button(self, text="Baptiste",fg="Green",
                            command=lambda: controller.show_frame("Baptiste"))
        button4 = tk.Button(self, text="Bastion",fg="Red",
                            command=lambda: controller.show_frame("Bastion"))
        button5 = tk.Button(self, text="Brigitte", fg="Green",
                            command=lambda: controller.show_frame("Brigitte"))
        button6 = tk.Button(self, text="D.Va",fg="Blue",
                            command=lambda: controller.show_frame("DVa"))
        button7 = tk.Button(self, text="Doomfist",fg="Red",
                            command=lambda: controller.show_frame("Doomfist"))
        button8 = tk.Button(self, text="Genji",fg="Red",
                            command=lambda: controller.show_frame("Genji"))
        button9 = tk.Button(self, text="Hanzo",fg="Red",
                            command=lambda: controller.show_frame("Hanzo"))
        button10 = tk.Button(self, text="Junkrat",fg="Red",
                            command=lambda: controller.show_frame("Junkrat"))
        button11 = tk.Button(self, text="Lucio",fg="Green",
                            command=lambda: controller.show_frame("Lucio"))
        button12 = tk.Button(self, text="McCree",fg="Red",
                            command=lambda: controller.show_frame("McCree"))
        button13 = tk.Button(self, text="Mei",fg="Red",
                            command=lambda: controller.show_frame("Mei"))
        button14 = tk.Button(self, text="Mercy",fg="Green",
                            command=lambda: controller.show_frame("Mercy"))
        button15 = tk.Button(self, text="Moira",fg="Green",
                            command=lambda: controller.show_frame("Moira"))
        button16 = tk.Button(self, text="Orisa",fg="Blue",
                            command=lambda: controller.show_frame("Orisa"))
        button17 = tk.Button(self, text="Pharah",fg="Red",
                            command=lambda: controller.show_frame("Pharah"))
        button18 = tk.Button(self, text="Reaper",fg="Red",
                            command=lambda: controller.show_frame("Reaper"))
        button19 = tk.Button(self, text="Reinhardt",fg="Blue",
                            command=lambda: controller.show_frame("Reinhardt"))
        button20 = tk.Button(self, text="Roadhog",fg="Blue",
                            command=lambda: controller.show_frame("Roadhog"))
        button21 = tk.Button(self, text="Sigma",fg="Blue",
                            command=lambda: controller.show_frame("Sigma"))
        button22 = tk.Button(self, text="Soldier 76",fg="Red",
                            command=lambda: controller.show_frame("Soldier76"))
        button23 = tk.Button(self, text="Sombra",fg="Red",
                            command=lambda: controller.show_frame("Sombra"))
        button24 = tk.Button(self, text="Symmetra",fg="Red",
                            command=lambda: controller.show_frame("Symmetra"))
        button25 = tk.Button(self, text="Torbjorn",fg="Red",
                            command=lambda: controller.show_frame("Torbjorn"))
        button26 = tk.Button(self, text="Tracer",fg="Red",
                            command=lambda: controller.show_frame("Tracer"))
        button27 = tk.Button(self, text="Widowmaker",fg="Red",
                            command=lambda: controller.show_frame("Widowmaker"))
        button28 = tk.Button(self, text="Winston",fg="Blue",
                            command=lambda: controller.show_frame("Winston"))
        button29 = tk.Button(self, text="Wreaking Ball",fg="Blue",
                            command=lambda: controller.show_frame("WreakingBall"))
        button30 = tk.Button(self, text="Zarya",fg="Blue",
                            command=lambda: controller.show_frame("Zarya"))
        button31 = tk.Button(self, text="Zenyatta",fg="Green",
                            command=lambda: controller.show_frame("Zenyatta"))
        button32 = tk.Button(self, text="Hero",
                            command=lambda: controller.show_frame("PageOne"))
        button33 = tk.Button(self, text="Hero",
                            command=lambda: controller.show_frame("PageTwo"))
        homebutton.grid(row = 0, column = 1)
        button1.grid(row = 1, column= 0)
        button2.grid(row = 1, column = 1)
        button3.grid(row = 1, column = 2)
        button4.grid(row = 1, column = 3)
        button5.grid(row = 2, column = 0)
        button6.grid(row = 2, column = 1)
        button7.grid(row = 2, column = 2)
        button8.grid(row = 2, column = 3)
        button9.grid(row = 3, column = 0)
        button10.grid(row = 3, column = 1)
        button11.grid(row = 3, column = 2)
        button12.grid(row = 3, column = 3)
        button13.grid(row = 4, column = 0)
        button14.grid(row = 4, column = 1)
        button15.grid(row = 4, column = 2)
        button16.grid(row = 4, column = 3)
        button17.grid(row = 5, column = 0)
        button18.grid(row = 5, column = 1)
        button19.grid(row = 5, column = 2)
        button20.grid(row = 5, column = 3)
        button21.grid(row = 6, column = 0)
        button22.grid(row = 6, column = 1)
        button23.grid(row = 6, column = 2)
        button24.grid(row = 6, column = 3)
        button25.grid(row = 7, column = 0)
        button26.grid(row = 7, column = 1)
        button27.grid(row = 7, column = 2)
        button28.grid(row = 7, column = 3)
        button29.grid(row = 8, column = 0)
        button30.grid(row = 8, column = 1)
        button31.grid(row = 8, column = 2)
        button32.grid(row = 8, column = 3)
        button33.grid(row = 9, column = 0)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()




class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Home Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Hero Info",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
        button = tk.Button(self, text="Hero Picker",
                           command=lambda: controller.show_frame("HeroPicker"))
        button.pack()

class Ana(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Ana",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Ashe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Ashe",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Baptiste(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Baptiste",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Bastion(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Bastion",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Brigitte(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Brigitte",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class DVa(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="D.Va",font=controller.title_font)
        Health = tk.Label(self,text=" Health: 400")
        Health.pack(side="left",fill="x",pady=10)
        Shields = tk.Label(self,text="Shields: 200")
        Shields.pack(side="left",fill="x",pady=10)
        label.pack(side="top",padx=10,pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Doomfist(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Doomfist",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Genji(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Genji",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Hanzo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Hanzo",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Junkrat(tk.Frame):    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Junkrat",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Lucio(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Lucio",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class McCree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="McCree",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Mei(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Mei",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Mercy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Mercy",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Moira(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Moira",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Orisa(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Orisa",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Pharah(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Pharah",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Reaper(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Reaper",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Reinhardt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Reinhardt",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Roadhog(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Roadhog",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Sigma(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Sigma",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Soldier76(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Soldier: 76",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Sombra(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Sombra",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Symmetra(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Symmetra",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Torbjorn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Torbjorn",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Tracer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Tracer",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Widowmaker(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Widowmaker",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Winston(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Winston",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class WreakingBall(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Wreaking Ball",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Zarya(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Zarya",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()
class Zenyatta(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="Zenyatta",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("HeroInfo"))
        button.pack()

class HeroPicker(tk.Frame):

    def __init__(self, parent, controller):
        EHeroList = []
        def EAnaAppend():
            if len(EHeroList) > 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Ana")
            return EHeroList
        def EAsheAppend():
            if len(EHeroList) > 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Ashe")
            return EHeroList
        def EBaptisteAppend():
            if len(EHeroList) > 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Baptiste")
            return EHeroList
        def EBastionAppend():
            if len(EHeroList) > 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Bastion")
            return EHeroList
       
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=EHeroList, font=controller.title_font)
        label.grid(row = 4, column = 0)
        controller.title("Hero Info")
        homebutton = tk.Button(self, text="Home",fg="Black",
                            command=lambda: controller.show_frame("Home"))
        helv12 = tkfont.Font(family='Helvetica', size=8, weight='bold')
        tkinter.ttk.Separator(self,orient="vertical").place(rely = 1,relx = 0)
        tkinter.ttk.Separator(self,orient="horizontal").grid(column=0,row=3,columnspan=20,sticky='we')
        EAna = tk.Button(self, text="Ana",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: EAnaAppend)
        EAshe = tk.Button(self, text="Ashe",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: EAsheAppend)
        button3 = tk.Button(self, text="Baptiste",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: EBaptisteAppend)
        button4 = tk.Button(self, text="Bastion",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: EBastionAppend)
        button5 = tk.Button(self, text="Brigitte", fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Brigitte"))
        button6 = tk.Button(self, text="D.Va",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("DVa"))
        button7 = tk.Button(self, text="Doomfist",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Doomfist"))
        button8 = tk.Button(self, text="Genji",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Genji"))
        button9 = tk.Button(self, text="Hanzo",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EBastionAppend)
        button10 = tk.Button(self, text="Junkrat",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: print(EHeroList))
        button11 = tk.Button(self, text="Lucio",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Lucio"))
        button12 = tk.Button(self, text="McCree",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("McCree"))
        button13 = tk.Button(self, text="Mei",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Mei"))
        button14 = tk.Button(self, text="Mercy",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Mercy"))
        button15 = tk.Button(self, text="Moira",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Moira"))
        button16 = tk.Button(self, text="Orisa",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Orisa"))
        button17 = tk.Button(self, text="Pharah",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Pharah"))
        button18 = tk.Button(self, text="Reaper",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Reaper"))
        button19 = tk.Button(self, text="Reinhardt",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Reinhardt"))
        button20 = tk.Button(self, text="Roadhog",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Roadhog"))
        button21 = tk.Button(self, text="Sigma",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Sigma"))
        button22 = tk.Button(self, text="Soldier 76",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Soldier76"))
        button23 = tk.Button(self, text="Sombra",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Sombra"))
        button24 = tk.Button(self, text="Symmetra",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Symmetra"))
        button25 = tk.Button(self, text="Torbjorn",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Torbjorn"))
        button26 = tk.Button(self, text="Tracer",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Tracer"))
        button27 = tk.Button(self, text="Widowmaker",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Widowmaker"))
        button28 = tk.Button(self, text="Winston",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Winston"))
        button29 = tk.Button(self, text="Wreaking Ball",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("WreakingBall"))
        button30 = tk.Button(self, text="Zarya",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Zarya"))
        button31 = tk.Button(self, text="Zenyatta",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("Zenyatta"))
        button32 = tk.Button(self, text="Hero",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("PageOne"))
        button33 = tk.Button(self, text="Hero",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: controller.show_frame("PageTwo"))
        homebutton.grid(row = 0, column = 1)
        
        dxadd = 0.1
        dx1 = 0.1
        dx2 = dx1 + dxadd
        dx3 = dx2 + dxadd
        dx4 = dx3 + dxadd
        dx5 = dx4 + dxadd
        dy_add = 0.1
        dy1 = 0.2
        dy2 = dy1 + dy_add
        dy3 = dy2 + dy_add
        dy4 = dy3 + dy_add
        dy5 = dy4 + dy_add
        dy6 = dy5 + dy_add
        dy7 = dy6 + dy_add
        dy8 = dy7 + dy_add
        loc = "e"
        EAna.place(relx = dx1, rely = dy1, anchor = loc)
        EAshe.place(relx = dx2, rely = dy1, anchor = loc)
        button3.place(relx = dx3, rely = dy1, anchor = loc)
        button4.place(relx = dx4, rely = dy1, anchor = loc)
        button5.place(relx = dx5, rely = dy1, anchor = loc)
        button6.place(relx = dx1, rely = dy2, anchor = loc)
        button7.place(relx = dx2, rely = dy2, anchor = loc)
        button8.place(relx = dx3, rely = dy2, anchor = loc)
        button9.place(relx = dx4, rely = dy2, anchor = loc)
        button10.place(relx = dx5, rely = dy2, anchor = loc)
        button11.place(relx = dx1, rely = dy3, anchor = loc)
        button12.place(relx = dx2, rely = dy3, anchor = loc)
        button13.place(relx = dx3, rely = dy3, anchor = loc)
        button14.place(relx = dx4, rely = dy3, anchor = loc)
        button15.place(relx = dx5, rely = dy3, anchor = loc)
        button16.place(relx = dx1, rely = dy4, anchor = loc)
        button17.place(relx = dx2, rely = dy4, anchor = loc)
        button18.place(relx = dx3, rely = dy4, anchor = loc)
        button19.place(relx = dx4, rely = dy4, anchor = loc)
        button20.place(relx = dx5, rely = dy4, anchor = loc)
        button21.place(relx = dx1, rely = dy5, anchor = loc)
        button22.place(relx = dx2, rely = dy5, anchor = loc)
        button23.place(relx = dx3, rely = dy5, anchor = loc)
        button24.place(relx = dx4, rely = dy5, anchor = loc)
        button25.place(relx = dx5, rely = dy5, anchor = loc)
        button26.place(relx = dx1, rely = dy6, anchor = loc)
        button27.place(relx = dx2, rely = dy6, anchor = loc)
        button28.place(relx = dx3, rely = dy6, anchor = loc)
        button29.place(relx = dx4, rely = dy6, anchor = loc)
        button30.place(relx = dx5, rely = dy6, anchor = loc)
        button31.place(relx = dx1, rely = dy7, anchor = loc)
        button32.place(relx = dx2, rely = dy8, anchor = loc)
        button33.place(relx = dx3, rely = dy8, anchor = loc)


        FAna = tk.Button(self, text="Ana",fg="Green",
                            command=lambda: controller.show_frame("Ana"))
        FAshe = tk.Button(self, text="Ashe",fg="Red",
                            command=lambda: controller.show_frame("Ashe"))
        FBaptiste = tk.Button(self, text="Baptiste",fg="Green",
                            command=lambda: controller.show_frame("Baptiste"))
        FBastion = tk.Button(self, text="Bastion",fg="Red",
                            command=lambda: controller.show_frame("Bastion"))
        FBrigitte = tk.Button(self, text="Brigitte", fg="Green",
                            command=lambda: controller.show_frame("Brigitte"))
        FDVa = tk.Button(self, text="D.Va",fg="Blue",
                            command=lambda: controller.show_frame("DVa"))
        FDoomfist = tk.Button(self, text="Doomfist",fg="Red",
                            command=lambda: controller.show_frame("Doomfist"))
        FGenji = tk.Button(self, text="Genji",fg="Red",
                            command=lambda: controller.show_frame("Genji"))
        FHanzo = tk.Button(self, text="Hanzo",fg="Red",
                            command=lambda: controller.show_frame("Hanzo"))
        FJunkrat = tk.Button(self, text="Junkrat",fg="Red",
                            command=lambda: controller.show_frame("Junkrat"))
        FLucio = tk.Button(self, text="Lucio",fg="Green",
                            command=lambda: controller.show_frame("Lucio"))
        FMcCree = tk.Button(self, text="McCree",fg="Red",
                            command=lambda: controller.show_frame("McCree"))
        FMei = tk.Button(self, text="Mei",fg="Red",
                            command=lambda: controller.show_frame("Mei"))
        FMercy = tk.Button(self, text="Mercy",fg="Green",
                            command=lambda: controller.show_frame("Mercy"))
        FMoira = tk.Button(self, text="Moira",fg="Green",
                            command=lambda: controller.show_frame("Moira"))
        FOrisa = tk.Button(self, text="Orisa",fg="Blue",
                            command=lambda: controller.show_frame("Orisa"))
        FPharah = tk.Button(self, text="Pharah",fg="Red",
                            command=lambda: controller.show_frame("Pharah"))
        FReaper = tk.Button(self, text="Reaper",fg="Red",
                            command=lambda: controller.show_frame("Reaper"))
        FReinhardt = tk.Button(self, text="Reinhardt",fg="Blue",
                            command=lambda: controller.show_frame("Reinhardt"))
        FRoadhog = tk.Button(self, text="Roadhog",fg="Blue",
                            command=lambda: controller.show_frame("Roadhog"))
        FSigma = tk.Button(self, text="Sigma",fg="Blue",
                            command=lambda: controller.show_frame("Sigma"))
        FSoldier76 = tk.Button(self, text="Soldier 76",fg="Red",
                            command=lambda: controller.show_frame("Soldier76"))
        FSombra = tk.Button(self, text="Sombra",fg="Red",
                            command=lambda: controller.show_frame("Sombra"))
        FSymmetra = tk.Button(self, text="Symmetra",fg="Red",
                            command=lambda: controller.show_frame("Symmetra"))
        FTorbjorn = tk.Button(self, text="Torbjorn",fg="Red",
                            command=lambda: controller.show_frame("Torbjorn"))
        FTracer = tk.Button(self, text="Tracer",fg="Red",
                            command=lambda: controller.show_frame("Tracer"))
        FWidowmaker = tk.Button(self, text="Widowmaker",fg="Red",
                            command=lambda: controller.show_frame("Widowmaker"))
        FWinston = tk.Button(self, text="Winston",fg="Blue",
                            command=lambda: controller.show_frame("Winston"))
        FWreakingBall = tk.Button(self, text="Wreaking Ball",fg="Blue",
                            command=lambda: controller.show_frame("WreakingBall"))
        FZarya = tk.Button(self, text="Zarya",fg="Blue",
                            command=lambda: controller.show_frame("Zarya"))
        FZenyatta = tk.Button(self, text="Zenyatta",fg="Green",
                            command=lambda: controller.show_frame("Zenyatta"))
        FHero1 = tk.Button(self, text="Hero",
                            command=lambda: controller.show_frame("PageOne"))
        FHero2 = tk.Button(self, text="Hero",
                            command=lambda: controller.show_frame("PageTwo"))
        homebutton.grid(row = 0, column = 1)
        FAna.grid(row = 5, column= 10)
        FAshe.grid(row = 5, column = 11)
        FBaptiste.grid(row = 5, column = 12)
        FBastion.grid(row = 5, column = 13)
        FBrigitte.grid(row = 6, column = 10)
        FDVa.grid(row = 6, column = 11)
        FDoomfist.grid(row = 6, column = 12)
        FGenji.grid(row = 6, column = 13)
        FHanzo.grid(row = 7, column = 10)
        FJunkrat.grid(row = 7, column = 11)
        FLucio.grid(row = 7, column = 12)
        FMcCree.grid(row = 7, column = 13)
        FMei.grid(row = 8, column = 10)
        FMercy.grid(row = 8, column = 11)
        FMoira.grid(row = 8, column = 12)
        FOrisa.grid(row = 8, column = 13)
        FPharah.grid(row = 9, column = 10)
        FReaper.grid(row = 9, column = 11)
        FReinhardt.grid(row = 9, column = 12)
        FRoadhog.grid(row = 9, column = 13)
        FSigma.grid(row = 10, column = 10)
        FSoldier76.grid(row = 10, column = 11)
        FSombra.grid(row = 10, column = 12)
        FSymmetra.grid(row = 10, column = 13)
        FTorbjorn.grid(row = 11, column = 10)
        FTracer.grid(row = 11, column = 11)
        FWidowmaker.grid(row = 11, column = 12)
        FWinston.grid(row = 11, column = 13)
        FWreakingBall.grid(row = 12, column = 10)
        FZarya.grid(row = 12, column = 11)
        FZenyatta.grid(row = 12, column = 12)
        FHero1.grid(row = 12, column = 13)
        FHero2.grid(row = 13, column = 10)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
