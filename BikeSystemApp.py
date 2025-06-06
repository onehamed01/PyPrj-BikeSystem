class BikeSystem:
    def __init__(self, count_bikes):
        self.bike_count = count_bikes
        self.type_rent = {
            'hour':5,
            'day':20,
            'week':60
        }
        self.bikes_stock = 10

    @property
    def viewStock(self):
        print("total Bikes:",self.bikes_stock) 

    def rentBike(self, type_rent, count_type_rent):
        while True:
            if self.bike_count > self.bikes_stock:
                print(f"you need to rent less than {self.bikes_stock}")
            else:
                break

        total_price = self.type_rent[type_rent] * count_type_rent * self.bike_count
        if 3 <= self.bike_count <= 5: 
            total_price = 0.30 * total_price

        self.bikes_stock -= self.bike_count
        print(f"you have rented {self.bike_count} Bikes, for {count_type_rent} {type_rent}\ntotal price is {total_price} £")
        print(f"total Bikes: {self.bikes_stock}")

    def returnBike(self, count_return_bikes):
        if count_return_bikes != self.bike_count:
            print("you didn't return all bikes")
        else:
            self.bikes_stock += count_return_bikes
            print("Thank you for your return")
        

