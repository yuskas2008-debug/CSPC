"""
Tests for the decay simulation.
(keep your original docstring)
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    N0 = 1000
    lam = 0.4
    dt = 0.05
    index = 20                 # position in the output array
    t = index * dt             # real time = 20 * 0.05 = 1.0
    runs = 200

    finals = [simulate(N0, lam, dt=dt, seed=s)[index] for s in range(runs)]
    average = np.mean(finals)
    expected = N0 * np.exp(-lam * t)

    assert average == pytest.approx(expected, rel=0.02)