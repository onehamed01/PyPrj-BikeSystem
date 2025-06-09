# Bike Rental System CLI

This is a simple command-line bike rental system built with Python.

## Description

This CLI-based Python application allows users to:

* Rent bikes on an hourly, daily, or weekly basis
* Return previously rented bikes
* View rental prices and available discounts

It demonstrates basic Object-Oriented Programming (OOP) principles in Python.

## Features

* Tracks available bike stock
* Calculates price based on rental duration and quantity
* Offers a 30% discount for family rentals (3 to 5 bikes)
* Menu-driven interface using basic CLI input/output

## Branches

* `main`: contains the latest, improved version of the CLI-based bike rental system
* `demo`: holds the earlier, basic implementation for comparison and reference

## Run the Project

Make sure you have Python 3 installed.

```bash
python3 BikeSystemAppCLI.py
```

## Price Table

| Period | Price per Bike |
| ------ | -------------- |
| Hourly | £5             |
| Daily  | £10            |
| Weekly | £60            |

> Family rentals (3 to 5 bikes) receive a 30% discount on the total price.

## Roadmap

This project is intended to grow in complexity:

* ✅ Basic CLI version (current)
* 🔜 Web version using Flask (future)
* 🔜 Add persistent storage (e.g., SQLite or JSON)

## License

This is a personal learning project and is provided "as is."
