# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A Git repository (CSPC) published on GitHub, with a conda environment file (environment.yml) so the project can be rebuilt on any machine.
- A radioactive decay simulation with two versions (pure-Python loop and NumPy), three pytest tests, and a script (speed.py) that compares their speed.

**Speed comparison (loop vs NumPy):**
- loop    : 1.9328 s
- numpy   : 0.0002 s
- speed-up: 11439.4x faster

**Tests:** all passing? yes

**Conclusion:**
- The NumPy version was about ten thousand times faster than the loop. The loop makes one random draw for every atom at every time step, while NumPy makes one binomial draw per step for the whole sample.
- The tests showed the simulation behaves correctly: it starts at N0, rejects a negative rate, and the average over many seeds matches N0*exp(-lam*t).
- Using Git branches, a remote on GitHub and an environment.yml file made the work organised and reproducible. (Add any problem you actually had, for example the GitHub token login or a conda error, or write that there were none.)