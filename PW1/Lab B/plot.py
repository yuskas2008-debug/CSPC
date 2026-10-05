"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read decay_observed.csv (columns: time, count; skip the header row)
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2: N0 = first observed value, then the analytical curve
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: 1x2 subplot with shared x and y axes
fig, (ax_left, ax_right) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax_left.scatter(t, observed, s=12)
ax_left.set_title("Observed data")
ax_left.set_xlabel("time")
ax_left.set_ylabel("number of atoms")

ax_right.plot(t, analytical)
ax_right.set_title("Analytical")
ax_right.set_xlabel("time")
ax_right.set_ylabel("number of atoms")

# TODO 4: save the figure as figure.png
plt.tight_layout()
plt.savefig("figure.png", dpi=150)