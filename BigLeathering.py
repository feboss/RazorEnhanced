waitAfterCut = 1000
waitAfterMove = 1500
waitForContents = 5000
waitForTarget = 1500
#0x2D23 cleaver
#0x0EC5 coltellino
leatherID = 0x1079
leatherID2 = 0x1081


        
def KillaMob():
    mob = Mobiles.Filter()
    mob.Enabled = True
    mob.RangeMax = 10
    mob.IsHuman = 0
    mobFound = Mobiles.ApplyFilter(mob)

    listMob = list()
    for c in mobFound: #itera la lista dei mob trovati
        if c.Notoriety == 3:
            listMob.append(c)
    return listMob

def AllKill(listMob):
    for mob in listMob:
        Player.ChatSay(33,"All Kill")
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(mob)
        AspettaMorto(mob)
        Misc.Pause(1000)

def CercaMorti():
    ignoreCorpo = list()
    # Filtro corpi
    corpse = Items.Filter()
    corpse.Enabled = True
    corpse.OnGround = True
    corpse.Movable = False
    corpse.RangeMax = 12
    corpse.IsCorpse = True
    corpseFound = Items.ApplyFilter(corpse)
        
    for c in corpseFound: #itera la lista dei corpi trovati
        #if c.Serial not in ignoreCorpo:
            #ignore.append(c.Serial)
        Player.PathFindTo(c.Position.X,c.Position.Y,c.Position.Z)
        Misc.Pause(2000)  
        loot(c)
    

def AspettaMorto(mobAttaccato):
    while True:
        if  Mobiles.FindBySerial(mobAttaccato.Serial) is None:
            return

def loot(corpo):
    Items.UseItemByID(0x2D23,-1)
    Target.WaitForTarget(waitForTarget, False)
    Target.TargetExecute(corpo)
    Misc.Pause(1000)
    if Target.HasTarget(): Target.Cancel()
    Items.WaitForContents(corpo, waitForContents)
    for item in corpo.Contains : #itera la lista degli oggetti nel corpo
        if item.ItemID == leatherID2: #se l'oggetto è di tipo pelle lo sposta nel backpack
            Items.Move(item,Player.Backpack, 0)
            Misc.Pause(1000)
        



def main():
    AllKill(KillaMob())
    CercaMorti()

main()