class BikeSystemCLI:
    bikeStock = 10

    pricePeriodBikes = {
        'hourly': 5,
        'daily':10,
        'weekly': 60
    }

    def __init__(self):
        self.rented_bikes = 0

    def _rentBike(self):
        while True:

            try:
                count = int(input("How many Bikes you want Rent: "))
            except ValueError:
                print("Invalid Input! Enter numbers", end="\n")
                continue

            if count > BikeSystemCLI.bikeStock:
                print(f"Sorry! we just have {BikeSystemCLI.bikeStock} Bikes", end="\n")
                continue

            if BikeSystemCLI.bikeStock == 0:
                print("We Don't have Enought Bikes in Stocks. Please Try later!")
                break

            BikeSystemCLI.bikeStock -= count
            self.rented_bikes += count

            break

    def _periodRent(self):
        while True:
            self.period_rent = input("Rental Period (hourly, daily, weekly): ")
            if self.period_rent not in BikeSystemCLI.pricePeriodBikes:
                print("Invalid input! please choose (hourly, daily, weekly)", end="\n")
                continue
            
            try:
                self.period_count_rent = int(input(f"How many {self.period_rent} you want: "))
            except ValueError:
                print("Please Enter the Number!", end="\n")
                continue
        
            break
        print(f"\nYou have Rented {self.rented_bikes} for {self.period_count_rent} {self.period_rent}\nTotal Price: {self.__calculateRent()}£", end="\n")

    def __calculateRent(self):
        base_price = self.period_count_rent * self.rented_bikes * BikeSystemCLI.pricePeriodBikes[self.period_rent]

        if 3 <= self.period_count_rent <= 5:
            base_price = base_price * 0.7
            base_price = float(f"{base_price:.2f}")
            return base_price
        
        return float(base_price)

    def _returnBike(self):
        while True:
            try:
                return_bike = int(input(f"You have rented {self.rented_bikes} Bikes\nHow many of them you want return: "))
            except ValueError:
                print("Invalid Input! Enter the number", end="\n")
                continue
            if return_bike > self.rented_bikes or return_bike == 0:
                print("Invalid number! please Enter equal or less than Bikes (except 0) you have!", end="\n")
                continue

            self.rented_bikes += return_bike
            break

        print("Thank you for your Return:)", end="\n")

    def _prices(self):
        for k,v in BikeSystemCLI.pricePeriodBikes.items():
            print(f"{k} is {v}£")

        print("you can get 30% discount for Family renting Between 3 to 5 Bikes.")
        return


    def run(self):
        print("**Welcome To Bike Rental System as CLI version 1.0**")


        while True:
            print("Please Enter on of the options")
            print("1. Rent Bikes")
            print("2. Return Bikes")
            print("3. Check Prices for each Bike")
            print("0. Exit")
            
            try:
                option = int(input("Enter: "))
            except ValueError:
                print("please Enter 1, 2, 3 or 0", end="\n")
                continue

            if option == 1:
                self._rentBike()
                self._periodRent()

            elif option == 2:
                self._returnBike()

            elif option == 3:
                self._prices()
            
            elif option == 0:
                print("Thank you!")
                break
            else:
                print("please Choose 1, 2, 3 or 0", end='\n')


if __name__ == "__main__":
    cli = BikeSystemCLI()
    cli.run()