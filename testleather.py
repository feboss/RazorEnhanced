waitAfterCut = 1000
waitAfterMove = 1500
waitForContents = 5000
waitForTarget = 1500
#0x2D23 cleaver
#0x0EC5 coltellino

leatherID = 0x1079
leatherID2 = 0x1081

ignore = list()
while True:  
    # Filtro corpi
    corpse = Items.Filter()
    corpse.Enabled = True
    corpse.OnGround = True
    corpse.Movable = False
    corpse.RangeMax = 2
    corpse.IsCorpse = True
    corpseFound = Items.ApplyFilter(corpse)
    
    for c in corpseFound: #itera la lista dei corpi trovati
        if c.Serial not in ignore:
            ignore.append(c.Serial)
            Items.UseItemByID(0x2D23,-1)
            Target.WaitForTarget(waitForTarget, False)
            Target.TargetExecute(c)
            Misc.Pause(waitAfterCut)
            if Target.HasTarget(): Target.Cancel()
            Items.WaitForContents(c, waitForContents) #apre il corpo e ne scansiona il contenuto
            for item in c.Contains : #itera la lista degli oggetti nel corpo
                if item.ItemID == leatherID2: #se l'oggetto è di tipo pelle lo sposta nel backpack
                    Items.Move(item,Player.Backpack, 0)
                    Misc.Pause(waitAfterMove)
                    #Items.UseItemByID(0x0F9E,-1)
                    #Target.WaitForTarget(waitForTarget, False)
                    #Target.TargetExecute(item)
                    #Misc.Pause(waitAfterCut)              
            Misc.Pause(200)
    Misc.Pause(200)