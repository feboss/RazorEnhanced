"""
================== Pet Grades ==================
=                by Cookie Lover               =
=            Latest Release: 06/14/2017        =
=                                              =
=    What you need:                            =
=    - Animal Lore                             =
================================================
"""

class Pet:
    def __init__(self, Str, Dex, Int, HP, Phys, Fire, Cold, Poison, Energy):
        self._stats = {'str' : Str, 'dex' : Dex, 'int' : Int, 'hp' : HP}
        self._res = {'physical' : Phys, 'fire' : Fire, 'cold' : Cold, 'poison' : Poison, 'energy' : Energy}

    @property
    def Stat(self):
        return self._stats

    @property
    def Res(self):
        return self._res

class PetCalc:   
    def __init__(self, petID=0x0001, Str=0, Dex=0, Int=0, HP=0, Ph=0, Fi=0, Co=0, Po=0, En=0):
        self.Pets = {
            'bake kitsune' : Pet((170,220), (124,145), (375,425), (310,350), (40,60), (70,90), (40,60), (40,60), (40,60)),
            'rune beetle' : Pet((400,465), (125,170), (375,450), (310,360), (40,65), (35,50), (35,50), (75,95), (40,60)),
            'dragon' : Pet((796,825), (86,105), (436,475), (478,495),  (55,65), (60,70), (30,40), (25,35), (35,45)),
            'nightmare' : Pet((496,525), (86,125), (86,125), (278,315), (55,65), (30,40), (30,40), (30,40), (20,30)),
            'dread war horse' : Pet((502,551), (89,123), (100,159), (555,648), (65,75), (20,40), (20,40), (50,60), (40,50)),
            'cu sidhe' : Pet((1200,1225), (150,170), (250,285), (1010,1275), (50,65), (25,45), (70,85), (30,50), (70,85)),
            'greater dragon' : Pet((1025,1425), (81,148), (475,675), (1000,2000), (60,85), (65,90), (40,55), (40,60), (50,75)),
            'hiryu' : Pet((1200,1420), (81,148), (300,325), (900,1100), (55,70), (70,90), (15,25), (40,50), (40,50)),
            'white wyrm' : Pet((721,760), (101,130), (386,425), (433,456), (55,70), (15,25), (80,90), (40,50), (40,50)),
            'fire steed' : Pet((376,400), (91,120), (291,300), (226,240), (30,40), (70,80), (20,30), (30,40), (30,40))
            }
        self.IDs = {246 : 'bake kitsune', 277 : 'cu sidhe', 190 : 'fire steed',
                    59 : 'greater dragon', 243 : 'hiryu', 179 : 'nightmare',
                    244 : 'rune beetle', 180 : 'white wyrm'} # dread war horse
        if petID == 59:
            name = 'dragon' if Str < 1025 else 'greater dragon'
        else:
            name = self.IDs[petID]
        self.Stats = {'name' : name, 'stats' : Pet(Str, Dex, Int, HP, Ph, Fi, Co, Po, En)}
        
    def GetGrades(self):
        media = 0
        data = {'stat' : [], 'res' : []}
        for k,v in self.Stats['stats'].Res.iteritems():
            minmax = self.Pets[self.Stats['name']].Res[k]
            curv = v if v < minmax[1] else minmax[1]
            minv = curv - minmax[0] if v >= minmax[0] else 0
            data['res'].append(minv * 5.0 / (minmax[1] - minmax[0]))
        for k,v in self.Stats['stats'].Stat.iteritems():
            minmax = self.Pets[self.Stats['name']].Stat[k]
            curv = v if v < minmax[1] else minmax[1]
            minv = curv - minmax[0] if v >= minmax[0] else 0
            data['stat'].append(minv * 5.0 / (minmax[1] - minmax[0]))
        return sum(data['res']) / float(len(data['res'])) * 0.75 + sum(data['stat']) / float(len(data['stat'])) * 0.25
        
def Clean(s):
    return s.replace('<div align=right>','').replace('</div>','').replace('%','').split('/')[0]

def GetPet():  
    Misc.SendMessage('Target the pet you wish to appraise', 90)
    targ = Target.PromptTarget()
    pet = Mobiles.FindBySerial(targ)
    Mobiles.WaitForProps(pet, 4000)
    # creatures have their hp pool halved once tamed
    hpmod = 2 if '(tame)' in ' '.join(l for l in Mobiles.GetPropStringList(pet)) else 1 
    Gumps.ResetGump()
    Player.UseSkill('Animal Lore')
    Target.WaitForTarget(4000)
    Target.TargetExecute(pet)
    Gumps.WaitForGump(2470783402, 4000)
    if Gumps.CurrentGump() != 2470783402: return
    Misc.Pause(300)
    props = [Clean(l) for l in Gumps.LastGumpGetLineList()]
    stat = list()
    stat.append(int(props[38]))
    stat.extend([int(s) for s in props[41:44]])
    stat.extend([float(r) for r in props[45:50]])
    pc = PetCalc(pet.Body, stat[1], stat[2], stat[3], stat[0] * hpmod, stat[4], stat[5], stat[6], stat[7], stat[8])
    Player.HeadMessage(33, '%s: %.1f' % (pet.Name, pc.GetGrades()))
    
GetPet()
