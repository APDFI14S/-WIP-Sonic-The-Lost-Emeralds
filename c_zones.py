# (TBRPG) Sonic: The Lost Emeralds
# Ace Moom
# 2024/04/05

from a_sonic.py import Sonic()

class Zones():
    def __init__(self):
        self.zone = ['Speed Highway (Present)', 'Ocean Base (Present)', 'Lava Reef (Present)',
                      'Flying Fortress (Present)', 'Radioactive Ruins (Future)', 
                      'Lunar Complex (Future)', 'Poached Egg (Future)', 'Speed Highway (Future)']
        
        self.rings = [300, 175, 260, 100, 275, 350, 100, 250]

        self.playtype = input("Do you want to play [R]isky, or [S]afely?: ")
    def playstyle_choice(self):
        print(self.playtype)
