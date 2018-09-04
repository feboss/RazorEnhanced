runebook=0x40315CFB
tinkerID = 0x1EB8
cassaLavoro=0x40066CA7
martelloID=0x0FB5
ingotID = 0x1BF2
bucklerID=0x1B73

def makeTinkerTool():
    if Items.BackpackCount(tinkerID, -1)<2:
        for item in Player.Bank.Contains:
            if item.ItemID == 0x1BF2:
                Items.Move(item, Player.Backpack, 2)
                Misc.Pause(1000)
                break
        Items.UseItemByID(tinkerID,-1) #usa il tinker tool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8) # tools
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23) # tinkertool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0) # close
        Misc.Pause(100)
        
def makeMartello():
    martelliInBag=Items.BackpackCount(martelloID,-1)
    if martelliInBag<5:
        for item in Player.Bank.Contains:
            if item.ItemID == 0x1BF2:
                Items.Move(item, Player.Backpack,((5-martelliInBag)*4))
                Misc.Pause(1000)
                break
        while Items.BackpackCount(martelloID, -1)<5:      
            Items.UseItemByID(tinkerID,-1) #usa il tinker tool
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 8) # tools
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 100) # martello
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0) # close
            Misc.Pause(100)

def craftaBuckler():
    Items.UseItemByID(martelloID,-1)#mar
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 15)
    Gumps.WaitForGump(949095101, 10000)
    while(Items.BackpackCount(ingotID,-1)>=10):                     
        Gumps.SendAction(949095101, 2)  
        if Journal.Search("You have worn"):
            Journal.Clear()
            Items.UseItemByID(martelloID,-1)#mar       
        Gumps.WaitForGump(949095101, 5000)
                            
    Gumps.SendAction(949095101, 0) #exit

def goBank():
    if Target.HasTarget(): Target.Cancel()
    Journal.Clear()
    Gumps.ResetGump()
    Items.UseItem(runebook)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 29)
    Misc.Pause(2000)
    Player.ChatSay(33,"BANK")
    while not Player.Bank:
       Misc.Pause(50) 
    if Items.BackpackCount(ingotID,-1)<=10:
        for item in Player.Bank.Contains:
            if item.ItemID == 0x1BF2:
                Items.Move(item, Player.Backpack, 850)
                Misc.Pause(1000)
                break
def goBritain():
    if Target.HasTarget(): Target.Cancel()
    Journal.Clear()
    Gumps.ResetGump()
    Items.UseItem(runebook)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 23)
    Misc.Pause(2000)
def goFabbro():
    if Target.HasTarget(): Target.Cancel()
    Gumps.ResetGump()
    Items.UseItem(runebook)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, 35)
    Misc.Pause(2000)
    
def consegna():    
    Mobiles.UseMobile(0x000377D0)
    Gumps.WaitForGump(2510313894, 10000)
    for item in Player.Backpack.Contains:
        if item.ItemID==bucklerID:
            Gumps.SendAction(2510313894, 304)
            Target.WaitForTarget(10000, False)
            Target.TargetExecute(item)
            Gumps.WaitForGump(2510313894, 10000)
    Gumps.SendAction(2510313894, 0)        
    
def main():
    while True:    
        goBank()  
        makeTinkerTool()
        makeMartello()
        goFabbro()
        craftaBuckler()
        goBritain()
        consegna()
        Misc.Pause(500)
        
main()
