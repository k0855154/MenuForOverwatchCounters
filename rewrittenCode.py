import main
import OverwatchData
Hero = ""
HeroL = []
LocationHero = []
ListOfCounters = []
def getHero(Hero):
    HeroL.append(EHero)
    #Get Location of Hero in List for Counter Finding
    for a in range(len(HeroL)):
      LocationHero.append(main.HeroList.index(HeroL[a]))
    return LocationHero, Hero

def getCounters(LocationHero, HeroL):
    for o in range(len(HeroL)):
        ListOfCounters.append(main.OverwatchCounters[LocationHero[o-1]])
        print(ListOfCounters)
    

def repeat():
    x,y = getHero(Hero)
    LocationHero = x
    getCounters(LocationHero, HeroL)  
    if len(HeroL) == 1:
        #Hero1S = main.ListSynergies[0]
        print("Number 5")
        NumRowsToAdd = 5
    elif len(HeroL) == 2:
        
        #Hero2S = main.ListSynergies[1]
        print("Number 4")
        NumRowsToAdd = 4
        return NumRowsToAdd
    elif len(HeroL) == 3:
        
        #Hero3S = main.ListSynergies[2]
        print("Number 3")
        NumRowsToAdd = 3
    elif len(HeroL) == 4:
        
        #Hero4S = main.ListSynergies[3]
        print("Number 2")
        NumRowsToAdd = 2
    elif len(HeroL) == 5:

        #Hero5S = main.ListSynergies[4]
        NumRowsToAdd = 1
    elif len(HeroL) == 6:
        #Hero6S = main.ListSynergies[5]
        print("Number 1")
        NumRowsToAdd = 0
    rows = 0
    for rows in range(NumRowsToAdd + 1):
      ListOfCounters.append(OverwatchData.Nothing.NothingCounters)
      rows =+ 1
    print(ListOfCounters)
    HeroSum1 = []
    Hero1C = ListOfCounters[0]
    Hero2C = ListOfCounters[1]
    Hero3C = ListOfCounters[2]
    Hero4C = ListOfCounters[3]
    Hero5C = ListOfCounters[4]
    Hero6C = ListOfCounters[5]
    for c in range(30):
      HeroSum1.append(Hero1C[c] + Hero2C[c] + Hero3C[c] + Hero4C[c] + Hero5C[c] + Hero6C[c])
    for d in range(30):
        print(main.HeroList[d],HeroSum1[d])
        d =+ 1
    print(ListOfCounters)
    print(Hero)
    print(Hero1C)
    print(Hero2C)
    print(Hero3C)
    print(Hero4C)
    print(Hero5C)
    print(Hero6C)
    print(LocationHero)
    print(HeroL)
    print(len(HeroL)-1)
repeat()
ListOfCounters = []
LocationHero = []
repeat()

