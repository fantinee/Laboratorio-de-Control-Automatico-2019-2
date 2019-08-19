from tank_system import TankSystem

if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    data = tank_system.objects_node.get_children_descriptions()
    for i in data:
        print(i)

    print()
    print()

    data = tank_system.objects_node.get_child([
        '2:Proceso_Tanques', '2:Alarmas', '2:Alarma_nivel'])

    # for i in data.get_children_descriptions():
    #     print(i)
    # print()

    print(data)

    # data = tank_system.objects_node.get_child([
    #     '2:Proceso_Tanques', '2:Tanques',
    #     '2:Tanque1'])
    # for i in data.get_children_descriptions():
    #     print(i)

    # tank_system.valve_1 = 0.5
    # tank_system.valve_2 = 0.5
    # tank_system.gamma_1 = 0.5
    # tank_system.gamma_2 = 0.5

    tank_system.disconnect()