'''

'''

leatherID = 0x1079
leatherID2 = 0x1081
piumeID=0x1BD1
ignoreMorti = list()
cassa = 0x404A31F2
ignora=list()
runa=19
arma=0x40098B88
# Filtro corpi
corpse = Items.Filter()
corpse.Enabled = True
corpse.OnGround = True
corpse.Movable = False
corpse.RangeMax = 12
corpse.IsCorpse = True
##################

def waitForMana():
    minmana = 11
    manaPause = 10000
    while (Player.Mana < minmana):
        Misc.Pause(manaPause)

def cura():
    Items.UseItemByID(0x0E21,-1)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(Player.Serial)

def checkSpada(xarma):
    xspada=Items.FindBySerial(xarma)
    if xspada.Durability<5:
        riparaSpada()
        
def riparaSpada():
    waitForMana()
    prendiRepair()
    waitForMana()
    goToFabbro()
    ripara(arma)
    waitForMana()
    
def ripara(xarma):
    Misc.SendMessage("Riparo")
    Player.UnEquipItemByLayer("RightHand")
    Misc.Pause(1000)
    Items.UseItemByID(0x14F0,-1)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(xarma)
    Misc.Pause(100)
    Player.EquipItem(xarma)
    Misc.Pause(500)
    
def goToFabbro():
    runebookFabbro=0x40315D82
    Gumps.ResetGump()
    Items.UseItem(runebookFabbro)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 49)
    Misc.Pause(2000)
    
def prendiRepair(): 
    RuneBookMining1=0x40455720
    cassa = 0x404A31F2
    
    Gumps.ResetGump()
    Items.UseItem(RuneBookMining1)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 7)
    Misc.Pause(2000)
    Player.PathFindTo(4114, 566, 7)
    Misc.Pause(500)
    xcassa=Items.FindBySerial(cassa)
    Items.WaitForContents(cassa,10000)
    for item in xcassa.Contains:
        if item.ItemID == 0x14F0:
            Items.Move(item, Player.Backpack, 1)
            Misc.Pause(1000)
            break  
                        
def LootMorti():
    global ignoreMorti
    corpseFound = Items.ApplyFilter(corpse)        
    for c in corpseFound: #itera la lista dei corpi trovati
        if c.Serial not in ignoreMorti:
            Journal.Clear()
            ignoreMorti.append(c.Serial)
            Player.PathFindTo(c.Position.X,c.Position.Y,c.Position.Z)
            Misc.Pause(2000)
            #skinna  
            Items.UseItemByID(0x2D23,-1)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(c)
            Misc.Pause(1000)
            if Target.HasTarget(): Target.Cancel()
            #loota
            if Journal.Search("You carve"):    
                Items.WaitForContents(c, 10000)
                for item in c.Contains : #itera la lista degli oggetti nel corpo
                    #if item.ItemID == piumeID:
                    if item.ItemID == leatherID2: #se l'oggetto è di tipo pelle lo sposta nel backpack
                        Items.Move(item,Player.Backpack, 0)
                        Misc.Pause(1000)
                    
def RecallNextSpot(RuneBookMining1,lastrune):
    if Target.HasTarget(): Target.Cancel()
    Gumps.ResetGump()
    Items.UseItem(RuneBookMining1)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, lastrune)
    Misc.Pause(2000)
    
def Scarico(RuneBookMining1,lastrune):
    if Player.Weight >= Player.MaxWeight - 50:
        if Target.HasTarget(): Target.Cancel()
        Journal.Clear()
        waitForMana()
        Gumps.ResetGump()
        Items.UseItem(RuneBookMining1)
        Gumps.WaitForGump(1431013363, 10000)
        Gumps.SendAction(1431013363, 7)
        Misc.Pause(2000)
        Player.PathFindTo(4114, 566, 7)
        Misc.Pause(500)
        for item in Player.Backpack.Contains:
            if item.ItemID == leatherID2:
                Items.Move(item, cassa, 0)
                Misc.Pause(1000)
        if lastrune!=19:        
            return lastrune - 6
    return lastrune 

def ScaricoInBanca(RuneBookMining1,lastrune):
    if Player.Weight >= Player.MaxWeight - 50:
        if Target.HasTarget(): Target.Cancel()
        Journal.Clear()
        waitForMana()
        Gumps.ResetGump()
        Items.UseItem(RuneBookMining1)
        Gumps.WaitForGump(1431013363, 10000)
        Gumps.SendAction(1431013363, 13)
        Misc.Pause(2000)
        Player.ChatSay(33,"BANK")
        Misc.Pause(500)
        for item in Player.Backpack.Contains:
            if item.ItemID == leatherID2:
                Items.Move(item, Player.Bank, 0)
                Misc.Pause(1000)
        if lastrune!=19:        
            return lastrune - 6
    return lastrune 
    
    
def main(lastrune):
    global ignora
    global runa
    global ignoreMorti
    RuneBookMining1=0x40455720
    checkSpada(arma)
    lock=False
    mob=Target.GetTargetFromList("nearest")
    if mob is None or mob.Serial in ignora: #se non ci sono mob 
        waitForMana()
        runa += 6
        RecallNextSpot(RuneBookMining1,runa)
        ignoreMorti = list()
        ignora = list()
        if runa >= ((6*16)+1):
            ignoreMorti = list()
            ignora = list()
            runa=19
        Misc.Pause(1000)
    else:
        Journal.Clear()
        corpseFound = Items.ApplyFilter(corpse)        
        for c in corpseFound: #itera la lista dei corpi trovati
            ignoreMorti.append(c.Serial)
        while(Mobiles.FindBySerial(mob.Serial) is not None) and mob.Serial not in ignora:#fino a quando è vivo            
            x=mob.Position.X
            y=mob.Position.Y
            z=mob.Position.Z
            if not Player.BuffsExist("Perfection"):
                Player.InvokeVirtue("Honor")
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(mob)
            if mob.Name=="a polar bear" and not Player.BuffsExist("Enemy Of One (new)"):
                Spells.CastChivalry("Enemy Of One")
                Misc.Pause(500)
            if not Player.BuffsExist("Consecrate Weapon"):
                Spells.CastChivalry("Consecrate Weapon")
                Misc.Pause(200)
            if Player.DistanceTo(mob)>2:
                Player.PathFindTo(x,y,z)           
            Player.Attack(mob)
            Misc.Pause(500)
            if Player.Hits < Player.HitsMax - 30 and not lock:
                Items.UseItemByID(0x0E21,-1)
                Target.WaitForTarget(10000, False)
                Target.TargetExecute(Player.Serial)
                lock=True
            if Journal.Search("Target cannot be seen"):
                ignora.append(mob.Serial)
            if Journal.Search("You are too far away"):
                ignora.append(mob.Serial)
            if Journal.Search("You finish applying"):
                lock=False
        if Mobiles.FindBySerial(mob.Serial) is None: #quando muore
            LootMorti()
            runa=ScaricoInBanca(RuneBookMining1,runa)
            if runa >= ((6*16)+1):
                ignoreMorti = list()
                ignora = list()
                runa=19
        Misc.Pause(1000)  
    main(runa)
                

main(runa)
    

