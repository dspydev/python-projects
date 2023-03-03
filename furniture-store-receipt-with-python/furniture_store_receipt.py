# Furniture Store

# Define the inventory of items available for purchase.
# Each item is a dictionary with a description and a price.

inventory = {
    "Lovely Loveseat": {
        "description": "Tufted polyester blend on wood.",
        "price": 254
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
customer_total = 0

# Iterate over the customer's purchases and update the itemization and total.
# For each item, add its name and description to the itemization string,
# and add its price to the total.

for item in customer_purchases:
    # Add the item and its description to the customer's itemization.
    customer_itemization += f"{item}: {inventory[item]['description']}\n"
    # Add the item's price to the customer's total.
    customer_total += inventory[item]['price']

# Calculate the sales tax on the customer's total.

sales_tax = calculate_sales_tax(customer_total)

# Add the sales tax to the customer's total to get the final price.

customer_total += sales_tax

# Print the customer's receipt, including the itemization, subtotal, sales tax, and total.

print("\nCUSTOMER RECEIPT\n")
print(f"Itemization:\n{customer_itemization}")
print(f"Subtotal: ${customer_total - sales_tax:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${customer_total:.2f}")
