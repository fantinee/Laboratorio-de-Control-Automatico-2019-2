from opcua import Client
import random

class TankSystem:
    def __init__(self):
        self.client = None
        self.objects_node = None

    def connect(self):
        self.client = Client('opc.tcp://192.168.1.23:4840/freeopcua/server/')
        self.client.connect()
        self.objects_node = self.client.get_objects_node()

    def disconnect(self):
        self.client.disconnect()
        self.client = None
        self.objects_node = None

    @property
    def tank_1(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Tanques',
                                            '2:Tanque1', '2:h'])
        value = node.get_value()
        return value

    @property
    def tank_2(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Tanques',
                                            '2:Tanque2', '2:h'])
        value = node.get_value()
        return value

    @property
    def tank_3(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Tanques',
                                            '2:Tanque3', '2:h'])
        value = node.get_value()
        return value

    @property
    def tank_4(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Tanques',
                                            '2:Tanque4', '2:h'])
        value = node.get_value()
        return value

    @property
    def valve_1(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Valvulas',
                                            '2:Valvula1', '2:u'])
        value = node.get_value()
        return value

    @valve_1.setter
    def valve_1(self, value):

        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Valvulas',
                                            '2:Valvula1', '2:u'])
        node.set_value(value)

    @property
    def valve_2(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Valvulas',
                                            '2:Valvula2', '2:u'])
        value = node.get_value()
        return value

    @valve_2.setter
    def valve_2(self, value):

        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Valvulas',
                                            '2:Valvula2', '2:u'])
        node.set_value(value)

    @property
    def gamma_1(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Razones',
                                            '2:Razon1', '2:gamma'])
        value = node.get_value()
        return value

    @gamma_1.setter
    def gamma_1(self, value):

        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Razones',
                                            '2:Razon1', '2:gamma'])
        node.set_value(value)

    @property
    def gamma_2(self):
        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Razones',
                                            '2:Razon2', '2:gamma'])
        value = node.get_value()
        return value

    @gamma_2.setter
    def gamma_2(self, value):

        node = self.objects_node.get_child(['2:Proceso_Tanques', '2:Razones',
                                            '2:Razon2', '2:gamma'])
        node.set_value(value)

class TankSystemFake:
    def __init__(self):
        self.client = None
        self.objects_node = None

    def connect(self):
        print('FAKE: Connecting')

    def disconnect(self):
        print('FAKE: Disconnecting')

    @property
    def tank_1(self):
        return random.uniform(0, 50)

    @property
    def tank_2(self):
        return random.uniform(0, 50)

    @property
    def tank_3(self):
        return random.uniform(0, 50)

    @property
    def tank_4(self):
        return random.uniform(0, 50)

    @property
    def valve_1(self):
        return random.uniform(0, 50)

    @property
    def valve_2(self):
        return random.uniform(0, 50)

    @property
    def gamma_1(self):
        return random.uniform(0, 50)

    @property
    def gamma_2(self):
        return random.uniform(0, 50)


if __name__ == '__main__':
    tank_system = TankSystem()
    tank_system.connect()

    data = tank_system.objects_node.get_children_descriptions()
    for i in data:
        print(i)

    print()

    data = tank_system.objects_node.get_child([
        '2:Proceso_Tanques']).get_children_descriptions()
    for i in data:
        print(i)

    print()

    data = tank_system.objects_node.get_child([
        '2:Proceso_Tanques', '2:Tanques']).get_children_descriptions()
    for i in data:
        print(i)

    print()

    data = tank_system.objects_node.get_child([
        '2:Proceso_Tanques', '2:Valvulas']).get_children_descriptions()
    for i in data:
        print(i)

    print()

    data = tank_system.objects_node.get_child([
        '2:Proceso_Tanques', '2:Razones']).get_children_descriptions()
    for i in data:
        print(i)

    print()

    data = tank_system.objects_node.get_child([
        '2:Proceso_Tanques', '2:Alarmas']).get_children_descriptions()
    for i in data:
        print(i)

    print()

    data = tank_system.objects_node.get_child([
        '2:Proceso_Tanques',
        '2:Razones',
        '2:Razon1']).get_children_descriptions()
    print(data)

    # data = tank_system.objects_node.get_child(['0:Objects'])
    # print(data)

    tank_system.disconnect()