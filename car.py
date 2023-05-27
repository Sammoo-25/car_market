import uuid


class Car:
    def __init__(self, mark, model, color, price, date):
        if type(mark) is str and type(model) is str and type(price) is int and type(color) is str and type(date) is int:
            self.__mark = mark
            self.__model = model
            self.__color = color
            self.__price = price
            self.__date = date

        else:
            raise ValueError
        self.__discount = 0
        self.__seller = None
        self.car_id = str(uuid.uuid4())

    @property
    def mark(self):
        return self.__mark

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @property
    def price(self):
        return self.__price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, new_dis):
        self.__discount = new_dis

    @property
    def date(self):
        return self.__date

    @property
    def seller(self):
        return self.__seller
