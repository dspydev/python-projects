import matplotlib.pyplot as plt

# Define the inventory of items available for purchase.
# Each item is a dictionary with a description and a price.

inventory = {
    "Lovely Loveseat": {
        "description": "Tufted polyester blend on wood.",
        "price": 254.00
    },
    "Stylish Settee": {
        "description": "Faux leather on birch.",
        "price": 180.50
    },
    "Luxurious Lamp": {
        "description": "Glass and iron. 36 inches tall. Brown with cream shade.",
        "price": 52.15
    }
}

# Create a bar chart to visualize the sales for each item.

item_names = list(inventory.keys())
item_prices = [inventory[item]['price'] for item in item_names]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(item_names, item_prices, color=['#8E44AD', '#3498DB', '#2ECC71'])
ax.set_title('Sales by Item', fontsize=18)
ax.set_xlabel('Item', fontsize=14)
ax.set_ylabel('Sales ($)', fontsize=14)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)
ax.set_axisbelow(True)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add labels to the bars.

for i, v in enumerate(item_prices):
    ax.text(i, v + 5, "${:.2f}".format(v), ha='center', fontsize=12)

# Add a caption to the chart.

ax.text(-0.5, -80, "Sales by Item: Lovely Loveseat is the best-selling item", fontsize=12, fontstyle='italic', 
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.5))

# Show the chart.

plt.show()
