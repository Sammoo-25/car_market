import json


class Database:

    def read_data(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def write_data(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
