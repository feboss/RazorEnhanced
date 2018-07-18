'''
gorget fino a 106.4(10)
plate gloves- 106.5 - 108.9 (12)
109.0 - 116.3 producete Plate Arms 
116.4 - 118.8 producete Plate Legs
118.9 - 120.0 producete Plate Armor
'''
gorgetID=0x1413
glovesID=0x1414
armsID=0x1410
legsID=0x1411
armorID=0x1415
tinkerID = 0x1EB8
cassaLavoro=0x40066CA7
martelloID=0x0FB5
ingotID = 0x1BF2

gumpSmelta=14
gumpTools=8
gumpMartello=100
gumpTinkerTool=23
gumpPlateGorget=65 #fino a 106.4
gumpPlateGloves=58 #fino a 108.9
gumpPlateArms=51 #fino a 116.3
gumpPlateLegs=72 #fino a 118.8
gumpPlateArmor=79 #120


cassaLingotti=0x404A31F2

def makeMartello():
    xcassaLavoro = Items.FindBySerial(cassaLavoro)
    if Items.BackpackCount(martelloID, -1)<2:
        Items.UseItemByID(tinkerID,-1) #usa il tinker tool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8) # tools
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 100) # martello
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0) # close
        Misc.Pause(100)
        for item in Player.Backpack.Contains: 
            if item.ItemID == martelloID:
                Items.Move(item, cassaLavoro, 0)
                Misc.Pause(1000)
    
def makeTinkerTool():
    if Items.BackpackCount(tinkerID, -1)<2:
        Items.UseItemByID(tinkerID,-1) #usa il tinker tool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8) # tools
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23) # tinkertool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0) # close
        Misc.Pause(100)
        
        
def rifornisci():
    cassaLingottiX = Items.FindBySerial(cassaLingotti)
    for item in cassaLingottiX.Contains:
        if item.ItemID == ingotID:
            if item.Hue == 0x0000:
                Items.Move(item, Player.Backpack, 500)
                Misc.Pause(1000)

def Crafta(gumpID):
    Items.UseItemByID(martelloID,-1)#mar
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 1)#metalarmor
    Gumps.WaitForGump(949095101, 10000)
    Journal.Clear()
    while True:
        if (Player.Weight > Player.MaxWeight - 80): 
            break
        if (int(((Items.GetPropStringList(Player.Backpack)[2].split('/', 1)[0]))[10:])>120):
            break
        if(Items.BackpackCount(ingotID, 0)<500):
            rifornisci()               
        if (Journal.Search("You have worn out your tool!") or (Journal.Search("That container cannot") )):
            Items.UseItemByID(martelloID,-1)#mar
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 1)#metalarmor
            Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, gumpID)
        Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 0)#exit 

def Smelta(oggettoID):
    xcassaLavoro = Items.FindBySerial(cassaLavoro)
    Items.UseItemByID(martelloID,-1)#mar
    Gumps.WaitForGump(949095101, 10000)
    for item in xcassaLavoro.Contains:
        if item.ItemID == oggettoID:
            Gumps.SendAction(949095101, 14)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(item)#gorget
            Misc.Pause(200)
    Gumps.SendAction(949095101, 0)    
109.0 - 116.3
def main():
    rifornisci()
    while Player.GetSkillValue("Blacksmith")>=95.4 and Player.GetSkillValue("Blacksmith")<106.4:
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateGorget)
        Smelta(gorgetID)
    while Player.GetSkillValue("Blacksmith")>=106.5 and Player.GetSkillValue("Blacksmith")<108.9:
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateGloves)
        Smelta(glovesID)
    while Player.GetSkillValue("Blacksmith")>=109 and Player.GetSkillValue("Blacksmith")<116.3:
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateArms)
        Smelta(armsID)
    while Player.GetSkillValue("Blacksmith")>=116.3 and Player.GetSkillValue("Blacksmith")<118.8:
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateLegs)
        Smelta(legsID)
    while Player.GetSkillValue("Blacksmith")>=118.8 and Player.GetSkillValue("Blacksmith")<120: 
        makeMartello()
        makeTinkerTool()
        Crafta(gumpPlateArmor)
        Smelta(armorID) 
main()
