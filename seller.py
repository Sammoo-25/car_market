import datetime

from person import Person


class Seller(Person):
    def __init__(self, name, surname, city, data_obj, car_market, seller_info_file, seller_bank_file, sold_cars_fname):
        if type(name) is str and type(surname) is str and type(city) is str:
            super().__init__(name, surname, city)
        self.dat = data_obj
        self.car_market = car_market
        # self.sold_cars_fname = sold_cars_fname
        # self.sold_cars = data_obj.read_data(self.sold_cars_fname)
        self.seller_info_file = seller_info_file
        self.seller_info = data_obj.read_data(self.seller_info_file)

        self.sold_cars_fname = sold_cars_fname
        self.sold_cars = data_obj.read_data(self.sold_cars_fname)

        self.seller_bank_file = seller_bank_file
        self.seller_bank = data_obj.read_data(self.seller_bank_file)
        self.money = 0

    def add_info(self, car_info_file):
        car_data = self.dat.read_data(car_info_file)
        self.seller_info = car_data
        self.dat.write_data(self.seller_info, self.seller_info_file)
        # old_data = self.dat.read_data(seller_filename)
        # data = {"name": self.name,
        #         "surname": self.surname,
        #         "city": self.city}
        # k = random.randint(1, 8)
        # old_data[str(k)] = data
        # self.seller_info = old_data
        #
        # self.dat.write_data(self.seller_info, self.seller_info_file)

    def get_available_cars(self):
        data = self.seller_info
        return data

    def __check_discount(self, car_code):
        if self.seller_info[car_code]['Discount']:
            return self.seller_info[car_code]['Price'] - (self.seller_info[car_code]['Price'] *
                                                          self.seller_info[car_code]['Discount'] // 100)
        else:
            return self.seller_info[car_code]['Price']

    def sell(self, car_obj, buyer):
        data = self.dat.read_data(self.sold_cars_fname)
        selles_cars = {}
        # l = []
        day_time = str(datetime.date.today())
        for id, car in self.seller_info.items():
            if car_obj.mark == car['Mark']:
                price = self.__check_discount(id)
                selles_cars[id] = car
                selles_cars[id]['Price'] = price
                selles_cars[id]['data'] = day_time
                selles_cars[id]['buyer'] = {'name': buyer.name, 'surname': buyer.surname, 'city': buyer.city}
                # selles_cars[id]['Seller'] = {'name': self.name, 'surname': self.surname, 'city': self.city}
                self.__change_money(car_obj)
                data.update(selles_cars)
                self.sold_cars = data
                # l.append(selles_cars)
                self.dat.write_data(self.sold_cars, self.sold_cars_fname)
                # self.car_market.remove_car(id)

        # sells_cars = {}
        # day_time = str(datetime.date.today())
        # for id, car in self.seller_info.items():
        #     if car_obj.mark == car['Mark']:
        #         price = self.__check_discount(id)
        #         sells_cars[id] = car
        #         sells_cars[id]['Price'] = price
        #         sells_cars[id]['data'] = day_time
        #         self.__change_money(car_obj)
        #         sells_cars[id]['buyer'] = {'name': buyer.name, 'surname': buyer.surname, 'city': buyer.city}
        #         sells_cars[id]['Seller'] = {'name': self.name, 'surname': self.surname, 'city': self.city}
        #         del self.seller_info[id]
        #         self.sold_cars = sells_cars
        #         self.dat.write_data(self.sold_cars, self.seller_info_file)

    def __change_money(self, car_obj):
        self.money = self.money + (car_obj.price * 0.05)
        self.seller_bank['Balance'] = self.money
        # balance = self.seller_bank
        # balance['Balance'] = self.money
        self.dat.write_data(self.seller_bank, self.seller_bank_file)


    def return_car(self):
        pass

#
# if __name__ == '__main__':
#     dt = Database()
#     file = 'seller.json'
#     seller = Seller("Karlen", "Martirosyan", "yerevan", dt, file)
#     seller.add_info(file)
#     seller2 = Seller("Vazgen", "Aslanyan", "London", dt, file)
#     seller2.add_info(file)
