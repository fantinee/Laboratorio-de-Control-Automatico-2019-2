from numpy import mean

class Control:
  def __init__(self, kp, ki, kd, windup, dfilter, ref, h):
    self.ki = ki
    self.kp = kp
    self.kd = kd
    self.windup = windup
    self.dfilter = dfilter
    self.ref = ref
    self.h = h
    self.old_data = []
    self.readings = 0

  def PID(self):

    error = ref - h

    # PROPORTIONAL
    proporcional = kp*error

    # INTEGRAL
    integral = ki*(integral + error)
    if(integral > windup):
      integral = windup1
    elif(integral < 0):
      integral = 0

    # DERIVATIVE
    derivative = kd*self.derivative_control()

    # U1
    u = proporcional + integral + derivative
    if(u < -1):
      u = -1
    if(u > 1):
      u = 1

    return u

  def derivative_control(self):
    if (len(self.readings) < self.dfilter):
      self.readings.append(h)
      return mean(self.readings)
    else:
      v = mean(self.readings + [self.h])
      self.readings.pop()
      self.readings.insert(0, v)
      return v
