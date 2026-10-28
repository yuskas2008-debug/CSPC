import pandas as pd             
import numpy as np         
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("Heart.csv")

print("Shape (rows, columns):", df.shape)
print(df.head())      
print(df.columns.tolist())
print("Missing cells:", df.isna().sum().sum())
print(df["target"].value_counts())

cont = df[["age", "chol", "trestbps", "thalach"]]
print(cont.describe())

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for ax, col in zip(axes, cont.columns):
    ax.hist(cont[col], bins=20, edgecolor="black")                          
    ax.axvline(cont[col].mean(), color="red", linestyle="--", label="mean")  
    ax.axvline(cont[col].median(), color="green", linestyle="--", label="median")
    ax.set_title(col)
    ax.legend()

plt.tight_layout()
plt.savefig("distributions.png", dpi=150)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()
for ax, col in zip(axes, cont.columns):
    stats.probplot(cont[col], dist="norm", plot=ax)
    ax.set_title("Q-Q plot: " + col)
plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.show()

print("\nShapiro-Wilk normality test")
for col in cont.columns:
    stat, p = stats.shapiro(cont[col])
    print(f"{col:10s} W={stat:.4f}  p={p:.3g}  skew={cont[col].skew():.2f}")