import tkinter as tk           # python 3
from tkinter import font  as tkfont # python 3
import tkinter.ttk
import tkinter.colorchooser
from tkinter import StringVar, IntVar     # python 2
import tkinter.Calendar
#import tkFont as tkfont  # python 2
EHeroList = []
FHeroList = []
EScores = []
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
        button.pack

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
        import main
        import OverwatchData
        Locations = []
        def Calculations():
            EnHero = EHeroList[len(EHeroList)-1]
            ELHero = EnHero
            print(ELHero)
            if ELHero in main.HeroList:
                print(ELHero)
                def findHero():
                    HeroLocation = main.HeroList.index(ELHero)
                    print(HeroLocation)
                    Locations.append(HeroLocation)
                    print(Locations)
                def getScores():
                     ListCounters = []
                     for i in range(len(Locations)):
                         ListCounters.append(main.OverwatchCounters[Locations[i]])
                         print(ListCounters)
                     if len(Locations) == 1:
                          #Hero1S = main.ListSynergies[0]
                          print("Number 5")
                          NumRowsToAdd = 5
                     elif len(Locations) == 2:
                          #Hero2S = main.ListSynergies[1]
                          print("Number 4")
                          NumRowsToAdd = 4
                          return NumRowsToAdd
                     elif len(Locations) == 3:
                          #Hero3S = main.ListSynergies[2]
                          print("Number 3")
                          NumRowsToAdd = 3
                     elif len(Locations) == 4:
                          #Hero4S = main.ListSynergies[3]
                          print("Number 2")
                          NumRowsToAdd = 2
                     elif len(Locations) == 5:
                          #Hero5S = main.ListSynergies[4]
                          NumRowsToAdd = 1
                     elif len(Locations) == 6:
                          #Hero6S = main.ListSynergies[5]
                        print("Number 1")
                        NumRowsToAdd = 0
                     for i in range(NumRowsToAdd):
                        ListCounters.append(OverwatchData.Nothing.NothingCounters)
                     print(ListCounters)
                     HeroSum1 = []
                     Hero1C = ListCounters[0]
                     Hero2C = ListCounters[1]
                     Hero3C = ListCounters[2]
                     Hero4C = ListCounters[3]
                     Hero5C = ListCounters[4]
                     Hero6C = ListCounters[5]
                     print(Hero1C)
                     print(Hero2C)
                     print(Hero3C)
                     print(Hero4C)
                     print(Hero5C)
                     print(Hero6C)
                     for c in range(31):
                        HeroSum1.append(Hero1C[c] + Hero2C[c] + Hero3C[c] + Hero4C[c] + Hero5C[c] + Hero6C[c])
                     for d in range(31):
                        print(main.HeroList[d],HeroSum1[d])
                        d =+ 1  
                findHero()
                getScores()
            else:
                print("Error")




        def PrintHeroes():
            scores = tkinter.Tk()
        #    e1 = tk.Entry(scores) 
        #    e2 = tk.Entry(scores) 
        #    e1.grid(row=0, column=1) 
        #    e2.grid(row=1, column=1) 
            text_var = tk.StringVar(scores)
            text_var.set(scores)
            tk.Label(scores,textvariable=text_var).pack()
         #   tk.Label(scores, text='First Name').grid(row=0) 
         #   tk.Label(scores, textvariable=yelll).grid(row=1)
            buttonbutton = tk.Button(scores,textvariable=yelll,command=lambda:print("Hello"))
            buttonbutton.pack()
            scores.mainloop()

        
        def EAnaAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Ana")
                Calculations()
            return EHeroList
        def EAsheAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Ashe")
                Calculations()
            return EHeroList
        def EBaptisteAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Baptiste")
                Calculations()
            return EHeroList
        def EBastionAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Bastion")
                Calculations()
            return EHeroList
        def EBrigitteAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Brigitte")
                Calculations()
            return EHeroList
        def EDVaAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("DVa")
                Calculations()
            return EHeroList
        def EDoomfistAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Doomfist")
                Calculations()
            return EHeroList
        def EGenjiAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Genji")
                Calculations()
            return EHeroList
        def EHanzoAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Hanzo")
                Calculations()
                Calculations()
            return EHeroList
        def EJunkratAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Junkrat")
                Calculations()
            return EHeroList
        def ELucioAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Lucio")
                Calculations()
            return EHeroList
        def EMcCreeAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("McCree")
                Calculations()
            return EHeroList
        def EMeiAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Mei")
                Calculations()
            return EHeroList
        def EMercyAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Mercy")
                Calculations()
            return EHeroList
        def EMoiraAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Moira")
                Calculations()
            return EHeroList
        def EOrisaAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Orisa")
                Calculations()
            return EHeroList
        def EPharahAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Pharah")
                Calculations()
            return EHeroList
        def EReaperAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Reaper")
                Calculations()
            return EHeroList
        def EReinhardtAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Reinhardt")
                Calculations()
            return EHeroList
        def ERoadhogAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Roadhog")
                Calculations()
            return EHeroList
        def ESigmaAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Sigma")
                Calculations()
            return EHeroList
        def ESoldier76Append():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Soldier 76")
                Calculations()
            return EHeroList
        def ESombraAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Sombra")
                Calculations()
            return EHeroList
        def ESymmetraAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Symmetra")
                Calculations()
            return EHeroList
        def ETorbjornAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Torbjorn")
                Calculations()
            return EHeroList
        def ETracerAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Tracer")
                Calculations()
            return EHeroList
        def EWidowmakerAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Widowmaker")
                Calculations()
            return EHeroList
        def EWinstonAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Winston")
                Calculations()
            return EHeroList
        def EWreakingBallAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Hammond")
                Calculations()
            return EHeroList
        def EZaryaAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Zarya")
                Calculations()
            return EHeroList
        def EZenyattaAppend():
            if len(EHeroList) >= 6:
                print("Hero List Filled")
            else:
                EHeroList.append("Zenyatta")
                Calculations()
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
                            command=EAnaAppend)
        EAshe = tk.Button(self, text="Ashe",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EAsheAppend)
        EBaptiste = tk.Button(self, text="Baptiste",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=EBaptisteAppend)
        EBastion = tk.Button(self, text="Bastion",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EBastionAppend)
        EBrigitte = tk.Button(self, text="Brigitte", fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=EBrigitteAppend)
        EDVa = tk.Button(self, text="D.Va",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=EDVaAppend)
        EDoomfist = tk.Button(self, text="Doomfist",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EDoomfistAppend)
        EGenji = tk.Button(self, text="Genji",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EGenjiAppend)
        EHanzo = tk.Button(self, text="Hanzo",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EHanzoAppend)
        EJunkrat = tk.Button(self, text="Junkrat",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EJunkratAppend)
        ELucio = tk.Button(self, text="Lucio",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=ELucioAppend)
        EMcCree = tk.Button(self, text="McCree",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EMcCreeAppend)
        EMei = tk.Button(self, text="Mei",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EMeiAppend)
        EMercy = tk.Button(self, text="Mercy",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=EMercyAppend)
        EMoira = tk.Button(self, text="Moira",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=EMoiraAppend)
        EOrisa = tk.Button(self, text="Orisa",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=EOrisaAppend)
        EPharah = tk.Button(self, text="Pharah",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EPharahAppend)
        EReaper = tk.Button(self, text="Reaper",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EReaperAppend)
        EReinhardt = tk.Button(self, text="Reinhardt",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=EReinhardtAppend)
        ERoadhog = tk.Button(self, text="Roadhog",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=ERoadhogAppend)
        ESigma = tk.Button(self, text="Sigma",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=ESigmaAppend)
        ESoldier76 = tk.Button(self, text="Soldier 76",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=ESoldier76Append)
        ESombra = tk.Button(self, text="Sombra",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=ESombraAppend)
        ESymmetra = tk.Button(self, text="Symmetra",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=ESymmetraAppend)
        ETorbjorn = tk.Button(self, text="Torbjorn",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=ETorbjornAppend)
        ETracer = tk.Button(self, text="Tracer",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=ETracerAppend)
        EWidowmaker = tk.Button(self, text="Widowmaker",fg="Red",height=1,width=9,anchor="center",font=helv12,
                            command=EWidowmakerAppend)
        EWinston = tk.Button(self, text="Winston",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=EWinstonAppend)
        EWreakingBall = tk.Button(self, text="Wreaking Ball",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=EWreakingBallAppend)
        EZarya = tk.Button(self, text="Zarya",fg="Blue",height=1,width=9,anchor="center",font=helv12,
                            command=EZaryaAppend)
        EZenyatta = tk.Button(self, text="Zenyatta",fg="Green",height=1,width=9,anchor="center",font=helv12,
                            command=EZenyattaAppend)
        EHero1 = tk.Button(self, text="Hero",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: EHeroList.clear())
        EHero2 = tk.Button(self, text="Hero",height=1,width=9,anchor="center",font=helv12,
                            command=lambda: print(EHeroList))
        EPrintHeroes = tk.Button(self,text="PHeroes",height=1,width=9,anchor="center",font=helv12,command=PrintHeroes)
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
        EBaptiste.place(relx = dx3, rely = dy1, anchor = loc)
        EBastion.place(relx = dx4, rely = dy1, anchor = loc)
        EBrigitte.place(relx = dx5, rely = dy1, anchor = loc)
        EDoomfist.place(relx = dx2, rely = dy2, anchor = loc)
        EDVa.place(relx = dx1, rely = dy2, anchor = loc)
        EDoomfist.place(relx = dx2, rely = dy2, anchor = loc)
        EGenji.place(relx = dx4, rely = dy2, anchor = loc)
        EHanzo.place(relx = dx5, rely = dy2, anchor = loc)
        EJunkrat.place(relx = dx1, rely = dy3, anchor = loc)
        ELucio.place(relx = dx2, rely = dy3, anchor = loc)
        EMcCree.place(relx = dx3, rely = dy3, anchor = loc)
        EMei.place(relx = dx4, rely = dy3, anchor = loc)
        EMercy.place(relx = dx5, rely = dy3, anchor = loc)
        EMoira.place(relx = dx1, rely = dy4, anchor = loc)
        EOrisa.place(relx = dx2, rely = dy4, anchor = loc)
        EPharah.place(relx = dx3, rely = dy4, anchor = loc)
        EReaper.place(relx = dx4, rely = dy4, anchor = loc)
        EReinhardt.place(relx = dx5, rely = dy4, anchor = loc)
        ERoadhog.place(relx = dx1, rely = dy5, anchor = loc)
        ESigma.place(relx = dx2, rely = dy5, anchor = loc)
        ESoldier76.place(relx = dx3, rely = dy5, anchor = loc)
        ESombra.place(relx = dx4, rely = dy5, anchor = loc)
        ESymmetra.place(relx = dx5, rely = dy5, anchor = loc)
        ETorbjorn.place(relx = dx1, rely = dy6, anchor = loc)
        ETracer.place(relx = dx2, rely = dy6, anchor = loc)
        EWidowmaker.place(relx = dx3, rely = dy6, anchor = loc)
        EWinston.place(relx = dx4, rely = dy6, anchor = loc)
        EWreakingBall.place(relx = dx5, rely = dy6, anchor = loc)
        EZarya.place(relx = dx1, rely = dy7, anchor = loc)
        EZenyatta.place(relx = dx2, rely = dy7, anchor = loc)
        EHero1.place(relx = dx3, rely = dy7, anchor = loc)
        EHero2.place(relx = dx4, rely = dy7, anchor = loc)
        EPrintHeroes.place(relx = dx5, rely = dy7, anchor = loc)

    
    """
    def FAnaAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Ana")
        return FHeroList
    def FAsheAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Ashe")
        return FHeroList
    def FBaptisteAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Baptiste")
        return FHeroList
    def FBastionAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Bastion")
        return FHeroList
    def FBrigitteAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Brigitte")
        return FHeroList
    def FDVaAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("DVa")
        return FHeroList
    def FDoomfistAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Doomfist")
        return FHeroList
    def FGenjiAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Genji")
        return FHeroList
    def FHanzoAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Hanzo")
        return FHeroList
    def FJunkratAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Junkrat")
        return FHeroList
    def FLucioAppend():
        if len(FHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Lucio")
        return FHeroList
    def FMcCreeAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("McCree")
        return FHeroList
    def FMeiAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Mei")
        return FHeroList
    def FMercyAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Mercy")
        return FHeroList
    def FMoiraAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Moira")
        return FHeroList
    def FOrisaAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Orisa")
        return FHeroList
    def FPharahAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Pharah")
        return FHeroList
    def FReaperAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Reaper")
        return FHeroList
    def FReinhardtAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Reinhardt")
        return FHeroList
    def FRoadhogAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Roadhog")
        return FHeroList
    def FSigmaAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Sigma")
        return FHeroList
    def FSoldier76Append():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Soldier 76")
        return FHeroList
    def FSombraAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Sombra")
        return FHeroList
    def FSymmetraAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Symmetra")
        return FHeroList
    def FTorbjornAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Torbjorn")
        return FHeroList
    def FTracerAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            FHeroList.append("Tracer")
        return FHeroList
    def FWidowmakerAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            EHeroList.append("Widowmaker")
        return FHeroList
    def FWinstonAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            EHeroList.append("Winston")
        return FHeroList
    def FWreakingBallAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            EHeroList.append("Hammond")
        return FHeroList
    def FZaryaAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            EHeroList.append("Zarya")
            print(EHeroList)
        return FHeroList
    def FZenyattaAppend():
        if len(EHeroList) >= 6:
            print("Hero List Filled")
        else:
            EHeroList.append("Zenyatta")
            print(FHeroList)
        return FHeroList
    FAna = tk.Button(self, text="Ana", height= 1, width= 9, anchor= 'center', font= helv12, command=FAnaAppend)
    FAshe = tk.Button(self, text="Ashe", height= 1, width= 9, anchor= 'center', font= helv12, command=FAsheAppend)
    FBaptiste = tk.Button(self, text="Baptiste", height= 1, width= 9, anchor= 'center', font= helv12, command=FBaptisteAppend)
    FBastion = tk.Button(self, text="Bastion", height= 1, width= 9, anchor= 'center', font= helv12, command=FBastionAppend)
    FBrigitte = tk.Button(self, text="Brigitte", height= 1, width= 9, anchor= 'center', font= helv12, command=FBrigitteAppend)
    FDVa = tk.Button(self, text="DVa", height= 1, width= 9, anchor= 'center', font= helv12, command=FDVaAppend)
    FDoomfist = tk.Button(self, text="Doomfist", height= 1, width= 9, anchor= 'center', font= helv12, command=FDoomfistAppend)
    FGenji = tk.Button(self, text="Genji", height= 1, width= 9, anchor= 'center', font= helv12, command=FGenjiAppend)
    FHanzo = tk.Button(self, text="Hanzo", height= 1, width= 9, anchor= 'center', font= helv12, command=FHanzoAppend)
    FJunkrat = tk.Button(self, text="Junkrat", height= 1, width= 9, anchor= 'center', font= helv12, command=FJunkratAppend)
    FLucio = tk.Button(self, text="Lucio", height= 1, width= 9, anchor= 'center', font= helv12, command=FLucioAppend)
    FMcCree = tk.Button(self, text="McCree", height= 1, width= 9, anchor= 'center', font= helv12, command=FMcCreeAppend)
    FMei = tk.Button(self, text="Mei", height= 1, width= 9, anchor= 'center', font= helv12, command=FMeiAppend)
    FMercy = tk.Button(self, text="Mercy", height= 1, width= 9, anchor= 'center', font= helv12, command=FMercyAppend)
    FMoira = tk.Button(self, text="Moira", height= 1, width= 9, anchor= 'center', font= helv12, command=FMoiraAppend)
    FOrisa = tk.Button(self, text="Orisa", height= 1, width= 9, anchor= 'center',font= helv12, command=FOrisaAppend)
    FPharah = tk.Button(self, text="Pharah", height= 1, width= 9, anchor= 'center', font= helv12, command=FPharahAppend)
    FReaper = tk.Button(self, text="Reaper", height= 1, width= 9, anchor= 'center', font= helv12, command=FReaperAppend)
    FReinhardt = tk.Button(self, text="Reinhardt", height= 1, width= 9, anchor= 'center', font= helv12, command=FReinhardtAppend)
    FRoadhog = tk.Button(self, text="Roadhog", height= 1, width= 9, anchor= 'center', font= helv12, command=FRoadhogAppend)
    FSigma = tk.Button(self, text="Sigma", height= 1, width= 9, anchor= 'center', font= helv12, command=FSigmaAppend)
    FSoldier76 = tk.Button(self, text="Soldier76", height= 1, width= 9, anchor= 'center', font= helv12, command=FSoldier76Append)
    FSombra = tk.Button(self, text="Sombra", height= 1, width= 9, anchor= 'center', font= helv12, command=FSombraAppend)
    FSymmetra = tk.Button(self, text="Symmetra", height= 1, width= 9, anchor= 'center', font= helv12, command=FSymmetraAppend)
    FTorbjorn = tk.Button(self, text="Torbjorn", height= 1, width= 9, anchor= 'center', font= helv12, command=FTorbjornAppend)
    FTracer = tk.Button(self, text="Tracer", height= 1, width= 9, anchor= 'center', font= helv12, command=FTracerAppend)
    FWidowmaker = tk.Button(self, text="Widowmaker", height= 1, width= 9, anchor= 'center', font= helv12, command=FWidowmakerAppend)
    FWinston = tk.Button(self, text="Winston", height= 1, width= 9, anchor= 'center', font= helv12, command=FWinstonAppend)
    FWreakingBall = tk.Button(self, text="WreakingBall", height= 1, width= 9, anchor= 'center', font= helv12, command=FWreakingBallAppend)
    FZarya = tk.Button(self, text="Zarya", height= 1, width= 9, anchor= 'center', font= helv12, command=FZaryaAppend)
    FZenyatta = tk.Button(self, text="Zenyatta", height= 1, width= 9, anchor= 'center', font= helv12, command=FZenyattaAppend)
    FHero1 = tk.Button(self, text="Hero1", height= 1, width= 9, anchor= 'center', font= helv12, command=lambda:print(FHeroList))
    FHero2 = tk.Button(self, text="Hero2", height= 1, width= 9, anchor= 'center', font= helv12, command=lambda: print(FHeroList))
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
    """


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
