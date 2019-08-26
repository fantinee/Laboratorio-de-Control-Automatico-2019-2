from tank_system import TankSystem
from pid import Control
from time import sleep

if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    tank_system.gamma_1 = 0.6
    tank_system.gamma_2 = 0.7

    tank_system.disconnect()
