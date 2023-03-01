# Furniture Store

# Define the items and their descriptions and prices
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

# Define the sales tax rate
sales_tax_rate = 0.088

# Define a function to calculate the sales tax
def calculate_sales_tax(amount):
    return round(amount * sales_tax_rate, 2)

# Define the customer's purchases
customer_purchases = ["Lovely Loveseat", "Luxurious Lamp"]

# Initialize the customer's itemization and total
customer_itemization = ""
customer_total = 0

# Iterate over the customer's purchases and update the itemization and total
for item in customer_purchases:
    customer_itemization += f"{item}: {inventory[item]['description']}\n"
    customer_total += inventory[item]['price']

# Add the sales tax to the total
sales_tax = calculate_sales_tax(customer_total)
customer_total += sales_tax

# Print the customer's receipt
print("\nCUSTOMER RECEIPT\n")
print(f"Itemization:\n{customer_itemization}")
print(f"Subtotal: ${customer_total - sales_tax:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${customer_total:.2f}") 
