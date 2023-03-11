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

# Define the sales tax rate as a decimal.

sales_tax_rate = 0.088

# Define a function to calculate the sales tax on a given amount.
# The sales tax rate is a global variable defined above.

def calculate_sales_tax(amount):
    # Multiply the amount by the sales tax rate and round to two decimal places.
    return round(amount * sales_tax_rate, 2)

# Define the customer's purchases as a list of item names.

customer_purchases = ["Lovely Loveseat", "Luxurious Lamp"]

# Initialize the customer's itemization and total as empty strings.

customer_itemization = ""
customer_subtotal = 0

# Iterate over the customer's purchases and update the itemization and subtotal.
# For each item, add its name, description, and price to the itemization string,
# and add its price to the subtotal.

for item in customer_purchases:
    # Add the item, description, and price to the customer's itemization.
    item_price = inventory[item]['price']
    customer_itemization += f"| {item:25} | ${item_price:>7.2f} |\n"
    customer_itemization += f"| {' ' * 3}{inventory[item]['description']:45} |\n"
    # Add the item's price to the customer's subtotal.
    customer_subtotal += item_price

# Calculate the sales tax on the customer's subtotal.

sales_tax = calculate_sales_tax(customer_subtotal)

# Add the sales tax to the customer's subtotal to get the final price.

customer_total = customer_subtotal + sales_tax

# Print the customer's receipt, including the itemization, subtotal, sales tax, and total.

print("\n" + "=" * 45)
print("     FURNITURE STORE")
print("=" * 45 + "\n")

print(f"{'Item':25}   {'Price':>10}")
print("-" * 45)
print(customer_itemization)
print("-" * 45)
print(f"{'Subtotal:':<25}   ${customer_subtotal:>7.2f}")
print(f"{'Sales Tax @8.8%:':<25}   ${sales_tax:>7.2f}")
print(f"{'Total:':<25}   ${customer_total:>7.2f}")
print("\n" + "=" * 45)
print("     THANK YOU FOR SHOPPING WITH US!")
print("=" * 45 + "\n")
