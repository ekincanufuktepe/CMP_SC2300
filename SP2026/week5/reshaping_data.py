import pandas as pd

df = pd.DataFrame({
        "Name" : ["Alice", "Bob", "Charlie"],
        "Math" : [85, 90, 95],
        "Science" : [80, 88, 92]
})
print("==== Original Data ====")
print(df)

# melt function: wide data -> long data
print("\n==== After melt() Wide -> Long ====")
df_melt = pd.melt(df, id_vars=["Name"], value_vars=["Math", "Science"], var_name="Subject", value_name="Score")
print(df_melt)

# pivot function: long data -> wide data
print("\n==== After pivot() Long -> Wide ====")
df_pivot = df_melt.pivot(index="Name", columns="Subject", values="Score")
print(df_pivot)

# pivot_table usage
df_long_dup = pd.DataFrame({
        "Name" : ["Alice", "Alice", "Bob", "Bob"],
        "Subject" : ["Math", "Math", "Science", "Science"],
        "Score" : [85, 90, 88, 92]
})
print("\n==== Before pivot_table ====")
print(df_long_dup)

print("\n==== After pivot_table ====")
df_pivot_table = pd.pivot_table(df_long_dup, 
                                index="Name",
                                columns="Subject",
                                values="Score",
                                aggfunc="mean")

print(df_pivot_table)



