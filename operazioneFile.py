#Player.HeadMessage(30,str(Player.Position))
#1000,518,-29
#Player.PathFindTo(1000,518,-29)
filename = "test.txt"
with open(filename, 'w') as f:
            f.write(str(Player.Position)[1:-1])