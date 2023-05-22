from car import Car
from car_market import Car_Market
from database import Database
from seller import Seller

car_par_f = "car_park.json"
sell_f = 'seller.json'
dt = Database()
car_market = Car_Market(dt, car_par_f, sell_f)
if __name__ == '__main__':
    while True:
        action = input("Enter the action 'add', 'sell','exit': ")
        if action == "add":
            car_mark = input("Enter mark of car: ")
            car_model = input("Enter model of car: ")
            car_color = input("Enter color of car: ")
            car_price = int(input("Enter price of car: "))
            car_date = int(input("Enter date of car: "))
            car = Car(car_mark, car_model, car_color, car_price, car_date)
            car_seller = Seller(input("Enter Saller name: "), input("Enter Saller surname: "),
                                input("Enter Saller city: "), dt, sell_f)
            car_market.car_add(car, car_seller)
            car_seller.add_info(sell_f)
            car_market.set_discount()
            # car_market.get_car_available_discount()
        if action == "exit":
            break

