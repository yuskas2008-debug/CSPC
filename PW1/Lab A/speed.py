import time
from decay import simulate, simulate_loop

N = 200000
LAM = 0.4

t0 = time.perf_counter()
simulate_loop(N, LAM)
t_loop = time.perf_counter() - t0

t0 = time.perf_counter()
simulate(N, LAM)
t_numpy = time.perf_counter() - t0

print(f"loop    : {t_loop:.4f} s")
print(f"numpy   : {t_numpy:.4f} s")
print(f"speed-up: {t_loop / t_numpy:.1f}x faster")