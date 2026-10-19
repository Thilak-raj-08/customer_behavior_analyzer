import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("customer_behavior_data.csv")
print(df.head(5))
print(df.shape)
df.info()

plt.scatter(df["Income"], df["Purchase_Amount"])
plt.title("Income vs Purchase Amount")
plt.xlabel("Income")
plt.ylabel("Purchase Amount")
plt.show()

plt.hist(df["Age"], bins=10, edgecolor="black")
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

plt.hist(df["Purchase_Amount"], bins=20, edgecolor="black")
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount")
plt.ylabel("Number of Customers")
plt.show()

plt.scatter(df["Website_Visits"], df["Purchase_Amount"])
plt.title("Website Visits vs Purchase Amount")
plt.xlabel("Website Visits")
plt.ylabel("Purchase Amount")
plt.show()

print(df["Purchase_Amount"].describe())

q1 = df["Purchase_Amount"].quantile(0.25)
q3 = df["Purchase_Amount"].quantile(0.75)
iqr = q3 - q1
print(q1)
print(q3)
print(iqr)

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr
print(lower_limit)
print(upper_limit)


outlier_mask = (
    (df["Purchase_Amount"] < lower_limit)
    | (df["Purchase_Amount"] > upper_limit)
)
outliers = df[outlier_mask]
print(outliers)
print("Possible Outliers:", outlier_mask.sum())


income_purchase_correlation = df["Income"].corr(df["Purchase_Amount"])
print(income_purchase_correlation)

visits_purchase_correlation = df["Website_Visits"].corr(df["Purchase_Amount"])
print(visits_purchase_correlation)


df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 30, 45, 60, 75],
    labels=["18–30", "31–45", "46–60", "61–75"]
)
print(df[["Age", "Age_Group"]].head())

age_group_spending = df.groupby(
    "Age_Group", observed=True
)["Purchase_Amount"].mean()

print(age_group_spending)
highest_spending_group = age_group_spending.idxmax()
print("Highest Spending Age Group:", highest_spending_group)
print("Average Purchase:", age_group_spending.loc[highest_spending_group])