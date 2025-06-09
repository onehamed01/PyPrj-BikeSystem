class BikeSystem:
    bikes_stock = 10
    def __init__(self, count_bikes):
        self.bike_count = count_bikes
        self.type_rent = {
            'hour':5,
            'day':20,
            'week':60
        }

    def rentBike(self, type_rent, count_type_rent):
        if self.bike_count > self.bikes_stock:
            print(f"you need to rent less than {self.bikes_stock}")
        if type_rent not in self.type_rent:
            print("Invalid Type rent")
            return

        calculate_price = lambda base_price: base_price * 0.7 if 3 <= self.bike_count <= 5 else base_price
        base_price = self.type_rent[type_rent] * count_type_rent * self.bike_count
        total_price = calculate_price(base_price)
        print(f"you have rented {self.bike_count} Bikes, for {count_type_rent} {type_rent}\ntotal price is {total_price} £")

    def returnBike(self, count_return_bikes):
        if count_return_bikes != self.bike_count:
            print("you didn't return all bikes")
        else:
            self.bikes_stock += count_return_bikes
            print("Thank you for your return")
        
