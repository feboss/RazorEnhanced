
'''Necro
0 - 40.0 Curse Weapon
40.0 - 60.0 Horrific Beast
60.0 - 70.0 Wither
70.0 - 100.0 Lich Form
100.0 - 120.0 Vampiric Embrace

SpellWeaving
0-10 Arcane Circle(da castare su un pentagram-abbatoir)
10-24 Thunder Storm
24-52 Reaper Form
52-66 Essence of wind
66-105 Wild Fire
105-120 Word of death
'''

while True:
    Spells.CastMagery("Weaken")
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(0x1D813)
    Misc.Pause(2000)
    Player.UseSkill("Spirit Speak")
    Misc.Pause(2000)
