class Client:
    def __init__(self, dealer, client_id, first_name, last_name, address=None):
        self.__client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.bought = []
        self.dealer = dealer

    @property
    def client_id(self):
        return self.__client_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}," \
               f"\n{self.address}"

    def __repr__(self):
        return f"Client({self.__client_id},{self.first_name},{self.last_name},{self.address})"

    def __lshift__(self, other):
        self.dealer.rent(other.overall_id, self.__client_id)

    def __rshift__(self, other):
        self.dealer.rtrn(other.overall_id)

    def __add__(self, other):
        self.dealer.sell(self.__client_id, other.overall_id)
