import random
import uuid

from car import Car
from database import Database


class Car_Market:
    def __init__(self, data, car_park_file, seller_file):
        self.car_park_file = car_park_file
        self.seller_file = seller_file
        self.car_park = data.read_data(self.car_park_file)
        self.seller = data.read_data(self.seller_file)
        self.data = data
        self.discount = 0

    def car_add(self, car_obj,seller_obj):
        sel_db = self.data.read_data(self.seller_file)
        # l = []
        # for i in range(len(sel_db)):
        #     l.append(i)

        # self.car_park[str(uuid.uuid1())] = {'Mark': car_obj.mark,
        #                                     'Model': car_obj.model,
        #                                     'Color': car_obj.color,
        #                                     'Price': car_obj.price,
        #                                     'Seller': sel_db[f"{random.randint(1, (len(l)))}"]
        #                                     }
        # self.data.write_data(self.car_park, self.car_park_file)

        self.car_park[str(uuid.uuid1())] = {'Mark': car_obj.mark,
                                            'Model': car_obj.model,
                                            'Color': car_obj.color,
                                            'Price': car_obj.price,
                                            'Seller': {"name": seller_obj.name,
                                                       "surname": seller_obj.surname,
                                                       "city": seller_obj.city
                                                      }
                                            }

        # self.car_park[str(uuid.uuid1())] = {'Mark': car_obj.mark,
        #                                     'Model': car_obj.model,
        #                                     'Color': car_obj.color,
        #                                     'Price': car_obj.price,
        #                                     }
        # self.data.write_data(self.car_park, self.car_park_file)

    def remove_car(self):
        pass

    def set_discount(self):
        pass

    def get_car_available_discount(self):
        pass

    def get_seller_available_cars(self):
        pass

    def get_sold_car_history(self):
        pass

    def return_car(self):
        pass


# if __name__ == '__main__':
#     file = "car_park.json"
#     file2 = "seller.json"
#     c = Car("BMW", "E60", "Black", 780000)
#     c1 = Car("Mercedes", "S220", "white", 2012220)
#     db = Database()
#     cm = Car_Market(db, file, file2)
#     cm.car_add(c)
#     cm.car_add(c1)
