####################################
######### Parametri ################
###################################
RuneBookBanca = 0x4038DA43 # Runebook for casa
RuneBookMining = 0x40315DF3 # Runebook for mine spots
RuneBookMining2 = 0x40312B17
NumeroRuneMiningBook = 16 # Numero di rune presenti nel runebook
NumeroRuneMiningBook2 = 11
MineBag = 0x404A31F2 # Serial of mine bag
MineBag2 = 0x404A2FB9 # Serial per i gioielli
FoodBag = 0x403A285D
PosizioneRunaCasa = 5
PlayerSerial = Player.Serial
#
TimeoutOnWaitAction = 4000

####################################
######### Variabili Sistema#########
####################################

pickaxeID = 0x0E86
forgiaID = 0x3C8BC # pet
forgiacasaID = 0x0FB1
tinkerID = 0x1EB8
oreID = [ 0x19B7, 0x19B8, 0x19B9, 0x19BA ]
gemmaID = [ 0x3195, 0x3193, 0x3194, 0x3192, 0x3198 ,0x3197 ]
AllFood =  [0x09C9 , 0x09F2, 0x09B7, 0x09C0, 0x097D, 0x09D2, 0x09D0, 0x09D1, 0x09EB, 0x097B]
#ham,ribs,cooked bird, sausage
SiFoodID = [ 0x09C9 , 0x09F2, 0x09B7, 0x09C0 ]
#cheese, pesca, apple, fragola, muffin,fish
noFoodID = [ 0x097D, 0x09D2, 0x09D0, 0x09D1, 0x09EB, 0x097B ]
ingotID = 0x1BF2
lastrune = 5
RecallPause = 4500
noLrc = ("More reagents are needed for this spell")
noMana = ("Insufficient mana for this spell")
noPickaxe = ("You have worn out your tool!")
locationBlocked = ("that location is blocked")
noMetal = ("There is no metal here to mine")
youcant = ("You can't mine there")
cantseen = ("Target cannot be seen")
onloop = True
WeightLimit = Player.MaxWeight - 80
PosizioneRunaCasa = PosizioneRunaCasa * 6 - 1
DragDelay = 1200

#######################################################
def saveDebug(Stringa):
    Stringa = "%s%s"%(Stringa,"\n")
    with open("logGiocoMiner.txt" , 'a') as txt_file:
        txt_file.write(Stringa)

def createFood():
    Journal.Clear()
    while True:
        Spells.CastMagery("Create Food")
        Misc.Pause(3000)
        if (Journal.Search("sausage") or Journal.Search("cut of ribs") or Journal.Search("a ham") or Journal.Search("a cooked bird")):
            moveFood()
            break
            
def moveFood():
    for item in Player.Backpack.Contains:
        for xfoodID in AllFood: 
            if item.ItemID == xfoodID:
                Misc.SendMessage("--> Sposto Cibo nella bag", 77)
                Items.Move(item, FoodBag, 0)
                Misc.Pause(DragDelay)

def moveFood2():
    FoodBagx = Items.FindBySerial(FoodBag)
    for item in FoodBagx.Contains:
            for xfoodID in noFoodID: 
                if item.ItemID == xfoodID:
                    Misc.SendMessage("--> Sposto Cibo inutile", 77)
                    Items.Move(item, MineBag2, 0)
                    Misc.Pause(DragDelay)
    Misc.SendMessage("Lingotti e Gemme scaricate", 77)

def giveFood():
    food = Items.FindBySerial(FoodBag)
    for item in food.Contains:
        for petfood in SiFoodID:
            if item.ItemID == petfood:
                Items.Move(item, forgiaID, 0)
                Misc.Pause(DragDelay)
                return
    createFood()
    giveFood()
     
    
def smeltaDaCassa():
    cont = Items.FindBySerial(MineBag)
    for item in cont.Contains:
        for xoreID in oreID:
            if item.ItemID == xoreID:
                Items.UseItem(item)
                Target.WaitForTarget(2000, False)
                Target.TargetExecute(0x40487754)
                Misc.Pause(200)

def smelta():
    if Player.Weight >= WeightLimit - 130:
        if Target.HasTarget(): Target.Cancel()
        for item in Player.Backpack.Contains:
            for xoreID in oreID:
                if item.ItemID == xoreID:
                    Items.UseItem(item)
                    Target.WaitForTarget(2000,False)
                    Target.TargetExecute(forgiaID)
                    Misc.Pause(200)

def dismount():
    io = Mobiles.FindBySerial(0x00036112)
    Mobiles.UseMobile(io)

def waitForMana():
    minmana = 30
    manaPause = 10000
    while (Player.Mana < minmana):
        Misc.SendMessage("Mana sotto la soglia. Wait...", 80)
        Misc.Pause(manaPause)
    return ;

def MakePickaxe():
    if getNumeriOggetti(tinkerID) == 0:
        Misc.SendMessage("ERRORE: Non hai il Tinker Tool. Vallo a comprare" , 77)
        return
    if getNumeriOggetti(pickaxeID) >= 2:
        Misc.SendMessage("Hai già abbastanza pickaxe", 77)
    else:
        Items.UseItemByID(tinkerID,-1) #usa il tinker tool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8) # tools
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 114) # pickaxe
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0) # close
        
def MakeTinkerTool():
    if getNumeriOggetti(tinkerID) < 2:
        Items.UseItemByID(tinkerID,-1) #usa il tinker tool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8) # tools
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23) # tinkertool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0) # close
    
def getNumeriOggetti(xxxID):
    i = 0
    for item in Player.Backpack.Contains:
        if item.ItemID == xxxID:
            i+=1
    return i

def switchRuneBook():
    global RuneBookMining
    global RuneBookMining2
    global NumeroRuneMiningBook
    global NumeroRuneMiningBook2
    RuneBookTemp = RuneBookMining
    RuneBookMining = RuneBookMining2
    RuneBookMining2 = RuneBookTemp
    NumeroRuneMiningBookTemp = NumeroRuneMiningBook
    NumeroRuneMiningBook = NumeroRuneMiningBook2
    NumeroRuneMiningBook2 = NumeroRuneMiningBookTemp

def Scarico( ):
    global lastrune
    if Player.Weight >= WeightLimit - 120:
        if Target.HasTarget(): Target.Cancel()
        Journal.Clear()
        waitForMana()
        while True:
            Gumps.ResetGump()
            Items.UseItem(RuneBookBanca)
            Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
            Gumps.SendAction(1431013363, PosizioneRunaCasa)
            Misc.Pause(RecallPause)
            if not (Journal.Search(noLrc) or Journal.Search(noMana)):
                break
            Journal.Clear()
        for item in Player.Backpack.Contains:
            #for xoreID in oreID:
                if item.ItemID == ingotID:
                    Misc.SendMessage("--> Sposto lingotti", 77)
                    Items.Move(item, MineBag, 0)
                    Misc.Pause(DragDelay)
        for item in Player.Backpack.Contains:
            for xgemmaID in gemmaID:
                if item.ItemID == xgemmaID:
                    Misc.SendMessage("--> Sposto Gemme", 77)
                    Items.Move(item, MineBag2, 0)
                    Misc.Pause(DragDelay)
        
        xFoodBag = Items.FindBySerial(FoodBag)
        for item in xFoodBag.Contains:
            for xfoodID in noFoodID: 
                if item.ItemID == xfoodID:
                    Misc.SendMessage("--> Sposto Cibo inutile", 77)
                    Items.Move(item, MineBag2, 0)
                    Misc.Pause(DragDelay)
        Misc.SendMessage("Lingotti e Gemme scaricate", 77)
        lastrune = lastrune - 6

def RecallNextSpot( ):
    if Target.HasTarget(): Target.Cancel()
    global lastrune
    if lastrune >= ((6*NumeroRuneMiningBook)-1):
        switchRuneBook()
        lastrune = 5
    Journal.Clear()
    while True:
        Gumps.ResetGump()
        Misc.SendMessage("--> Racall to Spot", 77)
        Items.UseItem(RuneBookMining)
        Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
        Gumps.SendAction(1431013363, lastrune)
        Misc.Pause(RecallPause)
        if not (Journal.Search(noLrc) or Journal.Search(noMana)):
            break
        Journal.Clear()
    Journal.Clear()
    lastrune = lastrune + 6

def Mina():
    tileinfo = Statics.GetStaticsTileInfo(Player.Position.X, Player.Position.Y, Player.Map)
    if tileinfo.Count > 0:
        minaCava()
    else:
        minaMontagna()
                    
                    
def minaCava():
    uscitaDiSicurezza = 15
    Journal.Clear()
    tileinfo = Statics.GetStaticsTileInfo(Player.Position.X, Player.Position.Y, Player.Map)
    for tile in tileinfo:
        if tile.StaticID > 1000 and tile.StaticID < 3000 and tile.StaticZ == Player.Position.Z :
            for x in range(-1,2):
                Journal.Clear()
                for y in range(-1,2):
                    Journal.Clear()                
                    Items.UseItemByID(pickaxeID,-1)
                    Target.WaitForTarget(2000,False)
                    Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,0,tile.StaticID)
                    Misc.Pause(300)
                    if (Journal.Search(noMetal)):
                        Misc.SendMessage("NoMetallo")
                        if Target.HasTarget(): Target.Cancel()
                        break
                    if (Journal.Search("You dig some") or Journal.Search("You loosen")):
                        while not(Journal.Search(noMetal) or Journal.Search(youcant) or Journal.Search(cantseen) or uscitaDiSicurezza<1):
                            Items.UseItemByID(pickaxeID,-1)
                            Target.WaitForTarget(2000,False)
                            Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,0,tile.StaticID)
                            Misc.Pause(500)
def minaMontagna():
    uscitaDiSicurezza = 15
    for x in range(-1,2):
        Journal.Clear()
        for y in range(-1,2):
            Journal.Clear() 
            Items.UseItemByID(pickaxeID,-1)
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,Player.Position.Z)
            Misc.Pause(300)
            if (Journal.Search(noMetal)):
                Misc.SendMessage("NoMetallo")
                if Target.HasTarget(): Target.Cancel()
                break
            if (Journal.Search("You dig some") or Journal.Search("You loosen")):
                while not(Journal.Search(noMetal) or Journal.Search(youcant) or Journal.Search(cantseen) or uscitaDiSicurezza<1):
                    Items.UseItemByID(pickaxeID,-1)
                    Target.WaitForTarget(2000,False)
                    Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,Player.Position.Z)
                    uscitaDiSicurezza-=1
                    Misc.Pause(500)
                                    
def main():
    global lastrune
    global NumeroRuneMiningBook
    Misc.SendMessage("--> Start Miner", 22)
    dismount()
    giveFood()
    while onloop:
        smelta()
        MakeTinkerTool()
        MakePickaxe()
        Scarico()  
        RecallNextSpot()
        waitForMana()
        Mina()
                     
##################
main()





        