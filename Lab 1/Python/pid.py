from numpy import mean

class Control:
  def __init__(self, kp, ki, kd, windup, dfilter, ref):
    self.ki = ki
    self.kp = kp
    self.kd = kd
    self.windup = windup
    self.dfilter = dfilter
    self.ref = ref
    self.old_data = []
    self.readings = 0

  def PID(self, h):

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
    derivative = kd*self.derivative_control(h)

    # U1
    u = proporcional + integral + derivative
    # se sacan los limites para que llegue a la referencia
    if(u < -1):
      u = -1
    if(u > 1):
      u = 1

    return u

  def derivative_control(self,h):
    if (len(self.readings) < self.dfilter):
      self.readings.append(h)
      return mean(self.readings)
    else:
      v = mean(self.readings + [self.h])
      self.readings.pop()
      self.readings.insert(0, v)
      return v