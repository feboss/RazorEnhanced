import clr
 
clr.AddReference("System")
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
 
import System
import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *
import thread, time
import System.Threading
 
 
TimeoutOnWaitAction = 4000
 
####################################
######### Variabili Sistema#########
####################################
pickaxeID = 0x0E86
forgiacasaID = 0x0FB1
tinkerID = 0x1EB8
oreID = [0x19B7, 0x19B8, 0x19B9, 0x19BA]
gemmaID = [0x3195, 0x3193, 0x3194, 0x3192, 0x3198, 0x3197]
SiFoodID = [0x09C9, 0x09F2, 0x09B7, 0x09C0]
NoFoodID = [0x097D, 0x09D2, 0x09D0, 0x09D1, 0x09EB, 0x097B]
AllFood = SiFoodID + NoFoodID
ingotID = 0x1BF2
lastrune = 5
RecallPause = 4500
noLrc = "More reagents are needed for this spell"
noMana = "Insufficient mana for this spell"
noPickaxe = "You have worn out your tool!"
locationBlocked = "that location is blocked"
noMetal = "There is no metal here to mine"
youcant = "You can't mine there"
cantseen = "Target cannot be seen"
WeightLimit = Player.MaxWeight - 80
DragDelay = 1200
 
 
class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
 
    def InitializeComponent(self):
        self.RuneBookBanca = Player.Serial
        self.RuneBookMining1 = Player.Serial
        self.RuneBookMining2 = Player.Serial
        self.MineBag1 = Player.Serial
        self.MineBag2 = Player.Serial
        self.FoodBag = Player.Serial
        self.PosizioneRunaCasa = 0
        self.SpazzaturaCasa = Player.Serial
        self.FireBeetle = Player.Serial
 
        self.PosizioneRunaCasa = self.PosizioneRunaCasa * 6 - 1
        self._groupBox_Backpack = System.Windows.Forms.GroupBox()
        self._groupBox_Casa = System.Windows.Forms.GroupBox()
        self._groupBox_Generali = System.Windows.Forms.GroupBox()
        self._label_Impostazioni = System.Windows.Forms.Label()
        self._button_Run = System.Windows.Forms.Button()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._label_RunebookMining1 = System.Windows.Forms.Label()
        self._button_RunebookMining1 = System.Windows.Forms.Button()
        self._label_RunebookMining2 = System.Windows.Forms.Label()
        self._button_RunebookMining2 = System.Windows.Forms.Button()
        self._label_SpazzaturaBackpack = System.Windows.Forms.Label()
        self._button_SpazzaturaBackpack = System.Windows.Forms.Button()
        self._label_Runebook_Casa = System.Windows.Forms.Label()
        self._button_RunebookCasa = System.Windows.Forms.Button()
        self._label_Lingotti = System.Windows.Forms.Label()
        self._button_Lingotti = System.Windows.Forms.Button()
        self._button_Gemme = System.Windows.Forms.Button()
        self._label_SpazzaturaCasa = System.Windows.Forms.Label()
        self._button_SpazzaturaCasa = System.Windows.Forms.Button()
        self._label_FireBeetle = System.Windows.Forms.Label()
        self._button_FireBeetle = System.Windows.Forms.Button()
        self._label_PosizioneCasa = System.Windows.Forms.Label()
        self._label_Gemme = System.Windows.Forms.Label()
        self._numericUpDown1 = System.Windows.Forms.NumericUpDown()
        self._textBox_Output = System.Windows.Forms.TextBox()
        self._label_Output = System.Windows.Forms.Label()
        self._label_Varie = System.Windows.Forms.Label()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._groupBox_Backpack.SuspendLayout()
        self._groupBox_Casa.SuspendLayout()
        self._groupBox_Generali.SuspendLayout()
        self._numericUpDown1.BeginInit()
        self.SuspendLayout()
        #
        # groupBox_Backpack
        #
        self._groupBox_Backpack.Controls.Add(self._label_SpazzaturaBackpack)
        self._groupBox_Backpack.Controls.Add(self._button_SpazzaturaBackpack)
        self._groupBox_Backpack.Controls.Add(self._label_RunebookMining2)
        self._groupBox_Backpack.Controls.Add(self._button_RunebookMining2)
        self._groupBox_Backpack.Controls.Add(self._label_RunebookMining1)
        self._groupBox_Backpack.Controls.Add(self._button_RunebookMining1)
        self._groupBox_Backpack.Location = System.Drawing.Point(12, 25)
        self._groupBox_Backpack.Name = "groupBox_Backpack"
        self._groupBox_Backpack.Size = System.Drawing.Size(209, 155)
        self._groupBox_Backpack.TabIndex = 0
        self._groupBox_Backpack.TabStop = False
        self._groupBox_Backpack.Text = "Backpack"
        #
        # groupBox_Casa
        #
        self._groupBox_Casa.Controls.Add(self._numericUpDown1)
        self._groupBox_Casa.Controls.Add(self._label_Gemme)
        self._groupBox_Casa.Controls.Add(self._label_PosizioneCasa)
        self._groupBox_Casa.Controls.Add(self._label_SpazzaturaCasa)
        self._groupBox_Casa.Controls.Add(self._button_SpazzaturaCasa)
        self._groupBox_Casa.Controls.Add(self._button_Gemme)
        self._groupBox_Casa.Controls.Add(self._label_Lingotti)
        self._groupBox_Casa.Controls.Add(self._button_Lingotti)
        self._groupBox_Casa.Controls.Add(self._label_Runebook_Casa)
        self._groupBox_Casa.Controls.Add(self._button_RunebookCasa)
        self._groupBox_Casa.Location = System.Drawing.Point(12, 186)
        self._groupBox_Casa.Name = "groupBox_Casa"
        self._groupBox_Casa.Size = System.Drawing.Size(209, 169)
        self._groupBox_Casa.TabIndex = 1
        self._groupBox_Casa.TabStop = False
        self._groupBox_Casa.Text = "Casa"
        #
        # groupBox_Generali
        #
        self._groupBox_Generali.Controls.Add(self._checkBox1)
        self._groupBox_Generali.Controls.Add(self._label_FireBeetle)
        self._groupBox_Generali.Controls.Add(self._button_FireBeetle)
        self._groupBox_Generali.Location = System.Drawing.Point(12, 361)
        self._groupBox_Generali.Name = "groupBox_Generali"
        self._groupBox_Generali.Size = System.Drawing.Size(209, 98)
        self._groupBox_Generali.TabIndex = 2
        self._groupBox_Generali.TabStop = False
        self._groupBox_Generali.Text = "Generali"
        #
        # label_Impostazioni
        #
        self._label_Impostazioni.Font = System.Drawing.Font(
            "Microsoft Sans Serif",
            8.25,
            System.Drawing.FontStyle.Bold,
            System.Drawing.GraphicsUnit.Point,
            0,
        )
        self._label_Impostazioni.Location = System.Drawing.Point(60, 9)
        self._label_Impostazioni.Name = "label_Impostazioni"
        self._label_Impostazioni.Size = System.Drawing.Size(101, 13)
        self._label_Impostazioni.TabIndex = 3
        self._label_Impostazioni.Text = "IMPOSTAZIONI"
        #
        # button_Run
        #
        self._button_Run.Font = System.Drawing.Font(
            "Microsoft Sans Serif",
            8.25,
            System.Drawing.FontStyle.Bold,
            System.Drawing.GraphicsUnit.Point,
            0,
        )
        self._button_Run.Location = System.Drawing.Point(302, 422)
        self._button_Run.Name = "button_Run"
        self._button_Run.Size = System.Drawing.Size(154, 37)
        self._button_Run.TabIndex = 5
        self._button_Run.Text = "Run"
        self._button_Run.UseVisualStyleBackColor = True
        self._button_Run.MouseClick += self.Button_RunMouseClick
        #
        # groupBox4
        #
        self._groupBox4.Location = System.Drawing.Point(559, 33)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.Size = System.Drawing.Size(209, 155)
        self._groupBox4.TabIndex = 1
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Backpack"
        #
        # label_RunebookMining1
        #
        self._label_RunebookMining1.Location = System.Drawing.Point(6, 16)
        self._label_RunebookMining1.Name = "label_RunebookMining1"
        self._label_RunebookMining1.Size = System.Drawing.Size(116, 23)
        self._label_RunebookMining1.TabIndex = 6
        self._label_RunebookMining1.Text = "Runebook Mining 1"
        self._label_RunebookMining1.TextAlign = (
            System.Drawing.ContentAlignment.MiddleLeft
        )
        #
        # button_RunebookMining1
        #
        self._button_RunebookMining1.Location = System.Drawing.Point(128, 16)
        self._button_RunebookMining1.Name = "button_RunebookMining1"
        self._button_RunebookMining1.Size = System.Drawing.Size(75, 23)
        self._button_RunebookMining1.TabIndex = 5
        self._button_RunebookMining1.Text = "Get"
        self._button_RunebookMining1.UseVisualStyleBackColor = True
        self._button_RunebookMining1.MouseClick += self.Button_RunebookMining1MouseClick
        #
        # label_RunebookMining2
        #
        self._label_RunebookMining2.Location = System.Drawing.Point(6, 39)
        self._label_RunebookMining2.Name = "label_RunebookMining2"
        self._label_RunebookMining2.Size = System.Drawing.Size(116, 23)
        self._label_RunebookMining2.TabIndex = 8
        self._label_RunebookMining2.Text = "Runebook Mining 2"
        self._label_RunebookMining2.TextAlign = (
            System.Drawing.ContentAlignment.MiddleLeft
        )
        #
        # button_RunebookMining2
        #
        self._button_RunebookMining2.Location = System.Drawing.Point(128, 39)
        self._button_RunebookMining2.Name = "button_RunebookMining2"
        self._button_RunebookMining2.Size = System.Drawing.Size(75, 23)
        self._button_RunebookMining2.TabIndex = 7
        self._button_RunebookMining2.Text = "Get"
        self._button_RunebookMining2.UseVisualStyleBackColor = True
        self._button_RunebookMining2.MouseClick += self.Button_RunebookMining2MouseClick
        #
        # label_SpazzaturaBackpack
        #
        self._label_SpazzaturaBackpack.Location = System.Drawing.Point(6, 62)
        self._label_SpazzaturaBackpack.Name = "label_SpazzaturaBackpack"
        self._label_SpazzaturaBackpack.Size = System.Drawing.Size(116, 23)
        self._label_SpazzaturaBackpack.TabIndex = 10
        self._label_SpazzaturaBackpack.Text = "Bag Spazzatura"
        self._label_SpazzaturaBackpack.TextAlign = (
            System.Drawing.ContentAlignment.MiddleLeft
        )
        #
        # button_SpazzaturaBackpack
        #
        self._button_SpazzaturaBackpack.Location = System.Drawing.Point(128, 62)
        self._button_SpazzaturaBackpack.Name = "button_SpazzaturaBackpack"
        self._button_SpazzaturaBackpack.Size = System.Drawing.Size(75, 23)
        self._button_SpazzaturaBackpack.TabIndex = 9
        self._button_SpazzaturaBackpack.Text = "Get"
        self._button_SpazzaturaBackpack.UseVisualStyleBackColor = True
        self._button_SpazzaturaBackpack.MouseClick += (
            self.Button_SpazzaturaBackpackMouseClick
        )
        #
        # label_Runebook_Casa
        #
        self._label_Runebook_Casa.Location = System.Drawing.Point(6, 16)
        self._label_Runebook_Casa.Name = "label_Runebook_Casa"
        self._label_Runebook_Casa.Size = System.Drawing.Size(116, 23)
        self._label_Runebook_Casa.TabIndex = 12
        self._label_Runebook_Casa.Text = "Runebook Casa"
        self._label_Runebook_Casa.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # button_RunebookCasa
        #
        self._button_RunebookCasa.Location = System.Drawing.Point(128, 16)
        self._button_RunebookCasa.Name = "button_RunebookCasa"
        self._button_RunebookCasa.Size = System.Drawing.Size(75, 23)
        self._button_RunebookCasa.TabIndex = 11
        self._button_RunebookCasa.Text = "Get"
        self._button_RunebookCasa.UseVisualStyleBackColor = True
        self._button_RunebookCasa.MouseClick += self.Button_RunebookCasaMouseClick
        #
        # label_Lingotti
        #
        self._label_Lingotti.Location = System.Drawing.Point(6, 62)
        self._label_Lingotti.Name = "label_Lingotti"
        self._label_Lingotti.Size = System.Drawing.Size(116, 23)
        self._label_Lingotti.TabIndex = 15
        self._label_Lingotti.Text = "Cassa Lingotti"
        self._label_Lingotti.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # button_Lingotti
        #
        self._button_Lingotti.Location = System.Drawing.Point(128, 62)
        self._button_Lingotti.Name = "button_Lingotti"
        self._button_Lingotti.Size = System.Drawing.Size(75, 23)
        self._button_Lingotti.TabIndex = 14
        self._button_Lingotti.Text = "Get"
        self._button_Lingotti.UseVisualStyleBackColor = True
        self._button_Lingotti.MouseClick += self.Button_LingottiMouseClick
        #
        # button_Gemme
        #
        self._button_Gemme.Location = System.Drawing.Point(128, 85)
        self._button_Gemme.Name = "button_Gemme"
        self._button_Gemme.Size = System.Drawing.Size(75, 23)
        self._button_Gemme.TabIndex = 16
        self._button_Gemme.Text = "Get"
        self._button_Gemme.UseVisualStyleBackColor = True
        self._button_Gemme.MouseClick += self.Button_GemmeMouseClick
        #
        # label_SpazzaturaCasa
        #
        self._label_SpazzaturaCasa.Location = System.Drawing.Point(6, 108)
        self._label_SpazzaturaCasa.Name = "label_SpazzaturaCasa"
        self._label_SpazzaturaCasa.Size = System.Drawing.Size(116, 23)
        self._label_SpazzaturaCasa.TabIndex = 19
        self._label_SpazzaturaCasa.Text = "Spazzatura"
        self._label_SpazzaturaCasa.TextAlign = (
            System.Drawing.ContentAlignment.MiddleLeft
        )
        #
        # button_SpazzaturaCasa
        #
        self._button_SpazzaturaCasa.Location = System.Drawing.Point(128, 108)
        self._button_SpazzaturaCasa.Name = "button_SpazzaturaCasa"
        self._button_SpazzaturaCasa.Size = System.Drawing.Size(75, 23)
        self._button_SpazzaturaCasa.TabIndex = 18
        self._button_SpazzaturaCasa.Text = "Get"
        self._button_SpazzaturaCasa.UseVisualStyleBackColor = True
        self._button_SpazzaturaCasa.MouseClick += self.Button_SpazzaturaCasaMouseClick
        #
        # button_FireBeetle
        #
        self._button_FireBeetle.Location = System.Drawing.Point(128, 16)
        self._button_FireBeetle.Name = "button_FireBeetle"
        self._button_FireBeetle.Size = System.Drawing.Size(75, 23)
        self._button_FireBeetle.TabIndex = 20
        self._button_FireBeetle.Text = "Get"
        self._button_FireBeetle.UseVisualStyleBackColor = True
        self._button_FireBeetle.MouseClick += self.Button_FireBeetleMouseClick
        #
        # label_FireBeetle
        #
        self._label_FireBeetle.Location = System.Drawing.Point(6, 16)
        self._label_FireBeetle.Name = "label_FireBeetle"
        self._label_FireBeetle.Size = System.Drawing.Size(100, 23)
        self._label_FireBeetle.TabIndex = 21
        self._label_FireBeetle.Text = "Fire Beetle"
        self._label_FireBeetle.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # label_PosizioneCasa
        #
        self._label_PosizioneCasa.Location = System.Drawing.Point(6, 39)
        self._label_PosizioneCasa.Name = "label_PosizioneCasa"
        self._label_PosizioneCasa.Size = System.Drawing.Size(116, 23)
        self._label_PosizioneCasa.TabIndex = 21
        self._label_PosizioneCasa.Text = "Posizione runa casa"
        self._label_PosizioneCasa.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # label_Gemme
        #
        self._label_Gemme.Location = System.Drawing.Point(6, 85)
        self._label_Gemme.Name = "label_Gemme"
        self._label_Gemme.Size = System.Drawing.Size(116, 23)
        self._label_Gemme.TabIndex = 22
        self._label_Gemme.Text = "Cassa Gemme"
        self._label_Gemme.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        #
        # numericUpDown1
        #
        self._numericUpDown1.Location = System.Drawing.Point(128, 41)
        self._numericUpDown1.Name = "numericUpDown1"
        self._numericUpDown1.Size = System.Drawing.Size(31, 20)
        self._numericUpDown1.TabIndex = 23
        self._numericUpDown1.Maximum = 12
        self._numericUpDown1.Minimum = 1
        #
        # textBox_Output
        #
        self._textBox_Output.Location = System.Drawing.Point(227, 33)
        self._textBox_Output.Multiline = True
        self._textBox_Output.Name = "textBox_Output"
        self._textBox_Output.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        self._textBox_Output.Size = System.Drawing.Size(326, 367)
        self._textBox_Output.TabIndex = 6
        #
        # label_Output
        #
        self._label_Output.Font = System.Drawing.Font(
            "Microsoft Sans Serif",
            8.25,
            System.Drawing.FontStyle.Bold,
            System.Drawing.GraphicsUnit.Point,
            0,
        )
        self._label_Output.Location = System.Drawing.Point(227, 9)
        self._label_Output.Name = "label_Output"
        self._label_Output.Size = System.Drawing.Size(101, 13)
        self._label_Output.TabIndex = 7
        self._label_Output.Text = "OUTPUT"
        #
        # label_Varie
        #
        self._label_Varie.Font = System.Drawing.Font(
            "Microsoft Sans Serif",
            8.25,
            System.Drawing.FontStyle.Bold,
            System.Drawing.GraphicsUnit.Point,
            0,
        )
        self._label_Varie.Location = System.Drawing.Point(559, 9)
        self._label_Varie.Name = "label_Varie"
        self._label_Varie.Size = System.Drawing.Size(101, 13)
        self._label_Varie.TabIndex = 8
        self._label_Varie.Text = "VARIE"
        #
        # checkBox1
        #
        self._checkBox1.Location = System.Drawing.Point(98, 16)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Padding = System.Windows.Forms.Padding(8, 0, 0, 0)
        self._checkBox1.Size = System.Drawing.Size(24, 24)
        self._checkBox1.TabIndex = 22
        self._checkBox1.UseVisualStyleBackColor = True
        #
        # MainForm
        #
        self.ClientSize = System.Drawing.Size(780, 468)
        self.Controls.Add(self._label_Varie)
        self.Controls.Add(self._label_Output)
        self.Controls.Add(self._textBox_Output)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._button_Run)
        self.Controls.Add(self._label_Impostazioni)
        self.Controls.Add(self._groupBox_Generali)
        self.Controls.Add(self._groupBox_Casa)
        self.Controls.Add(self._groupBox_Backpack)
        self.Name = "MainForm"
        self.Text = "GiocoMiner"
        self.TopMost = True
        self._groupBox_Backpack.ResumeLayout(False)
        self._groupBox_Casa.ResumeLayout(False)
        self._groupBox_Generali.ResumeLayout(False)
        self._numericUpDown1.EndInit()
        self.ResumeLayout(False)
        self.PerformLayout()
 
    def Button_RunebookMining1MouseClick(self, sender, e):
        self.RuneBookMining1 = Target.PromptTarget()
        self._textBox_Output.AppendText("Primo cammino impostato!\n")
 
    def Button_RunebookMining2MouseClick(self, sender, e):
        self.RuneBookMining2 = Target.PromptTarget()
        self._textBox_Output.AppendText("Secondo cammino impostato!\n")
 
    def Button_SpazzaturaBackpackMouseClick(self, sender, e):
        self.FoodBag = Target.PromptTarget()
        self._textBox_Output.AppendText("Bag cibo impostata!\n")
 
    #
    def Button_RunebookCasaMouseClick(self, sender, e):
        self.RuneBookBanca = Target.PromptTarget()
        self._textBox_Output.AppendText("Runebook Casa impostata!\n")
 
    def Button_LingottiMouseClick(self, sender, e):
        self.MineBag1 = Target.PromptTarget()
        self._textBox_Output.AppendText("Cassa lingotti impostata!\n")
 
    def Button_GemmeMouseClick(self, sender, e):
        self.MineBag2 = Target.PromptTarget()
        self._textBox_Output.AppendText("Cassa gemma impostata!\n")
 
    def Button_SpazzaturaCasaMouseClick(self, sender, e):
        self.SpazzaturaCasa = Target.PromptTarget()
        self._textBox_Output.AppendText("Spazzatura impostata!\n")
 
    #
    def Button_FireBeetleMouseClick(self, sender, e):
        self.FireBeetle = Target.PromptTarget()
        self._textBox_Output.AppendText("Fire Beetle impostato!\n")
 
    def Button_RunMouseClick(self, sender, e):
        SaveSettings(self,self.RuneBookMining1,self.RuneBookMining2,self.FoodBag,self.RuneBookBanca,self._numericUpDown1.Value,self.MineBag1,self.MineBag2,self.SpazzaturaCasa,self.FireBeetle)
        thread.start_new_thread(main, (self,int(self.RuneBookMining1),int(self.RuneBookMining2),int(self.FoodBag),int(self.RuneBookBanca),self._numericUpDown1.Value,int(self.MineBag1),int(self.MineBag2),int(self.SpazzaturaCasa),int(self.FireBeetle)))
        #main(self,int(self.RuneBookMining1),int(self.RuneBookMining2),int(self.FoodBag),int(self.RuneBookBanca),self._numericUpDown1.Value,int(self.MineBag1),int(self.MineBag2),int(self.SpazzaturaCasa),int(self.FireBeetle))
    def writeTextBox(self,stringa):
        stringa = str(stringa)
        self._textBox_Output.AppendText((stringa + "\n"))
         
    def ReadSettings(self):
        try:
            with open ('GiocoMinerSettings.txt', 'r') as f:
                with open("GiocoMinerSettings.txt") as in_file:
                    self.writeTextBox("File impostazioni trovato.Carico...")
                    self.writeTextBox("Le impostazioni vengono salvate in automatico al RUN.")
                    my_lines = in_file.readlines()
                    self.RuneBookMining1 = my_lines[0].strip()
                    self.RuneBookMining2 = my_lines[1].strip()
                    self.FoodBag = my_lines[2].strip()
                    self.RuneBookBanca = my_lines[3].strip()
                    self.PosizioneRunaCasa = int(my_lines[4])
                    self.MineBag1 = my_lines[5].strip()
                    self.MineBag2 = my_lines[6].strip()
                    self.SpazzaturaCasa = my_lines[7].strip()
                    self.FireBeetle = my_lines[8].strip()
                    self._numericUpDown1.Value = self.PosizioneRunaCasa
        except IOError:
            self.writeTextBox("File impostazioni NON TROVATO!!!")
            self.writeTextBox("Imposta le varie cose e poi runna il programma")
            self.writeTextBox("Non Dimenticarti NULLA!!!!")
 
def createFood(FoodBag):
    Journal.Clear()
    form.writeTextBox("Creo da mangiare al piccolo. Aspetta un attimo...")
    while True:
        Spells.CastMagery("Create Food")
        Misc.Pause(3000)
        if (Journal.Search("sausage") or Journal.Search("cut of ribs") or Journal.Search("a ham") or Journal.Search("a cooked bird")):
            moveFood(FoodBag)
            break
               
def moveFood(FoodBag):
    for item in Player.Backpack.Contains:
        for xfoodID in AllFood: 
            if item.ItemID == xfoodID:
                form.writeTextBox("Sposto cibo nella bag")
                Items.Move(item, FoodBag, 0)
                Misc.Pause(DragDelay)
   
def giveFood(FoodBag,FireBeetle):
    food = Items.FindBySerial(FoodBag)
    for item in food.Contains:
        for petfood in SiFoodID:
            if item.ItemID == petfood:
                Items.Move(item, FireBeetle, 0)
                Misc.Pause(DragDelay)
                return
    form.writeTextBox("Sposto cibo inutile nella bag spazzatura.")
    createFood(FoodBag)
    giveFood(FoodBag,FireBeetle)
        
   
def smelta(FireBeetle):
    form.writeTextBox("Fammi Smeltare...")
    if Player.Weight >= WeightLimit - 130:
        if Target.HasTarget(): Target.Cancel()
        for item in Player.Backpack.Contains:
            for xoreID in oreID:
                if item.ItemID == xoreID:
                    Items.UseItem(item)
                    Target.WaitForTarget(2000,False)
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
    if Items.BackpackCount(pickaxeID, -1) >= 2: ####DASISTEMARE
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
   
def Scarico(RuneBookBanca,MineBag1,MineBag2,FoodBag,SpazzaturaCasa,lastrune,PosizioneRunaCasa):
    if Player.Weight >= WeightLimit - 120:
        form.writeTextBox("Sono un pò appesantito. Vado a scaricare")
        if Target.HasTarget(): Target.Cancel()
        Journal.Clear()
        waitForMana()
        while True:
            Gumps.ResetGump()
            Items.UseItem(RuneBookBanca)
            Gumps.WaitForGump(1431013363, TimeoutOnWaitAction)
            Gumps.SendAction(1431013363, PosizioneRunaCasa*6-1)
            Misc.Pause(RecallPause)
            if not (Journal.Search(noLrc) or Journal.Search(noMana)):
                break
            Journal.Clear()
        for item in Player.Backpack.Contains:
            #for xoreID in oreID:
                if item.ItemID == ingotID:
                    form.writeTextBox("--> Sposto lingotti")
                    Items.Move(item, MineBag1, 0)
                    Misc.Pause(DragDelay)
        for item in Player.Backpack.Contains:
            for xgemmaID in gemmaID:
                if item.ItemID == xgemmaID:
                    form.writeTextBox("--> Sposto gemme")
                    Items.Move(item, MineBag2, 0)
                    Misc.Pause(DragDelay)       
        xFoodBag = Items.FindBySerial(FoodBag)
        for item in xFoodBag.Contains:
            for xfoodID in NoFoodID: 
                if item.ItemID == xfoodID:
                    form.writeTextBox("--> Sposto Cibo inutile")
                    Items.Move(item, SpazzaturaCasa, 0)
                    Misc.Pause(DragDelay)
        form.writeTextBox("Ho scaricato tutto. Adesso si che mi sento bene")
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
   
def Mina():
    tileinfo = Statics.GetStaticsTileInfo(Player.Position.X, Player.Position.Y, Player.Map)
    if tileinfo.Count > 0:
        minaCava()
    else:
        minaMontagna()
                       
                       
def minaCava():
    uscitaDiSicurezza = 15
    Journal.Clear()
    tileinfo = Statics.GetStaticsTileInfo(Player.Position.X, Player.Position.Y, Player.Map)
    for tile in tileinfo:
        if tile.StaticID > 1000 and tile.StaticID < 3000 and tile.StaticZ == Player.Position.Z :
            for x in range(-1,2):
                Journal.Clear()
                for y in range(-1,2):
                    Journal.Clear()                
                    Items.UseItemByID(pickaxeID,-1)
                    Target.WaitForTarget(2000,False)
                    Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,0,tile.StaticID)
                    Misc.Pause(300)
                    if (Journal.Search(noMetal)):
                        Misc.SendMessage("NoMetallo")
                        if Target.HasTarget(): Target.Cancel()
                        break
                    if (Journal.Search("You dig some") or Journal.Search("You loosen")):
                        while not(Journal.Search(noMetal) or Journal.Search(youcant) or Journal.Search(cantseen) or uscitaDiSicurezza<1):
                            Items.UseItemByID(pickaxeID,-1)
                            Target.WaitForTarget(2000,False)
                            Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,0,tile.StaticID)
                            uscitaDiSicurezza-=1
                            Misc.Pause(500)
def minaMontagna():
    uscitaDiSicurezza = 15
    for x in range(-1,2):
        Journal.Clear()
        for y in range(-1,2):
            Journal.Clear() 
            Items.UseItemByID(pickaxeID,-1)
            Target.WaitForTarget(2000,False)
            Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,Player.Position.Z)
            Misc.Pause(300)
            if (Journal.Search(noMetal)):
                form.writeTextBox("No metal")
                if Target.HasTarget(): Target.Cancel()
                break
            if (Journal.Search("You dig some") or Journal.Search("You loosen")):
                while not(Journal.Search(noMetal) or Journal.Search(youcant) or Journal.Search(cantseen) or uscitaDiSicurezza<1):
                    Items.UseItemByID(pickaxeID,-1)
                    Target.WaitForTarget(2000,False)
                    Target.TargetExecute(Player.Position.X+x,Player.Position.Y+y,Player.Position.Z)
                    uscitaDiSicurezza-=1
                    Misc.Pause(500)
 
 
def getNumRuneRunebook(runeBookSerial): 
    Items.UseItem(runeBookSerial)
    Gumps.WaitForGump(1431013363, 3000)
    Misc.Pause(100)
    listaBook = Gumps.LastGumpGetLineList( )
    newListaBook = []
    for x in listaBook:
        if not (x[0].isnumeric()) and not (x.isnumeric()) and (x != "Empty") and (x != "Gate Travel") and (x != "Charges: ") and (x != "Max Charges: ") and (x != "Rename book") and (x != "Sacred Journey") and (x != "Set default") and (x != "Recall") and (x != "Drop rune") :
            newListaBook.append(x)
    if Target.HasTarget(): Target.Cancel() 
    return len(newListaBook)/2      
 
form = MainForm()
         
def SaveSettings(form,RuneBookMining1,RuneBookMining2,FoodBag,RuneBookBanca,PosizioneRunaCasa,MineBag1,MineBag2,SpazzaturaCasa,FireBeetle):    
        with open("GiocoMinerSettings.txt", "w") as out_file:
                out_file.write(str(RuneBookMining1))
                out_file.write("\n")
                out_file.write(str(RuneBookMining2))
                out_file.write("\n")
                out_file.write(str(FoodBag))
                out_file.write("\n")
                out_file.write(str(RuneBookBanca))
                out_file.write("\n")
                out_file.write(str(form._numericUpDown1.Value))
                out_file.write("\n")
                out_file.write(str(MineBag1))
                out_file.write("\n")
                out_file.write(str(MineBag2))
                out_file.write("\n")
                out_file.write(str(SpazzaturaCasa))
                out_file.write("\n")
                out_file.write(str(FireBeetle))
 
                 
 
def main(form,RuneBookMining1,RuneBookMining2,FoodBag,RuneBookBanca,PosizioneRunaCasa,MineBag1,MineBag2,SpazzaturaCasa,FireBeetle):
    lastrune  = 5   
    NumeroRuneMiningBook1 = getNumRuneRunebook(RuneBookMining1)
    NumeroRuneMiningBook2 = getNumRuneRunebook(RuneBookMining2)
    form.writeTextBox("START GiocoMiner")
    dismount()
    giveFood(FoodBag,FireBeetle)
    while True:
        smelta(FireBeetle)
        MakeTinkerTool()
        MakePickaxe()
        lastrune = Scarico(RuneBookBanca,MineBag1,MineBag2,FoodBag,SpazzaturaCasa,lastrune,PosizioneRunaCasa)
        #SWITCH
        if lastrune >= ((6*NumeroRuneMiningBook1)-1):
            RuneBookTemp = RuneBookMining1
            RuneBookMining1 = RuneBookMining2
            RuneBookMining2 = RuneBookTemp
            NumeroRuneMiningBookTemp = NumeroRuneMiningBook1
            NumeroRuneMiningBook1 = NumeroRuneMiningBook2
            NumeroRuneMiningBook2 = NumeroRuneMiningBookTemp
            form.writeTextBox("Passiamo al prossimo Runebook")
            lastrune = 5 
        RecallNextSpot(RuneBookMining1,lastrune)
        lastrune = lastrune + 6
         
         
        waitForMana()
        Mina()
 
form.ReadSettings()
Application.Run(form)