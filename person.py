class Person:
    def __init__(self, name, surname, city):
        if type(name) is str and type(surname) is str and type(city) is str:
            self._name = name
            self._surname = surname
            self._city = city
        else:
            raise ValueError

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def city(self):
        return self._city

    def show(self):
        return f"name: {self._name}\nsurname: {self._surname}\ncity: {self._city}"


# if __name__ == '__main__':
#     p = Person("Arsen", "Manukyan", "Yerevan")
#     print(p.show())
