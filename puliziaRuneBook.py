Misc.SendMessage('Targetta il runebook', 82)
runeBookDaCopiare = Target.PromptTarget() 
Items.UseItem(runeBookDaCopiare)
Gumps.WaitForGump(1431013363, 2000)
Misc.Pause(500)
stringaGump = Gumps.LastGumpGetLineList( )

newList = []
for x in stringaGump:
    if not (x[0].isnumeric()) and not (x.isnumeric()) and (x != "Empty") and (x != "Gate Travel") and (x != "Charges: ") and (x != "Max Charges: ") and (x != "Rename book") and (x != "Sacred Journey") and (x != "Set default") and (x != "Recall") and (x != "Drop rune") :
        newList.append(x)

if Target.HasTarget(): Target.Cancel()   