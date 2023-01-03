from datetime import datetime, timedelta
from random import randint


class Car:
    def __init__(self, car_id: int, make: str, sell_price: float,
                 rent_price: float, overall_id: int):
        self.car_id = car_id
        self.client_id = None
        self.make = make
        self.sell_price = sell_price
        self.rent_price = rent_price
        self.__rent_date = None
        self.__return_date = None
        self.__sold = False
        self.overall_id = overall_id

    @property
    def rent_date(self):
        return self.__rent_date

    def update_rent_date(self):
        if self.__rent_date is not None:
            raise RuntimeError("Car cannot be rented (can only be done once)")
        self.__rent_date = datetime.today() + timedelta(days=randint(1, 10))

    @property
    def return_date(self):
        return self.__return_date

    def update_return_date(self):
        if self.__rent_date is None or self.__return_date is not None:
            raise RuntimeError("Can't return car which is not rented")
        self.__return_date = self.__rent_date + timedelta(days=randint(1, 100))

    def sold(self):
        if self.__return_date is not None or self.__rent_date is None:
            self.__sold = True
            return True
        return False

    def __repr__(self):
        return f"Car(car_id={self.car_id}," \
               f" make={self.make}," \
               f" sell_price={self.sell_price}," \
               f" rent_price={self.rent_price})"

    def __str__(self):
        return f"{self.make} | sell price: {self.sell_price}$ | rent price: {self.rent_price}$\n" \
               f"rented: {self.__rent_date if self.__rent_date is not None else '-'} | " \
               f"returned: {self.__return_date if self.__return_date is not None else '-'}\n" \
               f"sold: {'yes' if self.__sold else 'no'}"