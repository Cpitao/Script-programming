from car import Car
from client import Client


# Na zajęciach ustalono, że auto może być wypożyczone tylko raz

class Dealer:

    def __init__(self):
        self.magazine = {}
        self.clients = {}
        self.counters = {}
        self.max_id = -1

    def rent(self, car_id, client_id):
        if car_id in self.magazine:
            try:
                self.magazine[car_id].update_rent_date()
                self.magazine[car_id].client_id = client_id
            except RuntimeError:
                print("Car cannot be rented")
        else:
            print("No such car")

    def rtrn(self, car_id):
        if car_id in self.magazine:
            try:
                self.magazine[car_id].update_return_date()
            except RuntimeError:
                print("Car cannot be returned")
        else:
            print("No such car")

    def sell(self, client_id, car_id):
        if car_id in self.magazine:
            if self.magazine[car_id].sold():
                self.clients[client_id].bought.append(self.magazine.pop(car_id))
            else:
                print("Can't sell car")
        else:
            print("No such car")

    def list_cars(self):
        for c in self.magazine.values():
            print(c)
            print('------------------------------------------------')

    def list_clients(self):
        for k, c in self.clients.items():
            print(f"{k}) {c}")

    def parse_file_line(self, line: str):
        try:
            make, sell_price, rent_price = line.split(sep=',')
        except ValueError:
            print(f"Invalid input line:\n{line}")
        self.counters[make] = self.counters.get(make, -1) + 1
        self.max_id += 1
        self.magazine[self.max_id] = Car(self.counters[make], make, float(sell_price), float(rent_price),
                                         self.max_id)

    def parse_input_line(self, line):
        operation = line.split(sep=',')[0]
        if operation == 'list_cars':
            self.list_cars()
        elif operation == 'list_clients':
            self.list_clients()
        elif operation == 'rent':
            try:
                operation, client_id, car_id = line.split(sep=',')
                client_id = int(client_id)
                car_id = int(car_id)
            except ValueError:
                print("Invalid input line")
            self.rent(car_id, client_id)
        elif operation == 'return':
            try:
                operation, client_id, car_id = line.split(sep=',')
                client_id = int(client_id)
                car_id = int(car_id)
            except ValueError:
                print("Invalid input line")
            self.rtrn(car_id)
        elif operation == 'buy':
            try:
                operation, client_id, car_id = line.split(sep=',')
                client_id = int(client_id)
                car_id = int(car_id)
            except ValueError:
                print("Invalid input line")
            self.sell(client_id, car_id)
        elif operation == 'add_client':
            try:
                operation, first_name, last_name, address = line.split(sep=',')
            except ValueError:
                print("Invalid input line")
            self.add_client(first_name, last_name, address)
        else:
            print(f"Invalid operation \"{operation}\"")

    def add_client(self, first_name, last_name, address=None):
        if len(self.clients.keys()) > 0:
            last_id = max(self.clients.keys())
        else:
            last_id = -1
        self.clients[last_id + 1] = Client(self, last_id + 1, first_name, last_name, address)

    def __str__(self):
        s = ""
        for k, c in self.clients.items():
            s += str(c) + '\n'
            cost = 0
            for _, car in self.magazine.items():
                if car.client_id == c.client_id:
                    s += f"Rented: {car.rent_date}\n " \
                         f"Returned: {car.return_date if car.return_date is not None else '-'}\n"
                    if car.return_date is not None:
                        cost += max((car.return_date - car.rent_date).days + 1, 1)
            for car in c.bought:
                cost += car.sell_price
                s += f"Bought {car.make} for {car.sell_price}\n"
            s += f"Total price ${cost}"
        return s