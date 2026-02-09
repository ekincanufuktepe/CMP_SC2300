import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./data/study_hours_scores.csv")

plt.figure(figsize=(7,4))
color_map = {"A" : "red", "B" : "blue"}

for g, sub in df.groupby("group"):
    plt.scatter(sub["hours_studied"], sub["quiz_score"], 
                label=f"Group {g}", 
                color=color_map[g],
                s=60,
                alpha=0.85)
                
plt.title("Study Hours vs Quiz Score")
plt.xlabel("Hours Studied")
plt.ylabel("Quiz Score")
plt.legend()
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()

# Fit line to see trend

m, b = np.polyfit(df["hours_studied"], df["quiz_score"], 1)
x = np.linespace(df["hours_studied"].min(), df["hours_studied"].max(), 100)



                
                
                
                
                
                
                