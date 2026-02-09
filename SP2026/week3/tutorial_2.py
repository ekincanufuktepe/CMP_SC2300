import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/category_summary.csv")

print(df)

plt.figure(figsize=(7,4))
plt.bar(df["category"], df["count"])
plt.title("Counts by Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid(True, axis='y', alpha=0.2)
plt.tight_layout()
plt.show()

# Sort Data (by count)
df_sorted = df.sort_values("count", ascending=False)
print(df_sorted)

plt.figure(figsize=(7,4))
plt.bar(df_sorted["category"], df_sorted["count"])
plt.title("Counts by Category (sorted)")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid(True, axis='y', alpha=0.2)
plt.tight_layout()
plt.show()

# Improve readability adding edges to bars, some style improvement

plt.figure(figsize=(7,4))
plt.bar(df_sorted["category"], df_sorted["count"], edgecolor="black", linewidth=1.0)
plt.title("Improved readability (Edge + grid)")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid(True, axis='y', alpha=0.25)
plt.tight_layout()
plt.show()












