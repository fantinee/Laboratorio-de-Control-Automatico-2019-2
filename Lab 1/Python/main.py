from tank_system import TankSystem

if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    tank_system.valve_1 = 1
    tank_system.valve_2 = 1
    tank_system.gamma_1 = 1
    tank_system.gamma_2 = 1

    tank_system.disconnect()