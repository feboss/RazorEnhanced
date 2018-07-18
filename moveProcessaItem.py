#Items.Move(0x405131CA, 0x4038DA0A, 3850)
LogID = 0x1BDD
Boards = 0x1BD7
contid = Target.PromptTarget()
cont = Items.FindBySerial(contid)
Items.WaitForContents(cont, 8000)
Misc.Pause(500)
while True:
    for item in cont.Contains:
                if item.ItemID == LogID:
                    Misc.SendMessage("--> Sposto 50 Log", 77) 
                    Items.Move(item, Player.Backpack, 100)
                    Misc.Pause(500)
                    Items.UseItem(0x4039BEA3)
                    Target.WaitForTarget(1000, False)
                    Target.TargetExecute(item)
                    Misc.Pause(500)
                    for b in Player.Backpack.Contains:
                        #Items.WaitForContents(b, 8000)
                        if b.ItemID == Boards:
                            Items.Move(b, 0x401F5896, 0)
                            Misc.Pause(500)
                    Misc.Pause(200)
                
