
class Product:
    count = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
    
    def get_info(self): # Instance Method
        print(f"Price of {self.name} is {self.price}")
        
    @classmethod
    def get_count(cls):
        print(f"Total products in store: {cls.count}")
    
    @staticmethod
    def get_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"Discounted Price: {final_price}")
        
    
p1 = Product("Phone", 15000)
p2 = Product("Laptop", 50000)
p1.get_info()
p1.get_count()
p1.get_discount(50000, 10)