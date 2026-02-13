import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/overplotting.csv")
print(df.head(10))
print(df.info())
print(df.describe())

plt.figure(figsize=(7,4))
plt.scatter(df['x'], df['y'], s=18)
plt.title("Overplotting (No Transperency)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()

# Making scatter plot readable by adding transperency, and smaller markers
plt.figure(figsize=(7,4))
plt.scatter(df['x'], df['y'], s=14, alpha=0.25) # make marker size smaller (18 -> 14)
plt.title("Overplotting (With Transperency)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()

