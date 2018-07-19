'''
99.6 - 103.7 : Studded Gorget
103.8 - 107.8 : Studded Gloves
107.9 - 111.9 : Studded Sleeves
112.0 - 115.9 : Studded Leggings
116.0 - 118.9 : Studded Tunic
119.0 - 120.0 : Studded Do
'''
#949095101, 50

sewingKitID=0x0F9D
gumpStuddedArmor=50
gumpStuddedGorget=2 
cassaLavoro=0x40066CAA
gumpPlateGloves=58 #fino a 108.9
gumpPlateArms=51 #fino a 116.3
gumpPlateLegs=72 #fino a 118.8
gumpPlateArmor=79 #120


def rifornisci(cassaPelli):
    leatherID=0x1081
    cassaLingottiX = Items.FindBySerial(cassaPelli)
    for item in cassaLingottiX.Contains:
        if item.ItemID == leatherID:
            if item.Hue == 0x0000:
                Items.Move(item, Player.Backpack, 50)
                Misc.Pause(1000)
                
def Taglia(oggettoID):
    xcassaLavoro = Items.FindBySerial(cassaLavoro)
    for item in xcassaLavoro.Contains:
        if item.ItemID == oggettoID:
            Items.UseItem(0x4004C98D)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(item)
            
def Crafta(sewingKitID,gumpID):
    cassaPelli=0x404A31F2
    leatherID=0x1081
    gorgetID=0x13D6
    Items.UseItemByID(sewingKitID,-1)#mar
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 50)#metalarmor
    Gumps.WaitForGump(949095101, 10000)
    Journal.Clear()
    while True:
        if (Player.Weight > Player.MaxWeight - 80): 
            break
        if (int(((Items.GetPropStringList(Player.Backpack)[2].split('/', 1)[0]))[10:])>120):
            break
        if(Items.BackpackCount(leatherID, 0)<20):
            if(Items.BackpackCount(gorgetID, 0)>10):
                Taglia(gorgetID)
            else:
                rifornisci(cassaPelli)               
        if (Journal.Search("You have worn out your tool!") or (Journal.Search("That container cannot") )):
            Items.UseItemByID(sewingKitID,-1)#mar
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 50)#metalarmor
            Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, gumpID)
        Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 0)#exit 


def main():
    cassaPelli=0x404A31F2
    gorgetID=0x13D6
    sewingKitID=0x0F9D
    while Player.GetSkillValue("Tailoring")>=99.6 and Player.GetSkillValue("Tailoring")<103.7:
        #makeMartello()
        #makeTinkerTool()
        Crafta(sewingKitID,gumpStuddedGorget)
        Taglia(gorgetID)
    '''while Player.GetSkillValue("Tailoring")>=103.7 and Player.GetSkillValue("Tailoring")<107.9:
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateGloves)
        Smelta(glovesID)
    while Player.GetSkillValue("Tailoring")>=107.9 and Player.GetSkillValue("Tailoring")<111.9:
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateArms)
        Smelta(armsID)
    while Player.GetSkillValue("Tailoring")>=111.9 and Player.GetSkillValue("Tailoring")<115.9:
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateLegs)
        Smelta(legsID)
    while Player.GetSkillValue("Tailoring")>=115.9 and Player.GetSkillValue("Tailoring")<118.9: 
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateArmor)
        Smelta(armorID) 
    while Player.GetSkillValue("Tailoring")>=118.9 and Player.GetSkillValue("Tailoring")<120: 
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateArmor)
        Smelta(armorID) '''
main()