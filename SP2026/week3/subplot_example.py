import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/subplots_series.csv")
print(df.head(10))
print(df.info())
print(df.describe())

fig, axs = plt.subplots(1, 3, figsize=(11, 4))
axs[0].plot(df['t'], df['linear'])
axs[0].set_title("Linear")
axs[0].set_xlabel('t')
axs[0].grid(True, alpha=0.2)

axs[1].plot(df['t'], df['quadratic'])
axs[1].set_title("Quadratic")
axs[1].set_xlabel('t')
axs[1].grid(True, alpha=0.2)

axs[2].plot(df['t'], df['sin'])
axs[2].set_title("Sin")
axs[2].set_xlabel('t')
axs[2].grid(True, alpha=0.2)

axs[0].set_ylabel("value")
fig.suptitle("Subplots: Compare Multiple Views")

plt.tight_layout()
plt.show()