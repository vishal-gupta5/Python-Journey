class Laptop:
    stroage_type = "ssd"

    def __init__(self, RAM, stroage):
        self.RAM = RAM
        self.stroage = stroage
    
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.stroage_type}")
        
    def get_info(self): #Instance Method
        print(f"Laptop has {self.RAM}, {self.stroage} & {self.stroage_type}")
            
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discounted Price: {final_price}")

l1 = Laptop("16gb", "512gb")
l1.get_info()
l1.get_storage_type()
l1.calc_discount(40_000, 10)