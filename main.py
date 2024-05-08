class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_date and time <= menu.end_date:
                available_menus.append(menu)
        return available_menus


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Menu:
    def __init__(self, name, items, start_date, end_date):
        self.name = name
        self.items = items
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.name} menu available from {self.start_date} to {self.end_date}"

    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            if item in self.items:
                bill += self.items[item]
        return bill

# Define menu items outside the class definition
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
    'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50,
    'orange juice': 3.50
}
early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

# Create menu instances
brunch_menu = Menu("Brunch", brunch_items, 100, 1600)
early_bird_menu = Menu("Early-bird", early_bird_items, 1500, 1800)
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
kids_menu = Menu("Kids", kids_items, 1100, 2100)

# Create a list of menus
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

# Create Franchise instances
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# Print available menus at a certain time
print(flagship_store.available_menus(1200))

# Create Business instance
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Define Arepas menu items and franchise
arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Arepas", arepas_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepa = Business("Take a' Arepa", [arepas_place])
