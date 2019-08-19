from numpy import mean

class Control:
  def __init__(self, kp, ki, kd, windup, dfilter, ref):
    self.ki = ki
    self.kp = kp
    self.kd = kd
    self.windup = windup
    self.dfilter = dfilter
    self.ref = ref
    self.last_error = 0
    self.readings = 0

  def PID(self, h):

    error = ref - h

    # PROPORTIONAL
    proporcional = kp*error

    # INTEGRAL
    integral = ki*(integral + error)
    if(integral > windup):
      integral = windup
    elif(integral < -windup):
      integral = -windup

    # DERIVATIVE
    derivative = kd*(self.error - self.last_error)
    self.last_error = error

    # U1
    u = proporcional + integral + derivative
    # se sacan los limites para que llegue a la referencia
    if(u < -1):
      u = -1
    if(u > 1):
      u = 1

    return u

  def derivative_control(self, h):
    if (len(self.readings) < self.dfilter):
      self.readings.append(h)
      return mean(self.readings)
    else:
      v = mean(self.readings + [h])
      self.readings.pop()
      self.readings.insert(0, v)
      return v
