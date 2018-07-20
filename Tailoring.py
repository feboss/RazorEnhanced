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
gumpStuddedGloves=9
gumpStuddedSleeves=16
gumpStuddedLeggins=23
gumpStuddedTunic=30
gumpStuddedDo=44
cassaLavoro=0x40066CAA


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
            
def Crafta(sewingKitID,gumpID,itemID):
    cassaPelli=0x404A31F2
    leatherID=0x1081
    gorgetID=0x13D6
    Items.UseItemByID(sewingKitID,-1)#mar
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 50)#metalarmor
    Gumps.WaitForGump(949095101, 10000)
    Journal.Clear()
    while True:
        '''if (Player.Weight > Player.MaxWeight - 80):
            if(Items.BackpackCount(gorgetID, 0)<1):
                break'''
        if (int(((Items.GetPropStringList(Player.Backpack)[2].split('/', 1)[0]))[10:])>120):
            break
        if(Items.BackpackCount(leatherID, 0)<20):
            if(Items.BackpackCount(itemID, 0)>10):
                break
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
    glovesID=0x13D5
    sleevesID=0x13D4
    legginsID=0x13DA
    tunicID=0x13DB
    doID=0x27C7
    sewingKitID=0x0F9D
    while Player.GetSkillValue("Tailoring")>=99.6 and Player.GetSkillValue("Tailoring")<103.7:
        #makeMartello()
        #makeTinkerTool()
        Crafta(sewingKitID,gumpStuddedGorget,gorgetID)
        Taglia(gorgetID)
    while Player.GetSkillValue("Tailoring")>=103.7 and Player.GetSkillValue("Tailoring")<107.9:
        #makeMartello()
        #makeTinkerTool()
        Crafta(sewingKitID,gumpStuddedGloves,glovesID)
        Taglia(glovesID)
    while Player.GetSkillValue("Tailoring")>=107.9 and Player.GetSkillValue("Tailoring")<111.9:
        #makeMartello()
        #makeTinkerTool()
        Crafta(sewingKitID,gumpStuddedSleeves,sleevesID)
        Taglia(sleevesID)
    while Player.GetSkillValue("Tailoring")>=111.9 and Player.GetSkillValue("Tailoring")<115.9:
        #makeMartello()
        #makeTinkerTool()
        Crafta(sewingKitID,gumpStuddedLeggins,legginsID)
        Taglia(legginsID)
    while Player.GetSkillValue("Tailoring")>=115.9 and Player.GetSkillValue("Tailoring")<118.9: 
        #makeMartello()
        #makeTinkerTool()
        Crafta(sewingKitID,gumpStuddedTunic,tunicID)
        Taglia(tunicID) 
    while Player.GetSkillValue("Tailoring")>=118.9 and Player.GetSkillValue("Tailoring")<120: 
        #makeMartello()
        #makeTinkerTool()
        Crafta(sewingKitID,gumpStuddedDo,doID)
        Taglia(doID) 
main()