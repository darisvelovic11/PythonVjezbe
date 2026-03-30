class Cart():
    def __init__(self, owner):
        self.owner = owner
        self.items =[]
    def add_item(self , name, price):
        return self.items.append({
            "name":name,
            "price":price
        })
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        total = sum(item['price'] for item in self.items)
        return f"{self.owner}'s cart: {len(self.items)} items, total &{total:2f}"
    
    def __contains__(self, name):
        return any(item['name']==name for item in self.items)
    
    def __add__(self,other):
        new_cart = Cart("merged")
        new_cart.items = self.items + other.items
        return new_cart
    
cart1 = Cart("Daris")
cart1.add_item("Apple", 1.5)
cart1.add_item("Bread", 2.0)

cart2 = Cart("Ana")
cart2.add_item("Milk", 1.0)

print(len(cart1))           # 2
print(cart1)                # Daris's cart: 2 items, total $3.50
print("Apple" in cart1)     # True
print("Milk" in cart1)      # False

merged = cart1 + cart2
print(merged)               # merged's cart: 3 items, total $4.50

    
