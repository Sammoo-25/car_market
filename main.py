from car import Car
from car_market import Car_Market
from database import Database
from seller import Seller
import json
car_par_f = "car_park.json"
sell_f = 'seller.json'
dt = Database()
car_market = Car_Market(dt, car_par_f, sell_f)
if __name__ == '__main__':
    while True:
        action = input("Enter the action 'add', 'sell','exit': ")
        if action == "add":
            while True:
                acction_adding = input("Enter 'S' for adding sellers 'C' for adding cars 'exit' for stop: ")
                if acction_adding == "S":
                    seller_name = input("Name: ")
                    seller_surname = input("Surname: ")
                    seller_city = input("City: ")
                    seller = Seller(seller_name, seller_surname, seller_city, dt, sell_f)
                    seller.add_info(sell_f)
                if acction_adding == "C":
                    car_mark = input("Enter mark of car: ")
                    car_model = input("Enter model of car: ")
                    car_color = input("Enter color of car: ")
                    car_price = int(input("Enter price of car: "))
                    car = Car(car_mark, car_model, car_color, car_price)
                    car_market.car_add(car,seller)
                if acction_adding == "exit":
                    break
        if action == "exit":
            break