leatherID = 0x1079
leatherID2 = 0x1081
ignoreMorti = list()
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
        

def main():
    while True:
        mob=Target.GetTargetFromList("nearest")
        while True:            
            x=mob.Position.X
            y=mob.Position.Y
            z=mob.Position.Z
            Player.PathFindTo(x-1,y-1,z)
            Player.Attack(mob)
        if Mobiles.FindBySerial(mob) is None:    
            CercaMorti()
            break
        
        
 
main()
    

