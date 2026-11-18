import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch"]
sales = [40, 30, 20, 10]

colors = ["#3498db", "#e67e22", "#2ecc71", "#e74c3c"]

plt.figure(figsize=(8, 6))

plt.pie(
    sales,
    labels=products,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    explode=(0.05, 0, 0, 0),
    shadow=True,
    wedgeprops={"edgecolor": "white"},
)

plt.title("Product-wise Sales Distribution", fontsize=15)

plt.show()
