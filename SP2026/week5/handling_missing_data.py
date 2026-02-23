import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Data creation, and printing info
data = {
    'department' : ['Engineering', 'Engineering', 'Engineering',
                    'Marketing', 'Marketing', 'Marketing',
                    'HR', 'HR', 'HR'
    ],
    'salary' : [
        95000, 105000, None,
        65000, None, 70000,
        50000, None, None
    ]
}

df = pd.DataFrame(data)
print(df.head(10))
print(df.describe())
print(df.info())

# Step 2: Ignore missing values
avg_ignore = df.groupby("department")["salary"].mean()
plt.figure(figsize=(6,4))
avg_ignore.plot(kind='bar')
plt.title("Avg. Salary by Department (ignoring missing values)")
plt.ylabel("Avg. Salary")
plt.tight_layout()
plt.show()

# Step 3: Missing values filled with zeros
df_zero = df.copy(deep=True)
df_zero['salary'] = df_zero.groupby('department')['salary'].fillna(0)
print(df_zero)
avg_zero = df_zero.groupby("department")["salary"].mean()
plt.figure(figsize=(6,4))
avg_zero.plot(kind='bar')
plt.title("Avg. Salary by Department (Missing values filled with 0s)")
plt.ylabel("Avg. Salary")
plt.tight_layout()
plt.show()


# Step 4: Drop rows with missing values
df_drop = df.copy(deep=True) 
avg_zero = df_drop.groupby("department")["salary"].mean()
plt.figure(figsize=(6,4))
avg_zero.plot(kind='bar')
plt.title("Avg. Salary by Department (Missing values filled with 0s)")
plt.ylabel("Avg. Salary")
plt.tight_layout()
plt.show()
