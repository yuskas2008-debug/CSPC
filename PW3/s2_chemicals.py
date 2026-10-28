import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("chemicals_cancer.csv")
print(df.shape)
print(df.describe())

for chem in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(df[chem], df["malignancy"])
    print(f"{chem}: Pearson r = {r:.3f} (p = {p:.3g})")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, ["benzene", "cadmium"]):
    ax.scatter(df[chem], df["malignancy"], alpha=0.4)
    ax.set_xlabel(chem)
    ax.set_ylabel("malignancy")

plt.tight_layout()
plt.savefig("naive_chemicals.png", dpi=150)
plt.show()

print(df[["benzene", "cadmium", "pollution_index", "age", "malignancy"]].corr().round(2))

low, high = 55, 70
sub = df[(df["pollution_index"] > low) & (df["pollution_index"] < high)]
print("Patients in slice:", len(sub))

print("\nInside the pollution slice:")
for chem in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(sub[chem], sub["malignancy"])
    print(f"{chem}: r = {r:.3f} (p = {p:.3g})")

for lo, hi in [(40, 55), (55, 70), (70, 85)]:
    s = df[(df["pollution_index"] > lo) & (df["pollution_index"] < hi)]
    rb = stats.pearsonr(s["benzene"], s["malignancy"])[0]
    rc = stats.pearsonr(s["cadmium"], s["malignancy"])[0]
    print(f"pollution {lo}-{hi}: n={len(s)}  benzene r={rb:.2f}  cadmium r={rc:.2f}")