"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)  # delimiter="," = columns split by commas
                                                              # skiprows=1 = skip the "time,y" header line
t = data[:, 0]   # all rows, column 0 = time
y = data[:, 1]   # all rows, column 1 = height

# TODO 2: differentiate twice
v = np.gradient(y, t)   # velocity = rate of change of position
a = np.gradient(v, t)   # acceleration = rate of change of velocity
print("Mean acceleration:", a.mean())
print("Std of acceleration:", a.std())

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
