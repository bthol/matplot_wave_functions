import matplotlib.pyplot as plt
import math
import random

# point values
x = []
y = []

# Generic parameters
amplitude = 10
frequency = 5
start_window = 0
end_window = 10
phaze_shift = 5
sample_rate = 1

# parameters for function transformation
x_shift = 0
y_shift = 0
# negative values reflect opposite of positive
x_reflect = 1
y_reflect = 1
# compresses : x > 1 and stretch : 0 < x < 1
# NOTE: use postive values for compress parameters to avoid double negatives with reflect parameters
x_compress = 1
y_compress = 1

# Parameters for pulse wave
pulse_period = 2
pulse_frequency = 5
pulse_amplitude = 20


# sine wave function
def sine_wave(amplitude, frequency, x_shift, y_shift, x_reflect, y_reflect, x_compress, y_compress, start_window = 0, end_window = 10):
  for i in range(start_window, end_window + 1):
    x.append(i)
    y.append(y_reflect * y_compress * ((math.sin(x_reflect * x_compress * i + x_shift) * amplitude) + y_shift))

# smooth pulse wave function
def pulse_wave_smooth(pulse_period, pulse_frequency, pulse_amplitude, start_window = 0, end_window = 10):
  high_period = pulse_amplitude / 2
  low_period = -(pulse_amplitude / 2)
  y_val = low_period
  count = pulse_period
  for i in range(start_window, end_window + 1):
    x.append(i)
    y.append(y_val)
    count += 1
    if count == pulse_period:
      y_val = low_period
    if (i % pulse_frequency == 0):
      y_val = high_period
      count = 0

# sharp pulse wave function
def pulse_wave_sharp(pulse_period, pulse_frequency, pulse_amplitude, start_window = 0, end_window = 10):
  high_period = pulse_amplitude / 2
  low_period = -(pulse_amplitude / 2)
  y_val = low_period
  count = pulse_period
  for i in range(start_window, end_window + 1):
    x.append(i)
    y.append(y_val)
    count += 1
    if count == pulse_period:
      x.append(i)
      y_val = low_period
      y.append(y_val)
    if (i % pulse_frequency == 0):
      x.append(i)
      y_val = high_period
      y.append(y_val)
      count = 0

# rabid riser wave function
def riser_wave(start_window = 0, end_window = 10):
  for i in range(start_window, end_window + 1):
    x.append(i)
    y.append(math.sin(math.pi * i))

# random wave function
def random_wave(amplitude, start_window = 0, end_window = 10):
  for i in range(start_window, end_window + 1):
    x.append(i)
    y.append(random.random() * amplitude)

# Select wave function
sine_wave(amplitude, frequency, x_shift, y_shift, x_reflect, y_reflect, x_compress, y_compress, start_window, end_window)

# pulse_wave_smooth(pulse_period, pulse_frequency, pulse_amplitude, start_window, end_window)

# pulse_wave_sharp(pulse_period, pulse_frequency, pulse_amplitude, start_window, end_window)

# riser_wave(start_window, end_window)

# random_wave(amplitude, start_window, end_window)

# phaze function
# Note: phaze function does not work for sharp pulse wave
def phaze(ls, phaze):
  phazed = []
  multiplier = int((phaze / len(ls)) - (phaze / len(ls) % 1))
  for i in range(0, len(ls)):
    if (phaze >= 0):
      if i - phaze >= 0 and i - phaze < len(ls):
        phazed.append(ls[i - phaze])
      if i - phaze < 0:
        if phaze < (len(ls) * 2):
          phazed.append(ls[len(ls) + i - phaze])
        else:
          phazed.append(ls[(len(ls) * multiplier) + i - phaze])
    else:
      phazed.append(ls[(len(ls) * multiplier) + i - phaze])
  return phazed
# y = phaze(y, phaze_shift)

# Render Display
fig, ax = plt.subplots()
ax.plot(x, y)
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.show()