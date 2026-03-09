import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset with seaborn. (dataset: iris.csv)
iris = sns.load_dataset("iris")

plt.scatter(
    iris["sepal_length"],   # x-axis using the sepal_lenght variable
    iris["sepal_width"],    # y-axis using the sepal_width variable
    # c argument is for the color variable using 'species' feature/variable
    c=iris["species"].astype("category").cat.codes
)

plt.xlabel("Sepal Length")  # set the x label on scatter plot
plt.ylabel("Sepal Width")   # set the y labet on scatte plot
plt.title("Sepal Measurements by Species")  # adding a title

plt.show()

# Example 2 - Using all four variable
plt.scatter(
    iris["sepal_length"],
    iris["sepal_width"],
    s=iris["petal_length"] * 20,    # add size using petal_lenght
    c=iris["petal_width"],          # color for petal_width
    cmap="viridis",
    alpha=0.75
)

plt.colorbar(label="Petal Width")   # adds the legend for the color map

plt.show()




