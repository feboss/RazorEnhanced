import clr
clr.AddReference("System")
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
import thread
import cPickle as pickle

####################################
######### Variabili Sistema#########
####################################
pickaxeID = 0x0E86
tinkerID = 0x1EB8
lastrune = 5
RecallPause = 4500
DragDelay = 1200
TimeoutOnWaitAction = 10000
WeightLimit = Player.MaxWeight - 80
noLrc = "More reagents are needed for this spell"
noMana = "Insufficient mana for this spell"
noPickaxe = "You have worn out your tool!"
locationBlocked = "that location is blocked"
noMetal = "There is no metal here to mine"
youcant = "You can't mine there"
cantseen = "Target cannot be seen"

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self.settings = { 
                        "RuneBookBanca" : None,
                        "RuneBookMining" : list(),
                        "MineBag" : None,
                        "MineBag2" : None,
                        "PosizioneRunaCasa" : None,
                        "FireBeetle" : None,
                        "Posizione" : None
                        }
        self._label_posizioneRuna = System.Windows.Forms.Label()
        self._groupBox_minebook = System.Windows.Forms.GroupBox()
        self._button_delListaRunebook = System.Windows.Forms.Button()
        self._listBox_Runebook = System.Windows.Forms.ListBox()
        self._button_addListaRunebook = System.Windows.Forms.Button()
        self._groupBox_runebookCasa = System.Windows.Forms.GroupBox()
        self._button_runeBookCasa = System.Windows.Forms.Button()
        self._numericUpDown1 = System.Windows.Forms.NumericUpDown()
        self._label_runebookCasa = System.Windows.Forms.Label()
        self._groupBox_casa = System.Windows.Forms.GroupBox()
        self._button_position = System.Windows.Forms.Button()
        self._button_lingotti = System.Windows.Forms.Button()
        self._button_gemme = System.Windows.Forms.Button()
        self._label_position = System.Windows.Forms.Label()
        self._label_lingotti = System.Windows.Forms.Label()
        self._label_gemme = System.Windows.Forms.Label()
        self._groupBox_pet = System.Windows.Forms.GroupBox()
        self._button_fireBeetle = System.Windows.Forms.Button()
        self._label_fireBeetle = System.Windows.Forms.Label()
        self._groupBox_output = System.Windows.Forms.GroupBox()
        self._textBox_output = System.Windows.Forms.TextBox()
        self._button_Run = System.Windows.Forms.Button()
        self._groupBox_extra = System.Windows.Forms.GroupBox()
        self._button_daiCibo = System.Windows.Forms.Button()
        self._button_scarico = System.Windows.Forms.Button()
        self._button_smelta = System.Windows.Forms.Button()
        self._groupBox_minebook.SuspendLayout()
        self._groupBox_runebookCasa.SuspendLayout()
        self._groupBox_casa.SuspendLayout()
        self._groupBox_pet.SuspendLayout()
        self._groupBox_output.SuspendLayout()
        self._groupBox_extra.SuspendLayout()
        self.SuspendLayout()
        # 
        # label_posizioneRuna
        # 
        self._label_posizioneRuna.Location = System.Drawing.Point(6, 13)
        self._label_posizioneRuna.Name = "label_posizioneRuna"
        self._label_posizioneRuna.Size = System.Drawing.Size(127, 23)
        self._label_posizioneRuna.TabIndex = 0
        self._label_posizioneRuna.Text = "Posizione runa:"
        self._label_posizioneRuna.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # groupBox_minebook
        # 
        self._groupBox_minebook.Controls.Add(self._button_delListaRunebook)
        self._groupBox_minebook.Controls.Add(self._listBox_Runebook)
        self._groupBox_minebook.Controls.Add(self._button_addListaRunebook)
        self._groupBox_minebook.Location = System.Drawing.Point(12, 12)
        self._groupBox_minebook.Name = "groupBox_minebook"
        self._groupBox_minebook.Size = System.Drawing.Size(208, 127)
        self._groupBox_minebook.TabIndex = 6
        self._groupBox_minebook.TabStop = False
        self._groupBox_minebook.Text = "Runebook"
        # 
        # button_delListaRunebook
        # 
        self._button_delListaRunebook.AccessibleName = ""
        self._button_delListaRunebook.Location = System.Drawing.Point(139, 91)
        self._button_delListaRunebook.Name = "button_delListaRunebook"
        self._button_delListaRunebook.Size = System.Drawing.Size(63, 25)
        self._button_delListaRunebook.TabIndex = 2
        self._button_delListaRunebook.Text = "Cancella"
        self._button_delListaRunebook.UseVisualStyleBackColor = True
        self._button_delListaRunebook.Click += self.Button_delListaRunebookClick
        # 
        # listBox_Runebook
        # 
        self._listBox_Runebook.FormattingEnabled = True
        self._listBox_Runebook.ImeMode = System.Windows.Forms.ImeMode.Hangul
        self._listBox_Runebook.Location = System.Drawing.Point(6, 19)
        self._listBox_Runebook.Name = "listBox_Runebook"
        self._listBox_Runebook.Size = System.Drawing.Size(127, 95)
        self._listBox_Runebook.TabIndex = 0
        # 
        # button_addListaRunebook
        # 
        self._button_addListaRunebook.AccessibleName = ""
        self._button_addListaRunebook.Location = System.Drawing.Point(139, 62)
        self._button_addListaRunebook.Name = "button_addListaRunebook"
        self._button_addListaRunebook.Size = System.Drawing.Size(63, 25)
        self._button_addListaRunebook.TabIndex = 1
        self._button_addListaRunebook.Text = "Aggiungi"
        self._button_addListaRunebook.UseVisualStyleBackColor = True
        self._button_addListaRunebook.Click += self.Button_addListaRunebookClick
        # 
        # groupBox_runebookCasa
        # 
        self._groupBox_runebookCasa.Controls.Add(self._label_runebookCasa)
        self._groupBox_runebookCasa.Controls.Add(self._button_runeBookCasa)
        self._groupBox_runebookCasa.Controls.Add(self._label_posizioneRuna)
        self._groupBox_runebookCasa.Controls.Add( self._numericUpDown1)
        self._groupBox_runebookCasa.Location = System.Drawing.Point(12, 145)
        self._groupBox_runebookCasa.Name = "groupBox_runebookCasa"
        self._groupBox_runebookCasa.Size = System.Drawing.Size(208, 77)
        self._groupBox_runebookCasa.TabIndex = 22
        self._groupBox_runebookCasa.TabStop = False
        self._groupBox_runebookCasa.Text = "Runebook Casa"
        # 
        # button_runeBookCasa
        # 
        self._button_runeBookCasa.AccessibleName = ""
        self._button_runeBookCasa.Location = System.Drawing.Point(139, 40)
        self._button_runeBookCasa.Name = "button_runeBookCasa"
        self._button_runeBookCasa.Size = System.Drawing.Size(63, 25)
        self._button_runeBookCasa.TabIndex = 22
        self._button_runeBookCasa.Text = "Imposta"
        self._button_runeBookCasa.UseVisualStyleBackColor = True
        self._button_runeBookCasa.Click += self.Button_runeBookCasaClick
        # 
        #  numericUpDown1
        # 
        self._numericUpDown1.Location = System.Drawing.Point(139, 16)
        self._numericUpDown1.Name = "domainUpDown1"
        self._numericUpDown1.Size = System.Drawing.Size(37, 20)
        self._numericUpDown1.TabIndex = 3
        self._numericUpDown1.Maximum = 12
        self._numericUpDown1.Minimum = 1
        # 
        # label_runebookCasa
        # 
        self._label_runebookCasa.Location = System.Drawing.Point(6, 42)
        self._label_runebookCasa.Margin = System.Windows.Forms.Padding(0)
        self._label_runebookCasa.Name = "label_runebookCasa"
        self._label_runebookCasa.Size = System.Drawing.Size(127, 23)
        self._label_runebookCasa.TabIndex = 23
        self._label_runebookCasa.Text = "Runebook Casa:"
        self._label_runebookCasa.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # groupBox_casa
        # 
        self._groupBox_casa.Controls.Add(self._label_gemme)
        self._groupBox_casa.Controls.Add(self._label_lingotti)
        self._groupBox_casa.Controls.Add(self._label_position)
        self._groupBox_casa.Controls.Add(self._button_position)
        self._groupBox_casa.Controls.Add(self._button_lingotti)
        self._groupBox_casa.Controls.Add(self._button_gemme)
        self._groupBox_casa.Location = System.Drawing.Point(12, 230)
        self._groupBox_casa.Name = "groupBox_casa"
        self._groupBox_casa.Size = System.Drawing.Size(208, 116)
        self._groupBox_casa.TabIndex = 23
        self._groupBox_casa.TabStop = False
        self._groupBox_casa.Text = "Casa"
        # 
        # button_position
        # 
        self._button_position.AccessibleName = ""
        self._button_position.Location = System.Drawing.Point(139, 14)
        self._button_position.Name = "button_position"
        self._button_position.Size = System.Drawing.Size(63, 25)
        self._button_position.TabIndex = 3
        self._button_position.Text = "Set"
        self._button_position.UseVisualStyleBackColor = True
        self._button_position.Click += self.Button_positionClick
        # 
        # button_lingotti
        # 
        self._button_lingotti.AccessibleName = ""
        self._button_lingotti.Location = System.Drawing.Point(139, 45)
        self._button_lingotti.Name = "button_lingotti"
        self._button_lingotti.Size = System.Drawing.Size(63, 25)
        self._button_lingotti.TabIndex = 7
        self._button_lingotti.Text = "Imposta"
        self._button_lingotti.UseVisualStyleBackColor = True
        self._button_lingotti.Click += self.Button_lingottiClick
        # 
        # button_gemme
        # 
        self._button_gemme.AccessibleName = ""
        self._button_gemme.Location = System.Drawing.Point(139, 76)
        self._button_gemme.Name = "button_gemme"
        self._button_gemme.Size = System.Drawing.Size(63, 25)
        self._button_gemme.TabIndex = 9
        self._button_gemme.Text = "Imposta"
        self._button_gemme.UseVisualStyleBackColor = True
        self._button_gemme.Click += self.Button_gemmeClick
        # 
        # label_position
        # 
        self._label_position.Location = System.Drawing.Point(6, 14)
        self._label_position.Name = "label_position"
        self._label_position.Size = System.Drawing.Size(127, 23)
        self._label_position.TabIndex = 24
        self._label_position.Text = "Posizione di scarico"
        self._label_position.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label_lingotti
        # 
        self._label_lingotti.Location = System.Drawing.Point(6, 47)
        self._label_lingotti.Name = "label_lingotti"
        self._label_lingotti.Size = System.Drawing.Size(127, 23)
        self._label_lingotti.TabIndex = 25
        self._label_lingotti.Text = "Cassa lingotti:"
        self._label_lingotti.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label_gemme
        # 
        self._label_gemme.Location = System.Drawing.Point(6, 76)
        self._label_gemme.Name = "label_gemme"
        self._label_gemme.Size = System.Drawing.Size(127, 23)
        self._label_gemme.TabIndex = 26
        self._label_gemme.Text = "Cassa gemme:"
        self._label_gemme.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # groupBox_pet
        # 
        self._groupBox_pet.Controls.Add(self._label_fireBeetle)
        self._groupBox_pet.Controls.Add(self._button_fireBeetle)
        self._groupBox_pet.Location = System.Drawing.Point(12, 352)
        self._groupBox_pet.Name = "groupBox_pet"
        self._groupBox_pet.Size = System.Drawing.Size(208, 50)
        self._groupBox_pet.TabIndex = 24
        self._groupBox_pet.TabStop = False
        self._groupBox_pet.Text = "Pet"
        # 
        # button_fireBeetle
        # 
        self._button_fireBeetle.AccessibleName = ""
        self._button_fireBeetle.Location = System.Drawing.Point(139, 14)
        self._button_fireBeetle.Name = "button_fireBeetle"
        self._button_fireBeetle.Size = System.Drawing.Size(63, 25)
        self._button_fireBeetle.TabIndex = 17
        self._button_fireBeetle.Text = "Imposta"
        self._button_fireBeetle.UseVisualStyleBackColor = True
        self._button_fireBeetle.Click += self.Button_fireBeetleClick
        # 
        # label_fireBeetle
        # 
        self._label_fireBeetle.Location = System.Drawing.Point(6, 16)
        self._label_fireBeetle.Name = "label_fireBeetle"
        self._label_fireBeetle.Size = System.Drawing.Size(127, 23)
        self._label_fireBeetle.TabIndex = 27
        self._label_fireBeetle.Text = "Fire Beetle"
        self._label_fireBeetle.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # groupBox_output
        # 
        self._groupBox_output.Controls.Add(self._textBox_output)
        self._groupBox_output.Location = System.Drawing.Point(226, 12)
        self._groupBox_output.Name = "groupBox_output"
        self._groupBox_output.Size = System.Drawing.Size(232, 431)
        self._groupBox_output.TabIndex = 25
        self._groupBox_output.TabStop = False
        self._groupBox_output.Text = "Output"
        # 
        # textBox_output
        # 
        self._textBox_output.Location = System.Drawing.Point(6, 14)
        self._textBox_output.Multiline = True
        self._textBox_output.Name = "textBox_output"
        self._textBox_output.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        self._textBox_output.Size = System.Drawing.Size(220, 411)
        self._textBox_output.TabIndex = 2
        # 
        # button_Run
        # 
        self._button_Run.AccessibleName = ""
        self._button_Run.BackColor = System.Drawing.SystemColors.ControlLight
        self._button_Run.Location = System.Drawing.Point(272, 449)
        self._button_Run.Name = "button_Run"
        self._button_Run.Size = System.Drawing.Size(134, 32)
        self._button_Run.TabIndex = 28
        self._button_Run.Text = "Run"
        self._button_Run.UseVisualStyleBackColor = True
        self._button_Run.Click += self.Button_RunClick
        # 
        # groupBox_extra
        # 
        self._groupBox_extra.Controls.Add(self._button_smelta)
        self._groupBox_extra.Controls.Add(self._button_scarico)
        self._groupBox_extra.Controls.Add(self._button_daiCibo)
        self._groupBox_extra.Location = System.Drawing.Point(12, 408)
        self._groupBox_extra.Name = "groupBox_extra"
        self._groupBox_extra.Size = System.Drawing.Size(208, 79)
        self._groupBox_extra.TabIndex = 28
        self._groupBox_extra.TabStop = False
        self._groupBox_extra.Text = "Funzioni Extra"
        # 
        # button_daiCibo
        # 
        self._button_daiCibo.AccessibleName = ""
        self._button_daiCibo.Location = System.Drawing.Point(6, 19)
        self._button_daiCibo.Name = "button_daiCibo"
        self._button_daiCibo.Size = System.Drawing.Size(63, 25)
        self._button_daiCibo.TabIndex = 17
        self._button_daiCibo.Text = "Sfama pet"
        self._button_daiCibo.UseVisualStyleBackColor = True
        self._button_daiCibo.Click += self.Button_daiCiboClick
        # 
        # button_scarico
        # 
        self._button_scarico.AccessibleName = ""
        self._button_scarico.Location = System.Drawing.Point(70, 19)
        self._button_scarico.Name = "button_scarico"
        self._button_scarico.Size = System.Drawing.Size(63, 25)
        self._button_scarico.TabIndex = 29
        self._button_scarico.Text = "Scarica"
        self._button_scarico.UseVisualStyleBackColor = True
        self._button_scarico.Click += self.Button_scaricoClick
        # 
        # button_smelta
        # 
        self._button_smelta.AccessibleName = ""
        self._button_smelta.Location = System.Drawing.Point(135, 19)
        self._button_smelta.Name = "button_smelta"
        self._button_smelta.Size = System.Drawing.Size(63, 25)
        self._button_smelta.TabIndex = 30
        self._button_smelta.Text = "Smelta"
        self._button_smelta.UseVisualStyleBackColor = True
        self._button_smelta.Click += self.Button_smeltaClick
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(470, 499)
        self.Controls.Add(self._groupBox_extra)
        self.Controls.Add(self._button_Run)
        self.Controls.Add(self._groupBox_output)
        self.Controls.Add(self._groupBox_pet)
        self.Controls.Add(self._groupBox_casa)
        self.Controls.Add(self._groupBox_runebookCasa)
        self.Controls.Add(self._groupBox_minebook)
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
        self.Name = "MainForm"
        self.Text = "GiocoMiner 0.5"
        self.TopMost = True
        self._groupBox_minebook.ResumeLayout(False)
        self._groupBox_runebookCasa.ResumeLayout(False)
        self._groupBox_casa.ResumeLayout(False)
        self._groupBox_pet.ResumeLayout(False)
        self._groupBox_output.ResumeLayout(False)
        self._groupBox_output.PerformLayout()
        self._groupBox_extra.ResumeLayout(False)
        self.ResumeLayout(False)
        self._numericUpDown1.EndInit()

    def Button_addListaRunebookClick(self, sender, e):
        self.settings["RuneBookMining"].append(Target.PromptTarget())
        self._listBox_Runebook.Items.Add(self.settings["RuneBookMining"][-1])

    def Button_delListaRunebookClick(self, sender, e):
        selectedIndex = self._listBox_Runebook.SelectedIndex
        self._listBox_Runebook.Items.RemoveAt(selectedIndex)
        self.settings["RuneBookMining"].pop(selectedIndex)
              
    def Button_runeBookCasaClick(self, sender, e):
        self.settings["RuneBookBanca"] = Target.PromptTarget()
        self._textBox_output.AppendText("Runebook Casa impostata!\n")

    def Button_positionClick(self, sender, e):
        self.settings["PosizioneX"] = Player.Position.X
        self.settings["PosizioneY"] = Player.Position.Y
        self.settings["PosizioneZ"] = Player.Position.Z
        self._textBox_output.AppendText("Posizione di lavoro impostata!\n")

    def Button_lingottiClick(self, sender, e):
        self.settings["MineBag1"] = Target.PromptTarget()
        self._textBox_output.AppendText("Cassa lingotti impostata!\n")

    def Button_gemmeClick(self, sender, e):
        self.settings["MineBag2"] = Target.PromptTarget()
        self._textBox_output.AppendText("Cassa gemma impostata!\n")

    def Button_fireBeetleClick(self, sender, e):
        self.settings["FireBeetle"] = Target.PromptTarget()
        self._textBox_output.AppendText("Fire Beetle impostato!\n")

    def Button_daiCiboClick(self, sender, e):
        dismount()
        giveFood(self.settings["FireBeetle"])

    def Button_scaricoClick(self, sender, e):
        pass

    def Button_smeltaClick(self, sender, e):
        dismount()
        smelta(settings["FireBeetle"])

    def Button_RunClick(self, sender, e):
        self.settings["NumRunaCasa"] = self._numericUpDown1.Value
        SaveSettings(**self.settings)
        thread.start_new_thread(main, (self, ), (self.settings))
        #main(self,**self.settings)

    def writeTextBox(self,stringa):
        stringa = str(stringa)
        self._textBox_output.AppendText((stringa + "\n"))
         
    def ReadSettings(self):
        try:
            with open("GiocoMinerSettings3.txt") as in_file:
                self.writeTextBox("File impostazioni trovato.Carico...")
                self.writeTextBox("Le impostazioni vengono salvate in automatico al RUN.")
                my_lines = in_file.readlines()
                self.settings["RuneBookMining"] = my_lines[0].strip() 
                self.settings["RuneBookMining"] = self.settings["RuneBookMining"].split("-") #split at -
                self.settings["RuneBookMining"].pop(len(self.settings["RuneBookMining"])-1) #delete last string after the - that is void
                self.settings["RuneBookMining"] = map(int, self.settings["RuneBookMining"]) #trasformiamo tutto in int
                self.settings["RuneBookBanca"] = int(my_lines[1].strip())
                self.settings["NumRunaCasa"] = int(my_lines[2])
                self.settings["PosizioneX"] = int(my_lines[3])
                self.settings["PosizioneY"] = int(my_lines[4])
                self.settings["PosizioneZ"] = int(my_lines[5])
                self.settings["MineBag1"] = int(my_lines[6].strip())
                self.settings["MineBag2"] = int(my_lines[7].strip())
                self.settings["FireBeetle"] = int(my_lines[8].strip())
                self._numericUpDown1.Value = self.settings["NumRunaCasa"]
                for runebookmining in self.settings["RuneBookMining"]:
                    self._listBox_Runebook.Items.Add(runebookmining)
                #self._listBox_Runebook.Items.Add(self.settings["RuneBookMining"][-1])
        except IOError:
            self.writeTextBox("File impostazioni NON TROVATO!!!")
            self.writeTextBox("Imposta le varie cose e poi runna il programma")
            self.writeTextBox("Non Dimenticarti NULLA!!!!")

def createFood(cibo):    
    listaCibo=["sausage","cut of ribs","a ham","a cooked bird","a wedge of cheese","a peach","an apple","a fish steak","a grape bunch","muffins"]
    for xcibo in cibo:
        listaCibo.remove(xcibo)
    Journal.Clear()
    repeat = True
    while repeat:
        timeout=10000 
        Spells.CastMagery("Create Food")
        while timeout>0 and repeat: 
            for food in cibo:
                if Journal.Search(food):
                    moveFood()
                    return
            if repeat:
                for food in listaCibo:
                    if Journal.Search(food):
                        Misc.Pause(1500)
                        createFood(cibo)
            timeout-=100
            Misc.Pause(50)
               
def moveFood():
    NoFoodID = [0x097D, 0x09D2, 0x09D0, 0x09D1, 0x09EB, 0x097B]
    for item in Player.Backpack.Contains:
        for xfoodID in NoFoodID: 
            if item.ItemID == xfoodID:
                Items.WaitForContents(item, TimeoutOnWaitAction)
                form.writeTextBox("Butto cibo a terra")
                Items.DropItemGroundSelf(item, 0)
                Misc.Pause(DragDelay)
   
def giveFood(FireBeetle):
    SiFoodID = [0x09C9, 0x09F2, 0x09B7, 0x09C0]
    for item in Player.Backpack.Contains:        
        for petfood in SiFoodID:
            if item.ItemID == petfood:
                Items.WaitForContents(item, TimeoutOnWaitAction)
                Items.Move(item, FireBeetle, 0)
                Misc.Pause(DragDelay)
                return
    createFood(["sausage","cut of ribs","a ham","a cooked bird"])
    giveFood(FireBeetle)
        
   
def smelta(FireBeetle): 
    oreID = [0x19B7, 0x19B8, 0x19B9, 0x19BA]  
    if Player.Weight >= WeightLimit - 130:
        form.writeTextBox("Fammi Smeltare...")
        if Target.HasTarget(): Target.Cancel()
        for item in Player.Backpack.Contains:            
            for xoreID in oreID:
                if item.ItemID == xoreID:
                    Items.WaitForContents(item, TimeoutOnWaitAction)
                    if(item.Weight >=4):
                        Items.WaitForContents(item, TimeoutOnWaitAction)                       
                        Items.UseItem(item)
                        Target.WaitForTarget(TimeoutOnWaitAction,False)
                        Target.TargetExecute(FireBeetle)
                        Misc.Pause(200)
        form.writeTextBox("Il piccolo ha sciolto tutto")
   
def dismount():
    form.writeTextBox("Dismount dal beetle")
    io = Mobiles.FindBySerial(Player.Serial)
    Mobiles.UseMobile(io)
   
def waitForMana():
    minmana = 30
    manaPause = 10000
    while (Player.Mana < minmana):
        form.writeTextBox("Mana sotto la soglia. Aspetta...")
        Misc.Pause(manaPause)
   
def MakePickaxe():
    if Items.BackpackCount(tinkerID, -1) == 0:
        form.writeTextBox("ERRORE: Non hai il Tinker Tool. Vallo a comprare e ricominciamo")
        return
    if Items.BackpackCount(pickaxeID, -1) >= 5: ####DASISTEMARE
        return
    else:
        Items.UseItemByID(tinkerID,-1) #usa il tinker tool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8) # tools
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 114) # pickaxe
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0) # close
        form.writeTextBox("Ho costruito un Piccone. Quanto so bravo?")
           
def MakeTinkerTool():
    if Items.BackpackCount(tinkerID, -1) < 2:
        Items.UseItemByID(tinkerID,-1) #usa il tinker tool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 8) # tools
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 23) # tinkertool
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 0) # close
        form.writeTextBox("Ho costruito un Tinker Tool... Quanto so bravo?")
   
def Scarico(lastrune,**settings):
    gemmaID = [0x3195, 0x3193, 0x3194, 0x3192, 0x3198, 0x3197]
    ingotID = 0x1BF2
    RuneBookCasa=settings["RuneBookBanca"]
    PosizioneRunaCasa=settings["NumRunaCasa"]
    MineBag1=settings["MineBag1"]
    MineBag2=settings["MineBag2"]
    if Player.Weight >= WeightLimit - 120:
        form.writeTextBox("Sono un pò appesantito. Vado a scaricare")
        if Target.HasTarget(): Target.Cancel()
        Journal.Clear()
        waitForMana()
        while True:
            Gumps.ResetGump()
            Items.UseItem(RuneBookCasa)
            Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
            Gumps.SendAction(1431013363, PosizioneRunaCasa*6-1)
            Misc.Pause(RecallPause)
            if not (Journal.Search(noLrc) or Journal.Search(noMana)):
                break
        Player.PathFindTo(settings["PosizioneX"], settings["PosizioneY"], settings["PosizioneZ"])
        Misc.Pause(400)
        for item in Player.Backpack.Contains:
            if item.ItemID == ingotID:
                Items.WaitForContents(item, TimeoutOnWaitAction)
                form.writeTextBox("--> Sposto lingotti")
                Items.Move(item, MineBag1, 0)
                Misc.Pause(DragDelay)
        for item in Player.Backpack.Contains:
            for xgemmaID in gemmaID:
                if item.ItemID == xgemmaID:
                    Items.WaitForContents(item, TimeoutOnWaitAction)
                    form.writeTextBox("--> Sposto gemme")
                    Items.Move(item, MineBag2, 0)
                    Misc.Pause(DragDelay)       
        form.writeTextBox("Ho scaricato tutto. Adesso si che mi sento bene")
        if lastrune !=5:
            return lastrune - 6
    return lastrune
   
def RecallNextSpot(RuneBookMining1,lastrune):
    if Target.HasTarget(): Target.Cancel()
    Journal.Clear()
    while True:
        Gumps.ResetGump()
        form.writeTextBox("Recallo al prossimo spot")
        Items.UseItem(RuneBookMining1)
        Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
        Gumps.SendAction(1431013363, lastrune)
        Misc.Pause(RecallPause)
        if not (Journal.Search(noLrc) or Journal.Search(noMana)):
            break
        Journal.Clear()
    Journal.Clear()
   
def Mina(FireBeetle):
    tileinfo = Statics.GetStaticsTileInfo(Player.Position.X, Player.Position.Y, Player.Map)
    if tileinfo.Count > 0:
        minaCava(FireBeetle)
    else:
        minaMontagna(FireBeetle)
                       
                       
def minaCava(FireBeetle):
    digable = (220,221,222,223,224,225,226,227,228,229,230,231,236,237,238,239,240,241,242,243,244,245,246,247,252,253,254,255,256,257,258,259,260,261,262,263,268,269,270,271,272,273,274,275,276,277,278,279,286,287,288,289,290,291,292,293,294,296,296,297,321,322,323,324,467,468,469,470,471,472,473,474,476,477,478,479,480,481,482,483,484,485,486,487,492,493,494,495,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,610,611,612,613,1010,1741,1742,1743,1744,1745,1746,1747,1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1771,1772,1773,1774,1775,1776,1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1801,1802,1803,1804,1805,1806,1807,1808,1809,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,1880,1881,1882,1883,1884,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2028,2029,2030,2031,2032,2033,2100,2101,2102,2103,2104,2105,1339,1340,1341,1342,1343,1344,1345,1346,1347,1348,1349,1350,1351,1352,1353,1354,1355,1356,1357,1358,1359)
    for x in range(-2,3):
        for y in range(-2,3):
            tileinfo = Statics.GetStaticsTileInfo(Player.Position.X+x, Player.Position.Y+y, Player.Map)
            for tile in tileinfo:
                if tile.StaticID in digable and tile.StaticZ == Player.Position.Z :
                    rimina=True
                    while rimina:
                        Journal.Clear()
                        timeout=10000
                        if Player.Weight>=Player.MaxWeight-50:
                            smelta(FireBeetle)
                        Items.UseItemByID(pickaxeID,-1)
                        Target.WaitForTarget(TimeoutOnWaitAction,False)
                        Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,Player.Position.Z,tile.StaticID)
                        while timeout>0:                                 
                            if (Journal.Search("You dig some") or Journal.Search("You loosen")):
                                rimina=True
                                break 
                            elif (Journal.Search(noMetal) or Journal.Search(youcant) or Journal.Search(cantseen)): 
                                rimina=False
                                break
                            else:
                                timeout-=100
                                Misc.Pause(50)

def minaMontagna(FireBeetle):
    puntiBuoni = {}
    try:
        with open('testdata.data', 'rb') as handle:
            puntiBuoni = pickle.load(handle)
    except:
        form.writeTextBox("File dei dati non esistente. Creo")

    if str(Player.Position) in puntiBuoni:
        Journal.Clear()
        rimina = True
        form.writeTextBox("Trovato spot memorizzato. Piccono i punti conosciuti")
        for x in puntiBuoni[str(Player.Position)]:
            while rimina:
                Journal.Clear()
                timeout=10000
                if Player.Weight>=Player.MaxWeight-50:
                    smelta(FireBeetle)
                Items.UseItemByID(pickaxeID,-1)
                Target.WaitForTarget(TimeoutOnWaitAction,False)
                Target.TargetExecute( int((x[1:len(x)-1]).split(", ")[0]), int((x[1:len(x)-1]).split(", ")[1]), 0)
                while timeout>0:                                 
                    if (Journal.Search("You dig some") or Journal.Search("You loosen")):
                        rimina=True
                        break
                    elif (Journal.Search(noMetal) or Journal.Search(youcant) or Journal.Search(cantseen)): 
                        rimina=False
                        break #shifta
                    else:
                        timeout-=100
                        Misc.Pause(50)
    else:
        for x in range(-2,3):
            for y in range(-2,3):
                punto = Statics.GetLandID(Player.Position.X+x,Player.Position.Y+y,Player.Map)
                if(Statics.GetTileFlag(punto, "Wall")):
                    rimina=True
                    while rimina:
                        Journal.Clear()
                        timeout=10000
                        if Player.Weight>=Player.MaxWeight-50:
                            smelta(FireBeetle)
                        Items.UseItemByID(pickaxeID,-1)
                        Target.WaitForTarget(TimeoutOnWaitAction,False)
                        Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,0)
                        while timeout>0:                                 
                            if (Journal.Search("You dig some") or Journal.Search("You loosen")):
                                rimina=True
                                puntiBuoni.setdefault(str(Player.Position),[]).append("("+str(Player.Position.X+x)+", " +str(Player.Position.Y+y)+ ", " +str(0)+ ")")
                                break 
                            elif (Journal.Search(noMetal) or Journal.Search(youcant) or Journal.Search(cantseen)): 
                                rimina=False
                                break
                            else:
                                timeout-=100
                                Misc.Pause(50)
    #SCRIVE FILE                        
    with open("testdata.data",'wb') as fp:
        pickle.dump(puntiBuoni,fp)
 
 
def getNumRuneRunebook(runeBookSerial): 
    Items.UseItem(runeBookSerial)
    Gumps.WaitForGump(1431013363, 10000)
    Misc.Pause(100)
    listaBook = Gumps.LastGumpGetLineList( )
    newListaBook = []
    for x in listaBook:
        if not (x[0].isnumeric()) and not (x.isnumeric()) and (x != "Empty") and (x != "Gate Travel") and (x != "Charges: ") and (x != "Max Charges: ") and (x != "Rename book") and (x != "Sacred Journey") and (x != "Set default") and (x != "Recall") and (x != "Drop rune") :
            newListaBook.append(x)
    if Target.HasTarget(): Target.Cancel() 
    return len(newListaBook)/2      
 
form = MainForm()
         
def SaveSettings(**settings):    
        with open("GiocoMinerSettings3.txt", "w") as out_file:
            for x in settings["RuneBookMining"]:
                out_file.write(str(x))
                out_file.write("-")
            out_file.write("\n")
            out_file.write(str(settings["RuneBookBanca"]))
            out_file.write("\n")
            out_file.write(str(settings["NumRunaCasa"]))
            out_file.write("\n")
            out_file.write(str(settings["PosizioneX"]))
            out_file.write("\n")
            out_file.write(str(settings["PosizioneY"]))
            out_file.write("\n")
            out_file.write(str(settings["PosizioneZ"]))
            out_file.write("\n")
            out_file.write(str(settings["MineBag1"]))
            out_file.write("\n")
            out_file.write(str(settings["MineBag2"]))
            out_file.write("\n")
            out_file.write(str(settings["FireBeetle"]))
 
def main(form,**settings):
    lastrune  = 5   
    NumeroRuneMiningBook1 = getNumRuneRunebook(settings["RuneBookMining"][0])
    form.writeTextBox("START GiocoMiner")
    dismount()
    giveFood(settings["FireBeetle"])
    while True:
        smelta(settings["FireBeetle"])
        MakeTinkerTool()
        MakePickaxe()
        lastrune = Scarico(lastrune,**settings)
        #SWITCH
        if lastrune >= ((6*NumeroRuneMiningBook1)-1): #when we arrive at the end of the runebook
            settings["RuneBookMining"].append(settings["RuneBookMining"].pop(0)) # delete the first and put at the end
            NumeroRuneMiningBook1=getNumRuneRunebook(settings["RuneBookMining"][0]) # count the number of rune on new runebook
            lastrune = 5 #reset
            form.writeTextBox("Passiamo al prossimo Runebook")
            giveFood(settings["FireBeetle"])
        RecallNextSpot(settings["RuneBookMining"][0],lastrune)
        lastrune = lastrune + 6    
        waitForMana()
        Mina(settings["FireBeetle"])
 
form.ReadSettings()
Application.Run(form)
