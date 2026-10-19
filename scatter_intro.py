import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7]
marks = [40, 50, 45, 65, 70, 80, 85]

plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

ages = [18, 20, 22, 25, 25, 28, 30, 32, 35, 35, 40, 42, 45, 50, 60]
plt.hist(ages, bins=5, edgecolor="black")
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

purchase_amounts = [1000, 1200, 1500, 1600, 1800, 2000, 2200, 2500, 3000, 25000]
plt.hist(purchase_amounts, bins=5, edgecolor="black")
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount")
plt.ylabel("Number of Customers")
plt.show()