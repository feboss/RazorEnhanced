##====== RuneBook cloner ======##======================================
## Piattaforma: Razor Enhanced
## Autore: Giocos
## Versione: 0.1
## Shard: UODreams
##=============================##======================================
## I nomi degli spot delle rune NON devono inziare per un numero 
## All'avvio tutte le rune, se presenti, nella root del backpack 
## verranno trasferite all'interno della bag e sovrascritte.
##=============================##======================================
## roadmap
## --- copia di runebook delle biblioteche
## --- Se non hai rune andare dal vendor e comprarne una 20ina
## --- Undress del pg e attivazione meditation al recupero mana
## --- Attivazione lichform se si ha necro
## --- Drop di tutte le rune presenti nel runebook che dovrebbe essere vergine
## --- Grafica
##=============================##======================================
## Serve: 
## -runebook da copiare
## -runebook vergine
## -bag vuota dove andremo a inserire le rune vuote
## ---rune vuote nel backpack o dentro la bag
##=============================##======================================

def checkMana():
    minmana = 30
    manaPause = 10000
    while (Player.Mana < minmana):
        Misc.SendMessage("Mana sotto la soglia. Wait...", 80)
        Misc.Pause(manaPause)
    return ;   
#######################################
#######################################
def getNumRuneRunebook(runeBookSerial):
    return len(pulizia(runeBookSerial))
#######################################
def pulizia(runeBookSerial): 
    Items.UseItem(runeBookSerial)
    Gumps.WaitForGump(1431013363, 3000)
    Misc.Pause(100)
    listaBook = Gumps.LastGumpGetLineList( )
    newListaBook = []
    for x in listaBook:
        if not (x[0].isnumeric()) and not (x.isnumeric()) and (x != "Empty") and (x != "Gate Travel") and (x != "Charges: ") and (x != "Max Charges: ") and (x != "Rename book") and (x != "Sacred Journey") and (x != "Set default") and (x != "Recall") and (x != "Drop rune") :
            newListaBook.append(x)
    if Target.HasTarget(): Target.Cancel() 
    return newListaBook  
#######################################
def recalla(runeBookDaCopiare,num):
    wait = 1000
    recallPause=2000
    checkMana()
    Items.UseItem(runeBookDaCopiare)
    Gumps.WaitForGump(1431013363, wait)
    listGump = Gumps.LastGumpGetLineList( )
    Misc.Pause(2000)
    Gumps.SendAction(1431013363, num * 6 -1)
    Misc.Pause(recallPause)
    Gumps.ResetGump()
    return listGump
#######################################    
def marka(runa):
    wait = 3000
    markPause=1000
    checkMana()
    Misc.Pause(wait)
    Spells.CastMagery("Mark")
    Target.WaitForTarget(wait)
    Target.TargetExecute(runa)
    Misc.Pause(markPause)
####################################### 
def getGump(runeBookDaCopiare):
    Items.UseItem(runeBookDaCopiare)
    Misc.Pause(2000)
    return Gumps.LastGumpGetLineList( )
####################################### 
def muoviRune(bagRune):
    Misc.SendMessage("Sposto le rune nella bag", 82)
    runaID = 0x1F14
    dragDelay = 500
    for item in Player.Backpack.Contains:
        if item.ItemID == runaID:
            Items.Move(item,bagRune,0)
            Misc.Pause(dragDelay)
            Misc.SendMessage("Spostamento rune completato", 82)
 
####################################### 
############MAIN######################
####################################### 
runaID = 0x1F14

Misc.SendMessage('Targetta il runebook da copiare', 50)
runeBookDaCopiare = Target.PromptTarget() 

Misc.SendMessage('Targetta la bag con le rune', 50)
bagRune = Target.PromptTarget()
bagRune = Items.FindBySerial(bagRune)

Misc.SendMessage('Targetta il runebook VERGINE', 50)
runeBookVergine = Target.PromptTarget()

muoviRune(bagRune)

listaSpot = pulizia(runeBookDaCopiare)
Misc.SendMessage("DEBUG:" +str(len(listaSpot)),33)
for x in range(len(listaSpot)/2):
    Misc.SendMessage("--> Racall to -> " +listaSpot[x], 80)
    recalla(runeBookDaCopiare,x+1)
    for item in bagRune.Contains:
        if item.ItemID == runaID:
            Misc.SendMessage("--> Marko -> " +listaSpot[x], 80)
            marka(item)
            Items.UseItem(item)
            Misc.Pause(100)
            Misc.ResponsePrompt(listaSpot[x])
            Items.Move(item,runeBookVergine,0)
            Misc.Pause(1000)
            Misc.SendMessage("--> Runa inserita nel nuovo Runebook -> " +listaSpot[x], 80)
            break      