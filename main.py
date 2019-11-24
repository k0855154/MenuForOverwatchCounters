import OverwatchData
HeroList = ["Lucio","Reinhardt","McCree","Mercy","Zarya","DVa","Genji","Junkrat","Pharah","Reaper","Roadhog","Soldier 76","Symmetra","Widowmaker","Winston","Hanzo","Mei","Tracer","Bastion","Torbjorn","Zenyatta","Ana","Sombra","Orisa","Doomfist","Moira","Brigitte","Hammond","Ashe","Baptiste","Sigma"]

OverwatchInfo = [
  OverwatchData.Lucio.LuicoInfo,
  OverwatchData.Reinhardt.ReinhardtInfo,
  OverwatchData.McCree.McCreeInfo,
  OverwatchData.Mercy.MercyInfo,
  OverwatchData.Zarya.ZaryaInfo,
  OverwatchData.DVa.DVaInfo,
  OverwatchData.Genji.GenjiInfo,
  OverwatchData.Junkrat.JunkratInfo,
  OverwatchData.Pharah.PharahInfo,
  OverwatchData.Reaper.ReaperInfo,
  OverwatchData.Roadhog.RoadhogInfo,
  OverwatchData.Soldier76.Soldier76Info,
  OverwatchData.Symmetra.SymmetraInfo,
  OverwatchData.Widowmaker.WidowmakerInfo,
  OverwatchData.Winston.WinstonInfo,
  OverwatchData.Hanzo.HanzoInfo,
  OverwatchData.Mei.MeiInfo,
  OverwatchData.Tracer.TracerInfo,
  OverwatchData.Bastion.BastionInfo,
  OverwatchData.Torbjorn.TorbjornInfo,
  OverwatchData.Zenyatta.ZenyattaInfo,
  OverwatchData.Ana.AnaInfo,
  OverwatchData.Sombra.SombraInfo,
  OverwatchData.Orisa.OrisaInfo,
  OverwatchData.Doomfist.DoomfistInfo,
  OverwatchData.Moira.MoiraInfo,
  OverwatchData.Brigitte.BrigitteInfo,
  OverwatchData.Hammond.HammondInfo,
  OverwatchData.Ashe.AsheInfo,
  OverwatchData.Baptiste.BaptisteInfo,
  OverwatchData.Sigma.SigmaInfo]
import csv
datafile = open('scores.csv', 'r')
datareader = csv.reader(datafile, delimiter=',')
data = []
for row in datareader:
    data.append(row) 
HeroNum = 1
j = 1
OverwatchCountersEn = []
for HeroNum in range(32):
    DataLine = data[HeroNum][13:44]
    for j in range(len(DataLine)):
        OverwatchCountersEn.append(int(DataLine[j]))
start = 0
end = 31
OverwatchCountersE = []
for i in range(32):
    OverwatchCountersE.append(OverwatchCountersEn[start:start+31])
    print(i,"Start: ", start)
    print(i,"End: ", end)
    start = end
    end = start + 31

print(OverwatchCountersE.pop(0))
OverwatchCounters = OverwatchCountersE

OverwatchSynergies = [
  OverwatchData.Lucio.LucioSynergies,
  OverwatchData.Reinhardt.ReinhardtSynergies,
  OverwatchData.McCree.McCreeSynergies,
  OverwatchData.Mercy.MercySynergies,
  OverwatchData.Zarya.ZaryaSynergies,
  OverwatchData.DVa.DVaSynergies,
  OverwatchData.Genji.GenjiSynergies,
  OverwatchData.Junkrat.JunkratSynergies,
  OverwatchData.Pharah.PharahSynergies,
  OverwatchData.Reaper.ReaperSynergies,
  OverwatchData.Roadhog.RoadhogSynergies,
  OverwatchData.Soldier76.Soldier76Synergies,
  OverwatchData.Symmetra.SymmetraSynergies,
  OverwatchData.Widowmaker.WidowmakerSynergies,
  OverwatchData.Winston.WinstonSynergies,
  OverwatchData.Hanzo.HanzoSynergies,
  OverwatchData.Mei.MeiSynergies,
  OverwatchData.Tracer.TracerSynergies,
  OverwatchData.Bastion.BastionSynergies,
  OverwatchData.Torbjorn.TorbjornSynergies,
  OverwatchData.Zenyatta.ZenyattaSynergies,
  OverwatchData.Ana.AnaSynergies,
  OverwatchData.Sombra.SombraSynergies,
  OverwatchData.Orisa.OrisaSynergies,
  OverwatchData.Doomfist.DoomfistSynergies,
  OverwatchData.Moira.MoiraSynergies,
  OverwatchData.Brigitte.BrigitteSynergies,
  OverwatchData.Hammond.HammondSynergies,
  OverwatchData.Ashe.AsheSynergies,
  OverwatchData.Baptiste.BaptisteSynergies,
  OverwatchData.Sigma.SigmaSynergies]
array_length = len(HeroList)
ListHeroes = []
ListCounters = []
ListSynergies = []
ListOfListCounters = []

