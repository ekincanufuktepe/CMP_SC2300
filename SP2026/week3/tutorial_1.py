import pandas as pd
import matplotlib.pyplot as plt

'''
fig, ax = plt.subplots(figsize=(10,5))
ax.plot([1,2,3],[4,5,6])
plt.show()
'''

df = pd.read_csv("./data/time_series_sales.csv")

plt.plot(df["date"], df["daily_sales"])
plt.show()

# Improve readability for dates
df["date"] = pd.to_datetime(df["date"]) # improve readability for dates
 
plt.figure(figsize=(8,4))
plt.plot(df["date"], df["daily_sales"], marker="o", linewidth=2, label="Sales", zorder=1)
#plt.title("Daily sales over time")
plt.xlabel("Date")
plt.ylabel("Sales (units)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.2)

#plt.tight_layout()

#plt.show()

# Add a moving average line from the csv (column ma5)
#plt.figure(figsize=(8,4))
plt.plot(df["date"], df["ma5"], marker="x", linewidth=2, label="MA5", zorder=2)
plt.title("Sales with 5-day moving average and daily sales")
#plt.xlabel("Date")
#plt.ylabel("Sales (units)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.2)

# Make promo stand out
promo_row = df[df["promo"] == 1].iloc[0]
plt.scatter([promo_row["date"]], [promo_row["daily_sales"]], s=140, color="red", zorder=3)
plt.annotate("Promo Day", (promo_row["date"], promo_row["daily_sales"]), 
                textcoords="offset points", 
                xytext=(10,10))

plt.legend()


plt.tight_layout()
plt.show()