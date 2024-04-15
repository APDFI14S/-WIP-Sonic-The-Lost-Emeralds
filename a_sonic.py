# (TBRPG) Sonic: The Lost Emeralds
# Ace Moom
# 2024/04/05

from d_attacks.py import Attacks()

class Sonic():
    def __init__(self, rings_player, lives, chaos_emeralds, shield, exp, playstyle, checkpoint, rank):
        self.rings_player = rings_player
        self.lives = lives
        self.chaos_emeralds = chaos_emeralds
        self.shield = shield
        self.exp = exp
        self.playtype = playstyle
        self.checkpoint = checkpoint
        self.rank = rank
        self.Attacks()

        # rings_player: Lets you beat bosses more easily.
        # lives: They follow the same function as they do in any Sonic game.
        # chaos_emeralds: They will allow you to fight the final boss.
        # shield: They give you special abilities.
        # exp: The higher your exp, the more easily you can keep your shield.
        #      You also have better odds of dodging boss attacks.
        # playtype: If you play risky, you get more exp, but less rings, lives, and odds of keeping your shield.
        #           If you play safe, you get less exp, but more rings, lives, and odds of keeping your shield.

        # rank: determines what stages you can access
    
    def playstyle(self):
        while True:
            if self.playtype == 'R'.lower():
                return True
            elif self.playtype == 'S'.lower():
                return False
            else:
                print('Please select a valid option:\n')

    # Used to ask if you want to play risky or safe


default_sonic = Sonic(50, 3, 0, '')
    


