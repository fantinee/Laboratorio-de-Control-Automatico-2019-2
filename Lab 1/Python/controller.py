import random
import math

class Controller:
    def __init__(self, number):
        self.number = number

        self.active = False

        self.ref = 0

        self.k_p = 0
        self.k_i = 0
        self.k_d = 0
        self.windup = 0
        self.d_filter = 0

        self.error_sum = 0
        self.error_last = 0

    def pid_control(self, value, time_dif):
        error = self.ref - value

        # Proportional
        u_p = self.k_p * error

        # Integral
        self.error_sum += error
        self.error_sum = min(max(self.error_sum, -self.windup), self.windup)
        u_i = self.k_i * self.error_sum * 0.1

        # Derivative
        u_d = self.k_d * (error - self.error_last) / 0.1
        self.error_last = error

        u = u_p + u_i + u_d

        u = min(max(u, -1), 1)

        if self.number == 1:
            print('''PID {}
            Error: {}
            u_p: {}
            u_i: {}
            u_d: {}
            u: {}
            '''.format(self.number, error, u_p, u_i, u_d, u))

        return u

    def print_variables(self):
        print('''Controller {} variables
        Ref: {}
        K_p: {}
        K_i: {}
        K_d: {}
        Windup limit: {}
        Derivative filter: {}'''.format(self.number, self.ref, self.k_p,
                                        self.k_i, self.k_d, self.windup,
                                        self.d_filter))