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

    def pid_control_1(self, input):
        output = 0
        return output

    def pid_control_2(self, input):
        output = 0
        return output