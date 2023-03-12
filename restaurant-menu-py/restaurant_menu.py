# Menu Class

# Menu class represents a restaurant menu
class Menu:
    # Constructor initializes name, items, start_time, and end_time properties
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # __repr__ method returns a string representation of the menu
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    # calculate_bill method calculates the bill for a list of purchased items
    def calculate_bill(self, purchased_items):
        bill = 0
        item_counts = {}

        # Iterate over the purchased items and count the number of each item
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                if purchased_item not in item_counts:
                    item_counts[purchased_item] = 1
                else:
                    item_counts[purchased_item] += 1
            else:
                # If an item is not in the menu, print an error message
                print(f"Sorry, we don't have {purchased_item} on the menu.")

        # Iterate over the counted items and add up the prices
        for item, count in item_counts.items():
            bill += self.items[item] * count

        return bill

    # add_item method adds a new item to the menu's items dictionary
    def add_item(self, name, price):
        self.items[name] = price

# Franchise Class

# Franchise class represents a restaurant franchise
class Franchise:
    # Constructor initializes address and menus properties
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # __repr__ method returns a string representation of the franchise
    def __repr__(self):
        return f"Franchise at {self.address}"

    # available_menus method returns a list of menus that are available at a given time
    def available_menus(self, time):
        available_menus = []

        # Iterate over the menus and check if they are available at the given time
        for menu in self.menus:
            if time >= menu.start_time and time < menu.end_time:
                available_menus.append(menu)

        return available_menus

    # add_menu method adds a new menu to the franchise's menus list
    def add_menu(self, menu):
        self.menus.append(menu)

    # remove_menu method removes a menu from the franchise's menus list
    def remove_menu(self, menu):
        self.menus.remove(menu)

# Business Class

# Business class represents a restaurant business
class Business:
    # Constructor initializes name and franchises properties
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    # __repr__ method returns a string representation of the business
    def __repr__(self):
        return f"{self.name} Business"

    # total_revenue method calculates the total revenue for the business
    def total_revenue(self):
        total = 0

        # Iterate over the franchises, menus, and items to calculate the total revenue
        for franchise in self.franchises:
            for menu in franchise.menus:
                for item_price in menu.items.values():
                    total += item_price

        return total

# Menus

# Define menu items as dictionaries with item names as keys and item prices as values
brunch_items = {
    "pancakes": 7.50,
    "waffles": 9.00,
    "burger": 11.00,
    "home fries": 4.50,
    "coffee": 1.50,
    "espresso": 3.00,
    "tea": 1.00,
    "mimosa": 10.50,
    "orange juice": 3.50,
}

early_bird_items = {
    "salumeria plate": 8.00,
    "salad and breadsticks (serves 2, no refills)": 14.00,
    "pizza with quattro formaggi": 9.00,
    "duck ragu": 17.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 1.50,
    "espresso": 3.00,
}

dinner_items = {
    "crostini with eggplant caponata": 13.00,
    "ceaser salad": 16.00,
    "pizza with quattro formaggi": 11.00,
    "duck ragu": 19.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 2.00,
    "espresso": 3.00,
}

kids_items = {
    "chicken nuggets": 6.50,
    "fusilli with wild mushrooms": 12.00,
    "apple juice": 3.00,
}

arepas_items = {
    "arepa pabellon": 7.00,
    "pernil arepa": 8.50,
    "guayanes arepa": 8.00,
    "jamon arepa": 7.50,
}

# Create Menu objects for each menu type, passing in the corresponding item dictionary and operating hours
brunch_menu = Menu("Brunch", brunch_items, 11, 16)
early_bird_menu = Menu("Early Bird", early_bird_items, 15, 18)
dinner_menu = Menu("Dinner", dinner_items, 17, 23)
kids_menu = Menu("Kids", kids_items, 11, 21)

# Create a list of all the menu objects
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# Create a Menu object for a new menu type
arepas_menu = Menu("Take a' Arepa", arepas_items, 10, 20)

# Franchises

# Create Franchise objects for each location, passing in the address and list of available menus
flagship_address = "1232 West End Road"
flagship_menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise(flagship_address, flagship_menus)

installment_address = "12 East Mulberry Street"
installment_menus = [brunch_menu, early_bird_menu, kids_menu, dinner_menu]
new_installment = Franchise(installment_address, installment_menus)

arepas_address = "189 Fitzgerald Avenue"
arepas_place = Franchise(arepas_address, [arepas_menu])

# Businesses

# Create Business objects for each restaurant brand, passing in the name and list of Franchise objects
Basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
Arepa = Business("Take a' Arepa", [arepas_place])

# Testing code to verify the functionality of the classes

# Adding a new item to the brunch menu
brunch_menu.add_item("juice", 2.50)
print("\n*** Updated brunch menu items ***")
for item, price in brunch_menu.items.items():
    print(f"{item}: ${price}")

# Removing the kids menu from the new installment Franchise object
print("\n*** Menus at new installment franchise before and after removing kids menu ***")
print("Before:")
for menu in new_installment.menus:
    print(menu)
new_installment.remove_menu(kids_menu)
print("\nAfter:")
for menu in new_installment.menus:
    print(menu)

# Printing the available menus at the flagship store at noon
print("\n*** Menus available at flagship store at 12pm ***")
for menu in flagship_store.available_menus(12):
    print(menu)

# Printing the total revenue for each Business object
print("\n*** Total revenue ***")
print("Basta Fazoolin' with my Heart: ${:.2f}".format(Basta.total_revenue()))
print("Take a' Arepa: ${:.2f}".format(Arepa.total_revenue()))
