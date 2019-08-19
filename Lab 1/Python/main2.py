from tank_system import TankSystem
from pid import Control
import time

if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    tank_system.valve_1 = -1
    tank_system.valve_2 = -1

    tank_system.gamma_1 = 0.7
    tank_system.gamma_2 = 0.6

    pid1 = Control(2, 0.2, 0.2, 4, 20, 25)
    pid2 = Control(2, 0.2, 0.2, 4, 20, 25)

    while True:
        tank_system.valve_1 = pid1.PID(tank_system.tank_1)
        tank_system.valve_2 = pid2.PID(tank_system.tank_2)
        time.sleep(0.001)

    tank_system.disconnect()
