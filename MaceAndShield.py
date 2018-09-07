'''
The script: 
go to the bank <--- get the iron
craft blacksmith hammer and tinker tools if need
go to the forge <--- craft buckler
go to Britain library ---> give buckler

What you need:
    1 runebook with 3 rune
    Rune Bank
    Rune Forge
    Rune Britain(close to the npc)
    Skill tinker
    Skill blacksmith
    Skill Magery


!!! Have no check for no mana or no reagents or fizzles, so be sure to have enough LRC and magery skill
    Miss also the check for Rune Blocked. so be sure to choice a spot that is no busy at all
    
'''

########
runebook=0x40315CFB
runaBanca=5
runaFabbro=6
runaBritain=4
#######


tinkerID = 0x1EB8
martelloID=0x13E3
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
            Gumps.SendAction(949095101, 93) # martello
            Gumps.WaitForGump(949095101, 10000)
            Gumps.SendAction(949095101, 0) # close
            Misc.Pause(100)

def craftaBuckler():
    Items.UseItemByID(martelloID,-1)#mar
    Gumps.WaitForGump(949095101, 10000)
    Gumps.SendAction(949095101, 15)
    Gumps.WaitForGump(949095101, 10000)
    if Items.BackpackCount(ingotID,-1)<10:#Se non crafti
        Misc.Pause(1500)
    while(Items.BackpackCount(ingotID,-1)>=10):                     
        Gumps.SendAction(949095101, 2)  
        if Journal.Search("You have worn"):
            Journal.Clear()
            Items.UseItemByID(martelloID,-1)#mar       
        Gumps.WaitForGump(949095101, 5000)                            
    Gumps.SendAction(949095101, 0) #exit
    if Target.HasTarget: Target.Cancel()

def goBank():
    numeroScudi=((Player.MaxWeight-Player.Weight)/5-1-10+Items.BackpackCount(0x13E3,-1)*2)
    recall(runebook,runaBanca)
    while not Journal.Search("Bank container has"):
        Player.ChatSay(52, "bank")
        Misc.Pause(200)
    while Items.BackpackCount(ingotID,-1)<numeroScudi*10:
        for item in Player.Bank.Contains:
            if item.ItemID == 0x1BF2:
                Items.Move(item, Player.Backpack, numeroScudi*10-Items.BackpackCount(ingotID,-1) )
                Misc.Pause(2000)
                break
    else:
        Misc.Pause(2000)
def goBritain():
    recall(runebook,runaBritain)
def goFabbro():
    recall(runebook,runaFabbro)
    
def consegna():
    while not Mobiles.FindBySerial(0x000377D0): Misc.Pause(50)
    while not Gumps.HasGump( ):
        Mobiles.UseMobile(0x000377D0)
        Gumps.WaitForGump(2510313894, 10000)
    if Items.BackpackCount(bucklerID,-1)<10:
        Misc.Pause(1500)
    for item in Player.Backpack.Contains:
        if item.ItemID==bucklerID:
            Gumps.SendAction(2510313894, 304)
            Target.WaitForTarget(10000)
            Target.TargetExecute(item)
            Gumps.WaitForGump(2510313894, 10000)            
    Gumps.SendAction(2510313894, 0)
    if Target.HasTarget: Target.Cancel()

def recall(runebook,runa):
    x=Player.Position.X
    y=Player.Position.Y
    Journal.Clear()
    Gumps.ResetGump()
    Items.UseItem(runebook)
    Gumps.WaitForGump(1431013363, 10000)
    Gumps.SendAction(1431013363, runa*6-1)
    while Player.Position.X == x and Player.Position.Y == y:
        Misc.Pause(100)
    Misc.Pause(50)    
    
def main():
    while True:    
        goBank()  
        makeTinkerTool()
        makeMartello()
        goFabbro()
        craftaBuckler()
        goBritain()
        consegna()     
main()       
