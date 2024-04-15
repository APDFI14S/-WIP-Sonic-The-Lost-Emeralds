# (TBRPG) Sonic: The Lost Emeralds
# Ace Moom
# 2024/04/05

from a_sonic import Sonic()
from c_zones import Zones()

class Game():
    def __init__(self, save_point, Zones().zone):
        self.save_point = save_point

    def setup(self):
        
        print('Welcome to \"Sonic: The Lost Emeralds\"!')
        print('You must gather all of the Chaos Emeralds, for they have fallen into the wrong hands!')
        print('\nAnyhow, you can choose the  [F] ire Shield, the  [L] ightning Shield, or the  [B] ubble Shield\n')


        shield = input('What will you choose? ')
        
        player_one = Sonic(0, 5, 0, shield, 0, None, 0, 0)

        while True:

        print(shield)

            if shield == 'f'.lower():
                player_one.shield = 'Fire'
                break
            elif shield == 'l'.lower():
                player_one.shield = 'Lightning'
                break
            elif shield == 'b'.lower():
                player_one.shield = 'Bubble'
                break
            else:
                print('\nPlease pick a valid option.')

