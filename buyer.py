import datetime
import random
import uuid

from person import Person


class Buyer(Person):
    def __init__(self, name, surname, city, data_obj, bought_cars_fname, buyer_bank_file, sell_sold_cars_file,
                 buyers_cars_park_file):
        super().__init__(name, surname, city)
        self.data = data_obj
        self.bought_cars_fname = bought_cars_fname
        self.bought_cars = data_obj.read_data(self.bought_cars_fname)

        self.buyer_bank_file = buyer_bank_file
        self.money = data_obj.read_data(self.buyer_bank_file)
        self.__spent_money = 0

        self.sell_sold_cars_file = sell_sold_cars_file
        self.sold_cars = self.data.read_data(self.sell_sold_cars_file)

        self.buyers_cars_park_file = buyers_cars_park_file
        self.buyers_car_park = self.data.read_data(buyers_cars_park_file)

        self.buyer_id = str(uuid.uuid4())
        # self._add_info()
        self._buyers_bank()

    def _add_info(self):
        self.buyers_car_park[self.buyer_id] = {'name': self.name,
                                               'surname': self.surname,
                                               'city': self.city,
                                               'cars': []
                                               }
        self.data.write_data(self.buyers_car_park, self.buyers_cars_park_file)

    def _add_buyers_car(self, car_obj):
        data = self.data.read_data(self.bought_cars_fname)
        buyer_data = self.data.read_data(self.buyers_cars_park_file)

        for item in data.get('cars', []):
            if isinstance(item, dict) and 'Car_id' in item and item['Car_id'] == car_obj.car_id:
                car = {
                    'Car_id': car_obj.car_id,
                    'Mark': car_obj.mark,
                    'Model': car_obj.model,
                    'Color': car_obj.color,
                    'Price': car_obj.price,
                    'Date': car_obj.date,
                    'Discount': car_obj.discount,
                }

                buyer_id = item['Buyer']['name'] + '_' + item['Buyer']['surname']
                if buyer_id in buyer_data:
                    buyer_data[buyer_id]['cars'].append(car)
                else:
                    buyer_data[buyer_id] = {'cars': [car]}

        self.data.write_data(buyer_data, self.buyers_cars_park_file)

    def buy(self, car_obj, seller):
        data = self.data.read_data(self.bought_cars_fname)
        day_time = str(datetime.date.today())

        bought_car = {
            'Car_id': car_obj.car_id,
            'Mark': car_obj.mark,
            'Model': car_obj.model,
            'Color': car_obj.color,
            'Price': car_obj.price,
            'Date': car_obj.date,
            'Buyer': {
                'name': self.name,
                'surname': self.surname,
                'city': self.city
            },
            'Seller': {
                'name': seller.name,
                'surname': seller.surname,
                'city': seller.city
            },
            'data': day_time
        }

        if 'cars' in data:
            data['cars'].append(bought_car)
        else:
            data['cars'] = [bought_car]

        self.__change_money(car_obj, 'm')
        self.data.write_data(data, self.bought_cars_fname)
        seller.sell(car_obj)
        self._add_buyers_car(car_obj)

    def _plus_money(self, car_obj):
        ##return time
        data_money = self.money[self.name]['Balance']
        if isinstance(data_money, (int, float)):
            data_money = int(data_money) + car_obj.price  # Convert data_money to an integer
            self.money[self.name]['Balance'] = data_money
            self.data.write_data(self.money, self.buyer_bank_file)
        return self.money

    def _minus_money(self, car_obj):
        ##buy
        data_money = self.money[self.name]['Balance']
        if isinstance(data_money, (int, float)):
            data_money = int(data_money) - car_obj.price  # Convert data_money to an integer
            self.money[self.name]['Balance'] = data_money
            self.money[self.name]['Spent money'] = car_obj.price
            self.data.write_data(self.money, self.buyer_bank_file)
        return self.money

    def __change_money(self, car_obj, action):
        if action == "p":
            ##return
            self.money[self.name]['Balance'] = self._plus_money(car_obj)
        elif action == "m":
            ##buy
            self.money[self.name]['Balance'] = self._minus_money(car_obj)
        else:
            raise ValueError

    def _buyers_bank(self):
        data = self.data.read_data(self.buyer_bank_file)
        data[self.name] = {'Balance': random.randint(2500000, 10000000),
                           'Spent money': 0
                           }
        self.money = data

        self.data.write_data(self.money, self.buyer_bank_file)

    def print_my_cars(self):
        buyer_cars = self.data.read_data(self.buyers_cars_park_file)
        name_surname = self.name + "_" + self.surname
        if name_surname in buyer_cars:
            cars = buyer_cars[name_surname]['cars']
            if cars:
                print("Your cars:")
                for car in cars:
                    print(f"Car ID: {car['Car_id']}")
                    print(f"Mark: {car['Mark']}")
                    print(f"Model: {car['Model']}")
                    print(f"Color: {car['Color']}")
                    print(f"Price: {car['Price']}")
                    print(f"Date: {car['Date']}")
                    print(f"Discount: {car['Discount']}")
                    print("------------------------")
            else:
                print("You have no cars.")
        else:
            print("You have no cars.")

    #
    # def return_car(self, car_obj):
    #     buyers_cars_park = self.data.read_data(self.buyers_cars_park_file)
    #     seller_car_park = self.data.read_data(self.seller_car_park_file)
    #     car_park = self.data.read_data(self.car_park_file)
    #
    #     if buyer_name in buyers_cars_park:
    #         buyer = buyers_cars_park[buyer_name]
    #         for car in buyer['cars']:
    #             if car['Car_id'] == car_id:
    #                 seller_id = car_id.split('-')[0]  # Extract the seller ID from the car ID
    #                 if seller_id in seller_car_park:
    #                     seller = seller_car_park[seller_id]
    #                     seller['cars'].append(car)  # Add the car back to the seller's car list
    #                     self.data.write_data(seller_car_park, self.seller_car_park_file)
    #                 car_park[car_id] = car  # Add the car back to the car park
    #                 self.data.write_data(car_park, self.car_park_file)
    #                 buyer['cars'].remove(car)  # Remove the car from the buyer's car list
    #                 self.data.write_data(buyers_cars_park, self.buyers_cars_park_file)
    #                 return True  # Car successfully returned
    #     return False  # Car or buyer not found
