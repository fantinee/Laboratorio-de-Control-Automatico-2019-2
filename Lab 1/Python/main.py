from tank_system import TankSystem
from pid import Control
from time import sleep

if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    tank_system.gamma_1 = 0.7
    tank_system.gamma_2 = 0.6
    while True:
        pid1 = Control(0.7663, 0.01858, 0.43856, 20, 5, 25, tank_system.tank1)
        tank_system.valve1 = pid1
        time.sleep(0.1)
    tank_system.disconnect()
