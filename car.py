class Car:
    def __init__(self, mark, model, color, price):
        self.__mark = mark
        self.__model = model
        self.__color = color
        self.__price = price

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



if __name__ == '__main__':
    c = Car("BMW", "E60", "Black", 780000)
