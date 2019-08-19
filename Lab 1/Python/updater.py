from tank_system import TankSystem

if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    # tank_system.valve_1 = 0.5
    # tank_system.valve_2 = 0.5
    tank_system.gamma_1 = 0
    tank_system.gamma_2 = 0

    tank_system.disconnect()