from buyer import Buyer
from car import Car
from database import Database
from seller import Seller


class Car_Market:
    def __init__(self, data, car_park_file, seller_file, market_bank_file):
        self.car_park_file = car_park_file
        self.seller_file = seller_file
        self.market_bank_file = market_bank_file
        self.car_park = data.read_data(self.car_park_file)
        self.sellers = data.read_data(self.seller_file)
        self.bank = data.read_data(self.market_bank_file)
        self.data = data
        self.discount = 0

        self._car_market_bank_bank()

    def car_add(self, car_obj, seller):
        self.car_park[car_obj.car_id] = {'Mark': car_obj.mark,
                                         'Model': car_obj.model,
                                         'Color': car_obj.color,
                                         'Price': car_obj.price,
                                         'Date': car_obj.date,
                                         'Discount': car_obj.discount,
                                         }
        self._set_discount(car_obj)
        seller.add_sellers_car(car_obj)
        self.data.write_data(self.car_park, self.car_park_file)

    def remove_car(self, car_obj):
        if car_obj.car_id in self.car_park.keys():
            del self.car_park[car_obj.car_id]
            self.data.write_data(self.car_park, self.car_park_file)
        else:
            raise ValueError

    def _set_discount(self, car_obj):
        if isinstance(car_obj.discount, (int, float)):
            for car_m in self.car_park.values():
                if car_obj.mark == car_m['Mark']:
                    car_m['Discount'] = 15
            self.data.write_data(self.car_park, self.car_park_file)
        else:
            raise ValueError

    def _plus_money(self, car_obj):
        self.bank['Balance'] = self.bank['Balance'] + (car_obj.price - car_obj.price * 0.05)
        return self.bank['Balance']

    def _minus_money(self, car_obj):
        self.bank['Balance'] = self.bank['Balance'] - (car_obj.price - car_obj.price * 0.05)
        return self.bank['Balance']

    def _change_money(self, car_obj, action):
        data = self.data.read_data(self.market_bank_file)
        if action == "p":
            data['Balance'] = self._plus_money(car_obj)
            self.bank.update(data)
            self.data.write_data(self.bank, self.market_bank_file)
        elif action == "m":
            data['Balance'] = self._minus_money(car_obj)
            self.bank.update(data)
            self.data.write_data(self.seller_bank, self.market_bank_file)
        else:
            raise ValueError

    def _car_market_bank_bank(self):
        data_bank = {'Balance': 0}
        self.bank = data_bank
        self.data.write_data(self.bank, self.market_bank_file)

    def get_car_available_discount(self, car_obj):
        car_park = self.data.read_data(self.car_park_file)
        if car_obj.car_id in car_park:
            car = car_park[car_obj.car_id]
            return car['Discount']
        else:
            return None

    #
    def _get_seller_available_cars(self, seller):
        seller_car_park = self.data.read_data(seller.seller_car_park_file)
        if seller.seller_id in seller_car_park:
            seller = seller_car_park[seller.seller_id]
            return seller['cars']
        else:
            return []


if __name__ == '__main__':
    car_file = "car_park.json"
    sell_file = "seller_car_park.json"
    seller_bank = "seller_bank.json"
    seller_sold_cars = 'sold_cars.json'
    buyed_cars = 'bought_cars.json'
    buyer_bank = 'buyer_bank.json'
    buyer_car_park = 'buyers_cars_park.json'
    market_bank = "car_market_bank.json"

    db = Database()

    car = Car('BMW', "E60", "Black", 500000, 2012)
    car1 = Car("Mercedes", "S220", "white", 500000, 1990)
    car2 = Car("Kia", "Optima", "white", 500000, 2010)
    # car3 = Car("BMW", "E525", "Grey", 2012220, 2010)
    car4 = Car("Mercedes", "CLS", "red", 2012220, 2010)
    # car5 = Car("Kia", "Forte", "Black", 2012220, 2010)
    car6 = Car("Toyota", "Corola", "white", 500000, 2020)
    # car7 = Car("BMW", "X5", "white", 32100000, 2018)

    cm = Car_Market(db, car_file, sell_file, market_bank)

    sel1 = Seller("Vaspur", "Manucharyan", "Gyumri", db, cm, sell_file, seller_bank, seller_sold_cars)
    sel2 = Seller("Hasmik", "Apresyan", "Vanadzor", db, cm, sell_file, seller_bank, seller_sold_cars)
    # sel3 = Seller("Vazgen", "kirakosyan", "Lori", db, cm, sell_file, seller_bank, seller_sold_cars)
    # sel4 = Seller("Hmalet", "Abrahamyan", "Yerevan", db, cm, sell_file, seller_bank, seller_sold_cars)

    cm.car_add(car, sel1)
    cm.car_add(car6, sel2)
    cm.car_add(car2, sel1)
    cm.car_add(car4, sel2)
    # cm.car_add(car5, sel4)
    # cm.car_add(car7, sel3)

    # sel1.add_info(car_file)
    # sel1.add_info(car_file)
    # sel2.add_info(car_file)
    # sel3.add_info(car_file)
    # sel4.add_info(car_file)

    buy1 = Buyer("Manuk", "Avetisyan", "Moscow", db, buyed_cars, buyer_bank, seller_sold_cars, buyer_car_park)
    buy2 = Buyer("James", "Madison", "London", db, buyed_cars, buyer_bank, seller_sold_cars, buyer_car_park)

    # sel1.sell(car, buy1)
    buy1.buy(car, sel1)
    buy1.buy(car6, sel1)

    # buy1.print_my_cars()
    # print(cm.get_car_available_discount(car))
    # print(cm.get_seller_available_cars(sel1))

    # sel2.sell(car2, buy2)
    # sel1.sell(car6, buy2)
