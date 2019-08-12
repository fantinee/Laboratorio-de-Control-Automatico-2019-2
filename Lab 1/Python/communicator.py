from opcua import Client
import random

class Comunnicator:
    def __init__(self):
        self.client = None
        self.objects_node = None

    def connect(self):
        self.client = Client('opc.tcp://localhost:4840/freeopcua/server/')
        self.client.connect()
        self.objects_node = self.client.get_objects_node()

    def disconnect(self):
        self.client.disconnect()
        self.client = None
        self.objects_node = None

    @property
    def tank_1(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Tanques',
                                            '1:Tanque 1', '1:h'])
        value = node.get_value()
        return value

    @property
    def tank_2(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Tanques',
                                            '1:Tanque 2', '1:h'])
        value = node.get_value()
        return value

    @property
    def tank_3(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Tanques',
                                            '1:Tanque 3', '1:h'])
        value = node.get_value()
        return value

    @property
    def tank_4(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Tanques',
                                            '1:Tanque 4', '1:h'])
        value = node.get_value()
        return value

    @property
    def valve_1(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Valvulas',
                                            '1:Valvula 1', '1:u'])
        value = node.get_value()
        return value

    @property
    def valve_2(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Valvulas',
                                            '1:Valvula 2', '1:u'])
        value = node.get_value()
        return value

    @property
    def gamma_1(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Razones',
                                            '1:Razon 1', '1:gamma'])
        value = node.get_value()
        return value

    @property
    def gamma_2(self):
        node = self.objects_node.get_child(['1:Proceso Tanques', '1:Razones',
                                            '1:Razon 1', '1:gamma'])
        value = node.get_value()
        return value

class CommunicatorFake:
    def __init__(self):
        self.client = None
        self.objects_node = None

    def connect(self):
        print('FAKE: Connecting')

    def disconnect(self):
        print('FAKE: Disconnecting')

    @property
    def tank_1(self):
        return random.uniform(0, 1)

    @property
    def tank_2(self):
        return random.uniform(0, 1)

    @property
    def tank_3(self):
        return random.uniform(0, 1)

    @property
    def tank_4(self):
        return random.uniform(0, 1)

    @property
    def valve_1(self):
        return random.uniform(0, 1)

    @property
    def valve_2(self):
        return random.uniform(0, 1)

    @property
    def gamma_1(self):
        return random.uniform(0, 1)

    @property
    def gamma_2(self):
        return random.uniform(0, 1)

