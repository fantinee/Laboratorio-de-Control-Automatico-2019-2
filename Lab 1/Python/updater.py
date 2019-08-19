from tank_system import TankSystem

if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    # tank_system.valve_1 = 0.7
    # tank_system.valve_2 = 0.6
    tank_system.gamma_1 = 0.7 # No puede ser cero
    tank_system.gamma_2 = 0.6 # No puede ser cero

    # print(tank_system.tank_1)
    # print(tank_system.tank_2)
    # print(tank_system.tank_3)
    # print(tank_system.tank_4)

    tank_system.disconnect()