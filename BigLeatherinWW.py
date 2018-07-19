leatherID = 0x1079
leatherID2 = 0x1081
ignoreMorti = list()
cassa = 0x404A31F2
def loot(corpo):
    Items.UseItemByID(0x2D23,-1)
    Target.WaitForTarget(2000, False)
    Target.TargetExecute(corpo)
    Misc.Pause(1000)
    if Target.HasTarget(): Target.Cancel()
    Items.WaitForContents(corpo, 2000)
    for item in corpo.Contains : #itera la lista degli oggetti nel corpo
        if item.ItemID == leatherID2: #se l'oggetto è di tipo pelle lo sposta nel backpack
            Items.Move(item,Player.Backpack, 0)
            Misc.Pause(1000)
            
def AspettaMorto(mobAttaccato):
    while True:
        if  Mobiles.FindBySerial(mobAttaccato.Serial) is None:
            return
            
            
def CercaMorti():
    global ignoreMorti
    # Filtro corpi
    corpse = Items.Filter()
    corpse.Enabled = True
    corpse.OnGround = True
    corpse.Movable = False
    corpse.RangeMax = 12
    corpse.IsCorpse = True
    corpseFound = Items.ApplyFilter(corpse)
        
    for c in corpseFound: #itera la lista dei corpi trovati
        if c.Serial not in ignoreMorti:
            ignoreMorti.append(c.Serial)
            Player.PathFindTo(c.Position.X,c.Position.Y,c.Position.Z)
            Misc.Pause(2000)  
            loot(c)
                    
def RecallNextSpot(RuneBookMining1,lastrune):
    if Target.HasTarget(): Target.Cancel()
    Journal.Clear()
    while True:
        Gumps.ResetGump()
        Items.UseItem(RuneBookMining1)
        Gumps.WaitForGump(1431013363, 4000)
        Gumps.SendAction(1431013363, lastrune)
        Misc.Pause(1000)
        if not (Journal.Search("noLrc") or Journal.Search("noMana")):
            break
        Journal.Clear()
    Journal.Clear()
    
def Scarico(RuneBookMining1,lastrune):
    if Player.Weight >= Player.MaxWeight - 120:
        if Target.HasTarget(): Target.Cancel()
        Journal.Clear()
        while True:
            Gumps.ResetGump()
            Items.UseItem(RuneBookMining1)
            Gumps.WaitForGump(1431013363, 4000)
            Gumps.SendAction(1431013363, 7)
            Misc.Pause(2000)
            if not (Journal.Search("noLrc") or Journal.Search("noMana")):
                break
            Journal.Clear()
        for item in Player.Backpack.Contains:
            if item.ItemID == leatherID2:
                Items.Move(item, cassa, 0)
                Misc.Pause(1000)
        return lastrune - 6
    return lastrune            
def main(lastrune):
    RuneBookMining1=0x403113B6
    while True:
        mob=Target.GetTargetFromList("nearest")
        if mob is None:
            Misc.SendMessage("Non Trovato")
            RecallNextSpot(RuneBookMining1,lastrune)
            lastrune +6
            Misc.Pause(200)
            main(lastrune)
        while True:            
            x=mob.Position.X
            y=mob.Position.Y
            z=mob.Position.Z
            Player.PathFindTo(x-1,y-1,z)
            Player.Attack(mob)
            if Mobiles.FindBySerial(mob.Serial) is None:
                CercaMorti()
                lastrune=Scarico(RuneBookMining1,lastrune)
                main(lastrune+6)
        
        
            
        
        
 
main(13)
    

