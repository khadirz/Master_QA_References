"""
28 - OOP: Class and Object
Class is a blueprint.
Object is a real thing created from the class.
"""

# Create a class called ShoppingCart.
# A class is like a blueprint for creating shopping cart objects.
class ShoppingCart:

    # This method runs automatically when we create a new ShoppingCart.
    def __init__(self, owner):
        # Store the cart owner's name.
        self.owner = owner

        # Create an empty list to store the cart items.
        self.items = []

    # Create a method to add an item to the cart.
    def add_item(self, item):
        # Add the item to the items list.
        self.items.append(item)

        print(f"{item} added to {self.owner}'s cart")

    # Create a method to show all items in the cart.
    def show_items(self):
        print(f"{self.owner}'s cart contains: {self.items}")


# Create a shopping cart object for User A.
user_a_cart = ShoppingCart("User A")

# Create another shopping cart object for User B.
user_b_cart = ShoppingCart("User B")

# Add Laptop to User A's cart.
user_a_cart.add_item("Laptop")

# Add Phone to User B's cart.
user_b_cart.add_item("Phone")

# Show items in User A's cart.
user_a_cart.show_items()

# Show items in User B's cart.
user_b_cart.show_items()
