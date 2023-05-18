from person import Person


class Seller(Person):
    def __init__(self, name, surname, city, data_obj, seller_info_file):
        super().__init__(name, surname, city)
        self.dat = data_obj
        # self.sold_cars_fname = sold_cars_fname
        # sold_cars_fname
        # self.sold_cars = data_obj.data_obj.read_data(self.sold_cars_fname)
        self.seller_info_file = seller_info_file
        self.seller_info = data_obj.read_data(self.seller_info_file)
        self.money = 0

    def add_info(self, seller_filename):
        old_data = self.dat.read_data(seller_filename)
        data = [{"name": self.name,
                 "surname": self.surname,
                 "city": self.city}
                ]

            # {"name": "Gisella", "surname": "Casewell", "city": "Anguil"},
            # {"name": "Lolly", "surname": "Androli", "city": "Hepingjie"}

        for i, entry in enumerate(data, start=1):
            old_data[str(i)] = entry
        self.dat.write_data(old_data, self.seller_info_file)

    def _get_available_cars(self):
        pass

    def __check_discount(self):
        pass

    def sell(self):
        pass

    def __change_money(self):
        pass

    def add_sold_car(self):
        pass

    def return_car(self):
        pass
