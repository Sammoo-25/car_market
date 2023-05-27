import uuid

from person import Person


class Seller(Person):
    def __init__(self, name, surname, city, data_obj, car_market, seller_car_park_file, seller_bank_file,
                 sold_cars_fname):
        if type(name) is str and type(surname) is str and type(city) is str:
            super().__init__(name, surname, city)
        self.dat = data_obj
        self.car_market = car_market
        # self.sold_cars_fname = sold_cars_fname
        # self.sold_cars = data_obj.read_data(self.sold_cars_fname)
        self.seller_car_park_file = seller_car_park_file
        self.seller_car_park = data_obj.read_data(self.seller_car_park_file)

        self.sold_cars_fname = sold_cars_fname
        self.sold_cars = data_obj.read_data(self.sold_cars_fname)

        self.seller_bank_file = seller_bank_file
        self.seller_bank = data_obj.read_data(self.seller_bank_file)
        self.money = 0

        self.seller_id = str(uuid.uuid4())
        self._add_info()
        self._sellers_bank()

    def _add_info(self):
        self.seller_car_park[self.seller_id] = {'name': self.name,
                                                'surname': self.surname,
                                                'city': self.city,
                                                'cars': []
                                                }
        self.dat.write_data(self.seller_car_park, self.seller_car_park_file)

    def add_sellers_car(self, car_obj):
        data = self.dat.read_data(self.seller_car_park_file)
        car = {'Car_id': car_obj.car_id,
               'Mark': car_obj.mark,
               'Model': car_obj.model,
               'Color': car_obj.color,
               'Price': car_obj.price,
               'Date': car_obj.date,
               'Discount': car_obj.discount,
               }
        for id, sell in data.items():
            if self.seller_id == id:
                data[self.seller_id]['cars'].append(car)
        self.seller_car_park.update(data)
        # self.seller_car_park = data
        self.dat.write_data(self.seller_car_park, self.seller_car_park_file)

    # def get_available_cars(self):
    #     data = self.seller_info
    #     return data

    def __check_discount(self, car_code):
        if self.seller_car_park[car_code]['Discount']:
            return self.seller_car_park[car_code]['Price'] - (self.seller_car_park[car_code]['Price'] *
                                                              self.seller_car_park[car_code]['Discount'] // 100)
        else:
            return self.seller_car_park[car_code]['Price']

    #
    def sell(self, car_obj):
        data = self.dat.read_data(self.seller_car_park_file)
        for id, value in data.items():
            cars_copy = value['cars'][:]
            for car in range(len(cars_copy)):
                # print(value['cars'][car]['Mark'])
                # print(car_obj.mark)
                if car_obj.mark == cars_copy[car]['Mark']:
                    # print(value['cars'])
                    # print(car)
                    value['cars'].remove(cars_copy[car])
                    self.__change_money(car_obj, "p")
                    self.seller_car_park.update(data)
                    self.dat.write_data(self.seller_car_park, self.seller_car_park_file)
                    self.car_market.remove_car(car_obj)
                    self.add_sold_cars(car_obj)
        # data = self.dat.read_data(self.sold_cars_fname)
        # selles_cars = {}
        # day_time = str(datetime.date.today())
        # for id, car in self.seller_info.items():
        #     if car_obj.mark == car['Mark']:
        #         price = self.__check_discount(id)
        #         selles_cars[id] = car
        #         selles_cars[id]['Price'] = price
        #         selles_cars[id]['data'] = day_time
        #         selles_cars[id]['buyer'] = {'name': buyer.name, 'surname': buyer.surname, 'city': buyer.city}
        #         self.__change_money(car_obj)
        #         data.update(selles_cars)
        #         self.sold_cars = data
        #         self.dat.write_data(self.sold_cars, self.sold_cars_fname)
        #         self.car_market.remove_car(id)

    """
    Money
    """

    def _plus_money(self, car_obj):
        self.money = self.money + (car_obj.price * 0.05)
        return self.money

    def _minus_money(self, car_obj):
        self.money = self.money - (car_obj.price * 0.05)
        return self.money

    def __change_money(self, car_obj, action):
        data = self.dat.read_data(self.seller_bank_file)
        # print(data)
        if action == "p":
            data[self.name]['Balance'] = self._plus_money(car_obj)
            self.seller_bank.update(data)
            self.dat.write_data(self.seller_bank, self.seller_bank_file)
        elif action == "m":
            data[self.name]['Balance'] = self._minus_money(car_obj)
            self.seller_bank.update(data)
            self.dat.write_data(self.seller_bank, self.seller_bank_file)
        else:
            raise ValueError

    # self.money = self.money + (car_obj.price * 0.05)
    # self.seller_bank['Balance'] = self.money
    # self.car_market.bank['Balance'] = car_obj.price - self.money
    # # balance = self.seller_bank
    # # balance['Balance'] = self.money
    # self.dat.write_data(self.car_market.bank, self.car_market.market_bank_file)
    # self.dat.write_data(self.seller_bank, self.seller_bank_file)

    def _sellers_bank(self):
        data = self.dat.read_data(self.seller_bank_file)
        data[self.name] = {'Balance': 0
                           }
        self.seller_bank = data

        self.dat.write_data(self.seller_bank, self.seller_bank_file)

    """
    Money
    """

    def add_sold_cars(self, car_obj):
        sold_cars = self.dat.read_data(self.sold_cars_fname)

        seller_key = f"{self.name}_{self.surname}"  # Generate the key using seller's name and surname

        sold_car = {
            'Car_id': car_obj.car_id,
            'Mark': car_obj.mark,
            'Model': car_obj.model,
            'Color': car_obj.color,
            'Price': car_obj.price,
            'Date': car_obj.date,
        }

        if seller_key in sold_cars:
            sold_cars[seller_key].append(sold_car)
        else:
            sold_cars[seller_key] = [sold_car]

        self.dat.write_data(sold_cars, self.sold_cars_fname)

    def get_available_cars(self):
        seller_car_park = self.dat.read_data(self.seller_car_park_file)
        if self.seller_id in seller_car_park:
            seller = seller_car_park[self.seller_id]
            return seller['cars']
        else:
            return []
