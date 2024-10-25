
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, item):
        product = {}
        product["name"] = item.name
        product["price"] = item.price
        product["quantity"] = item.quantity

        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)

    def calculate_total_price(self):
        total = 0
        for product in self.products:
            total += product["price"] * product["quantity"] # total = product_price * product_quantity keep adding until all products are calculated
        return total
    
    def print_cart(self):
        for product in self.products:
            print(f"{product['name']} - {product['price']} - {product['quantity']}")
        

# Create a few products
p1 = Product("MSI Laptop", 300000, 1)
p2 = Product("Pen drive", 1200, 3)
p3 = Product("Mechanical Keyboard", 12500, 2)
p4 = Product("Windows 11 Pro", 15000, 1)

# Create a shopping cart
cart = ShoppingCart()

# Add products to the cart
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.add_product(p4)


# Remove Mechanical Keyboard from the cart
cart.remove_product("Mechanical Keyboard")

# Print cart
cart.print_cart()

# calculate total price
print("\nTotal Price : LKR", cart.calculate_total_price())