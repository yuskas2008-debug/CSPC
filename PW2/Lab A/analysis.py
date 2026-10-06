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
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)

t = data[:, 0]  
y = data[:, 1]  

# TODO 2: differentiate twice
v = np.gradient(y, t)   
a = np.gradient(v, t)  
print("Mean acceleration:", a.mean())
print("Std of acceleration:", a.std())

## TODO 3: integrate back up
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]      
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]  

max_diff = np.max(np.abs(y_rec - y))
print("Max |y_rec - y|:", max_diff, "m")

# TODO 4: three stacked panels sharing the time axis
fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")

axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")

axes[2].plot(t, a, label="measured acceleration")
axes[2].axhline(-9.81, linestyle="--", color="red", label="-9.81 m/s²")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_xlabel("Time (s)")
axes[2].legend()

fig.tight_layout()
fig.savefig("motion.png", dpi=150)
plt.show()
