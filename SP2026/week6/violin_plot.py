import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example dataset
data = {
    "Class": ["A","A","A","A","A","A","A","A","A",
              "B","B","B","B","B","B","B","B","B"],
    "Score": [55,60,62,65,70,72,75,80,90,
              50,52,54,60,63,64,65,66,67]
}

df = pd.DataFrame(data)

sns.violinplot(x='Class', y='Score', data=df)
plt.title("Violin plot of Test Scores by Class")
plt.show()

