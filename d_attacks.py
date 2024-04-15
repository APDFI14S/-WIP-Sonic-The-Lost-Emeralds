# (TBRPG) Sonic: The Lost Emeralds
# Ace Moom
# 2024/04/05

class Attacks():
    from random import randint

    def __init__(self):
        self.spin_dash = self.random.randint(3, 17)
        self.spin_charge = (1, 9)
        self.homing_attack = (7, 20)

        self.safety_margin = 20

        # spin_dash, spin_charge, and homing_attack refer to a range of
        # hitpoints dealt.

        # safety_margin is a number that will subtract from the values of
        # the attack variables. That will result in a net safety value,
        # which will directly correspond to how safe you are after landing
        # an attack.

    def SpinDash(self):
        pass
    def SpinCharge(self):
        pass
    def HomingAttack(self):
        pass