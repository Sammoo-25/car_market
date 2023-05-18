from database import Database
from person import Person


class Buyer(Person):
    def __init__(self, name, surname, city, money, data_obj, buyed_cars_fname):
        super().__init__(name, surname, city)
        self.buyed_cars_fname = buyed_cars_fname
        self.bought_cars = data_obj.read_data(self.buyed_cars_fname)
        self.__spent_money = 0
        self.money = money

    def buy(self):
        pass

    def __change_money(self):
        pass

    def add_bought_cars(self):
        pass

    def print_my_cars(self):
        pass

    def return_car(self):
        pass


if __name__ == '__main__':
    dt = Database()
    fname = "buyed_cars.json"
    by1 = Buyer("Karlen", "Manukyan", "Yerevan", dt, fname)
