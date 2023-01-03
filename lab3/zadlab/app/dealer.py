class Dealer:

    def __init__(self):
        self.__ids = 0 # increment every time a car is added to magazine and assign 
        self.magazine = {}
        self.rented = {}
        self.sold = {}
        self.clients = {}
        # magazine is a dictionary of cars with id being the key
        # Car will be represented as a dictionary with the following elements:
        # - id
        # - make
        # - sell price
        # - rent price
        # - history (when rented/returned/sold)

    def rent(self, id, day, person):
        if id in self.magazine:
            self.magazine[id]["history"].append(f"Rented on day {day} by {person}")
            self.clients[person] = self.clients.get(person, []) + [(0, "rent", id, day)]
            if person in self.rented:
                self.rented[person][id] = self.magazine.pop(id)
            else:
                self.rented[person] = {id: self.magazine.pop(id)}
        else:
            raise ValueError("No such car to rent")
            
    def rtrn(self, id, day, person):
        if person not in self.rented:
            raise ValueError("This person rents no car")
        elif id not in self.rented[person]:
            raise ValueError("This person doesn't rent such car")
        else:
            day_rented = sorted(list(filter(lambda x: x[2] == id, self.clients[person])),
                                key=lambda x: x[3], reverse=True)[0][3]
            self.clients[person] = self.clients.get(person, []) + \
                [((day - day_rented) * self.rented[person][id]["rent"], "return", id, day)]
            self.rented[person][id]["history"].append(f"Returned on day {day} by {person}")
            self.magazine[id] = self.rented[person].pop(id)
            
            if len(self.rented[person].keys()) == 0:
                self.rented.pop(person)

    def sell(self, id, person):
        if id in self.magazine:
            self.sold[id] = self.magazine.pop(id)
            self.clients[person] = self.clients.get(person, []) + \
                [(self.sold[id]["sell"], "sell", id, "-")]
        else:
            raise ValueError("No such car in the magazine")

    def list_cars(self):
        """Lists available cars"""
        for id, c in self.magazine.items():
            print(f"{id}: {c['make']}")

    def parseFileLine(self, line):
        data = line.split(sep=',')
        if len(data) < 3:
            raise ValueError("Invalid file format")
        try:
            car = {"make": data[0],
                   "rent": float(data[1]),
                   "sell": float(data[2]),
                   "history": []}
        except ValueError:
            print("Invalid price value")
            exit(0)
        
        self.magazine[self.__ids] = car
        self.__ids += 1

    def parseInputLine(self, line):
        try:
            op = line.split(sep=',')[0]
        except ValueError:
            print("Invalid input data")
        if op.lower() == 'rent':
            try:
                op, person, id, day = line.split(sep=',')
                id = int(id)
                day = int(day)
                self.rent(id, day, person)
            except ValueError:
                print("Invalid operation")
        elif op.lower() == 'return':
            try:
                op, person, id, day = line.split(sep=',')
                id = int(id)
                day = int(day)
                self.rtrn(id, day, person)
            except ValueError:
                print("Invalid input data")
        elif op.lower() == 'buy':
            try:
                op, person, id = line.split(sep=',')
                id = int(id)
                self.sell(id, person)
            except ValueError:
                print("Invalid input data")
        elif op.lower() == 'list':
            self.list_cars()
        else:
            print("Usage: [list|rent|return|buy] [name] [id] [day]")

    def end_print(self):
        for client, actions in self.clients.items():
            print(f"Client {client} made operations for a total of "
                  f"{sum([x[0] for x in actions])}$")
            for a in actions:
                print(f"- {a[0]} for {a[1]} (car {a[2]}) day {a[3]}")

        print("Cars in the magazine after all operations:")
        for id, car in self.magazine.items():
            print(f" {id}) {car['make']}")