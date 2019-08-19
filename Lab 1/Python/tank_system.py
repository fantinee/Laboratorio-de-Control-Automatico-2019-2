from opcua import Client
import time
import collections


class TankSystem:
    def __init__(self):
        self.client = None
        self.objects_node = None
        self.connected = False

        self.max_size = 600
        self.past_values = {'time': collections.deque(maxlen=self.max_size),
                            'tank_1': collections.deque(maxlen=self.max_size),
                            'tank_2': collections.deque(maxlen=self.max_size),
                            'tank_3': collections.deque(maxlen=self.max_size),
                            'tank_4': collections.deque(maxlen=self.max_size),
                            'valve_1': collections.deque(maxlen=self.max_size),
                            'valve_2': collections.deque(maxlen=self.max_size),
                            }

        self.seconds = time.time()
        self.start_time = time.time()
        self.logging_time = 1

    def connect(self):
        if not self.connected:
            # self.client = Client('opc.tcp://192.168.1.23:4840/freeopcua/server/')
            self.client = Client('opc.tcp://0.0.0.0:4840/freeopcua/server/')
            self.client.connect()
            self.objects_node = self.client.get_objects_node()
            self.connected = True
            self.log_values()

    def disconnect(self):
        if self.connected:
            self.connected = False
            self.client.disconnect()
            self.client = None
            self.objects_node = None
            self.past_values = {'time': collections.deque(maxlen=self.max_size),
                                'tank_1': collections.deque(maxlen=self.max_size),
                                'tank_2': collections.deque(maxlen=self.max_size),
                                'tank_3': collections.deque(maxlen=self.max_size),
                                'tank_4': collections.deque(maxlen=self.max_size),
                                'valve_1': collections.deque(maxlen=self.max_size),
                                'valve_2': collections.deque(maxlen=self.max_size),
                                }

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

    def log_values(self):
        if self.connected:
            self.seconds = time.time()
            self.past_values['time'].append(
                round(time.time() - self.start_time, 3))
            self.past_values['tank_1'].append(round(self.tank_1, 3))
            self.past_values['tank_2'].append(round(self.tank_2, 3))
            self.past_values['tank_3'].append(round(self.tank_3, 3))
            self.past_values['tank_4'].append(round(self.tank_4, 3))
            self.past_values['valve_1'].append(round(self.valve_1, 3))
            self.past_values['valve_2'].append(round(self.valve_2, 3))


class TankSystemFake:
    def __init__(self):
        self.client = None
        self.objects_node = None
        self.connected = False

        self.tank_values = {1: [], 2: [], 3: [], 4: []}
        self.valve_values = {1: [], 2: []}

    def connect(self):
        print('FAKE: Connecting')
        self.connected = True

    def disconnect(self):
        print('FAKE: Disconnecting')
        self.connected = False

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

    def log_values(self):
        self.tank_values[1].append(self.tank_1)
        self.tank_values[2].append(self.tank_2)
        self.tank_values[3].append(self.tank_3)
        self.tank_values[4].append(self.tank_4)
        self.valve_values[1].append(self.valve_1)

    def nothing(self):
        pass


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