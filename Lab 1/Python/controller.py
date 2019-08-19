from numpy import mean
from pid import Control

class Controller:
    def __init__(self):
        self.activated = False

        self.ref_1 = 0
        self.ref_2 = 0

        self.kp_1 = 0
        self.ki_1 = 0
        self.kd_1 = 0
        self.windup_1 = 0
        self.d_filter_1 = 0
        self.kp_2 = 0
        self.ki_2 = 0
        self.kd_2 = 0
        self.windup_2 = 0
        self.d_filter_2 = 0
        # creates two instances
        tank_1_control = Control(self.kp_1, self.ki_1, self.kd_1, self.windup_1, self.d_filter_1, self.ref_1)
        tank_2_control = Control(self.kp_2, self.ki_2, self.kd_2, self.windup_2, self.d_filter_2, self.ref_2)

    def pid_control_1(self, input):

        output = tank_1_control.PID(input)
        return output

    def pid_control_2(self, input):
        output = tank_1_control.PID(input)
        return output