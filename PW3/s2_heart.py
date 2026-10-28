import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("Heart.csv")

disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]  
print("n disease:", len(disease), "| n healthy:", len(healthy))


t, p = stats.ttest_ind(disease, healthy, equal_var=False)
print("Welch t-test: t =", t, " p =", p)

u, p = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
print("Mann-Whitney U: U =", u, " p =", p)

m_d, s_d = disease.mean(), stats.sem(disease)
m_h, s_h = healthy.mean(), stats.sem(healthy)
print(f"Disease: mean = {m_d:.2f} +/- {s_d:.2f} (SEM)")
print(f"Healthy: mean = {m_h:.2f} +/- {s_h:.2f} (SEM)")

plt.figure(figsize=(5, 5))
plt.errorbar(["Disease", "Healthy"], [m_d, m_h], yerr=[s_d, s_h],
             fmt="o", capsize=8, markersize=8)
plt.ylabel("Mean max heart rate (thalach)")
plt.title("Mean thalach +/- SEM")
plt.savefig("thalach_means.png", dpi=150)
plt.show()

r, p = stats.pearsonr(df["age"], df["thalach"])
rho, p2 = stats.spearmanr(df["age"], df["thalach"])
print(f"Pearson r = {r:.3f} (p = {p:.3g})")
print(f"Spearman rho = {rho:.3f} (p = {p2:.3g})")

plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
slope, intercept = np.polyfit(df["age"], df["thalach"], 1)
xs = np.linspace(df["age"].min(), df["age"].max(), 100)
plt.plot(xs, slope * xs + intercept, color="red")
plt.xlabel("age")
plt.ylabel("thalach")
plt.savefig("age_vs_thalach.png", dpi=150)
plt.show()

for col in ["target", "sex"]:
    pr = df[col].value_counts(normalize=True)
    H = -(pr * np.log2(pr)).sum()
    print(col, dict(pr.round(3)), f"entropy = {H:.3f} bits (max = {np.log2(len(pr)):.3f})")