import uuid

from buyer import Buyer
from car import Car
from database import Database
from seller import Seller


class Car_Market:
    def __init__(self, data, car_park_file, seller_file):
        self.car_park_file = car_park_file
        self.seller_file = seller_file
        self.car_park = data.read_data(self.car_park_file)
        self.sellers = data.read_data(self.seller_file)
        self.data = data
        self.discount = 0

    def car_add(self, car_obj, car_seller):
        self.car_park[str(uuid.uuid4())] = {'Mark': car_obj.mark,
                                            'Model': car_obj.model,
                                            'Color': car_obj.color,
                                            'Price': car_obj.price,
                                            'Date': car_obj.date,
                                            'Discount': car_obj.discount,
                                            'Seller': {'name': car_seller.name,
                                                       'surname': car_seller.surname,
                                                       'city': car_seller.city
                                                       }
                                            }
        self._set_discount(car_obj)
        self.data.write_data(self.car_park, self.car_park_file)

    # 33 150 + 85 519 + 85 519
    def remove_car(self, car_id):
        if car_id in self.car_park:
            del self.car_park[car_id]
            self.data.write_data(self.car_park, self.car_park_file)
        else:
            raise KeyError

    def _set_discount(self, car_obj):
        if isinstance(car_obj.discount, (int, float)):
            for car_m in self.car_park.values():
                if car_obj.mark == car_m['Mark']:
                    car_m['Discount'] = 15
            self.data.write_data(self.car_park, self.car_park_file)
        else:
            raise ValueError
        # self.data.write_data(self.car_park, self.car_park_file)
        # data = self.data.read_data(self.car_park_file)
        # for car_data in data.values():
        #     if car_data['Date'] > 1990 and car_data['Date'] < 2003:
        #         car_data['Discount'] = 15
        #     elif car_data['Date'] > 2004 and car_data['Date'] < 2012:
        #         car_data['Discount'] = 5
        # self.car_park = data
        # self.data.write_data(self.car_park, self.car_park_file)

    def get_car_available_discount(self):
        pass
        # count = 0
        # data = self.data.read_data(self.car_park_file)
        # for car_data in data.values():
        #     if car_data['Discount'] > 0:
        #         print(car_data)

    def _get_seller_available_cars(self, sellers_file, cars_file):
        sel_data = self.data.read_data(sellers_file)
        car_data = self.data.read_data(cars_file)
        for sell_info in sel_data.values():
            for car_info in car_data.values():
                if sell_info["name"] in car_info['Seller'].values():
                    print(car_info)

    def __get_sold_car_history(self):
        pass

    def return_car(self):
        pass


if __name__ == '__main__':
    car_file = "car_park.json"
    sell_file = "seller.json"
    seller_bank = "seller_bank.json"
    seller_sold_cars = 'sold_cars.json'
    buyed_cars = 'bought_cars.json'
    buyer_bank = 'buyer_bank.json'
    db = Database()

    car = Car('BMW', "E60", "Black", 500000, 2012)
    car1 = Car("Mercedes", "S220", "white", 500000, 1990)
    car2 = Car("Kia", "Optima", "white", 500000, 2010)
    # car3 = Car("BMW", "E525", "Grey", 2012220, 2010)
    # car4 = Car("Mercedes", "CLS", "red", 2012220, 2010)
    # car5 = Car("Kia", "Forte", "Black", 2012220, 2010)
    car6 = Car("Toyota", "Corola", "white", 500000, 2020)
    # car7 = Car("BMW", "X5", "white", 32100000, 2018)

    cm = Car_Market(db, car_file, sell_file)

    sel1 = Seller("Vaspur", "Manucharyan", "Gyumri", db, cm, sell_file, seller_bank, seller_sold_cars)
    sel2 = Seller("Hasmik", "Apresyan", "Vanadzor", db, cm, sell_file, seller_bank, seller_sold_cars)
    # sel3 = Seller("Vazgen", "kirakosyan", "Lori", db, cm, sell_file, seller_bank, seller_sold_cars)
    # sel4 = Seller("Hmalet", "Abrahamyan", "Yerevan", db, cm, sell_file, seller_bank, seller_sold_cars)

    cm.car_add(car, sel1)
    cm.car_add(car1, sel2)
    # cm.car_add(car4, sel3)
    # cm.car_add(car5, sel4)
    # cm.car_add(car6, sel4)
    # cm.car_add(car7, sel3)
    cm.car_add(car2, sel2)
    cm.car_add(car6, sel1)

    sel1.add_info(car_file)
    sel2.add_info(car_file)
    # sel3.add_info(car_file)
    # sel4.add_info(car_file)

    buy1 = Buyer("Manuk", "Avetisyan", "Moscow", db, buyed_cars, buyer_bank, seller_sold_cars)
    buy2 = Buyer("James", "Madison", "London", db, buyed_cars, buyer_bank, seller_sold_cars)

    # sel1.sell(car, buy1)
    buy1.buy(car, sel1)
    buy1.buy(car6, sel1)
    # sel2.sell(car2, buy2)
    # sel1.sell(car6, buy2)
