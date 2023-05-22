import datetime

from person import Person


class Buyer(Person):
    def __init__(self, name, surname, city, data_obj, buyed_cars_fname, buyer_bank_file, sell_sold_cars_file):
        super().__init__(name, surname, city)
        self.data = data_obj
        self.buyed_cars_fname = buyed_cars_fname
        self.bought_cars = data_obj.read_data(self.buyed_cars_fname)

        self.buyer_bank_file = buyer_bank_file
        self.money = data_obj.read_data(self.buyer_bank_file)
        self.__spent_money = 0

        self.sell_sold_cars_file = sell_sold_cars_file
        self.sold_cars = self.data.read_data(self.sell_sold_cars_file)

    def buy(self, car_obj, seller):
        sell_data = self.data.read_data(self.sell_sold_cars_file)
        data = self.data.read_data(self.buyed_cars_fname)
        bought_cars = {}
        day_time = str(datetime.date.today())
        if self.sold_cars:
            data = sell_data
            self.bought_cars = data
            self.__change_money(car_obj)
            self.data.write_data(self.bought_cars, self.buyed_cars_fname)
        else:
            for id, car in seller.seller_info.items():
                if car_obj.mark == car['Mark']:
                    bought_cars[id] = car
                    bought_cars[id]["Buyer"] = {'name': self.name, 'surname': self.surname, 'city': self.city}
                    bought_cars[id]['data'] = day_time
                    bought_cars[id]['spent money'] = car_obj.price
                    self.__change_money(car_obj)
                    data.update(bought_cars)
                    self.bought_cars = data
                    self.data.write_data(self.bought_cars, self.buyed_cars_fname)

    def __change_money(self, car_obj):
        self.__spent_money = car_obj.price
        self.money['Balance'] -= self.__spent_money
        self.data.write_data(self.money, self.buyer_bank_file)

    # def __check_discount(self, car_code):
    #     if self.seller_info[car_code]['Discount']:
    #         return self.seller_info[car_code]['Price'] - (self.seller_info[car_code]['Price'] *
    #                                                       self.seller_info[car_code]['Discount'] // 100)
    #     else:
    #         return self.seller_info[car_code]['Price']


    def print_my_cars(self):
        data = self.bought_cars
        print(data)

    def return_car(self):
        pass

# if __name__ == '__main__':
#     dt = Database()
#     fname = "buyed_cars.json"
#     by1 = Buyer("Karlen", "Manukyan", "Yerevan", dt, fname)
