import unittest
from app.dealer import Dealer


class TestFull(unittest.TestCase):

    # def __init__(self):
    #     self.setup()

    def test_integrate(self):
        self.dealer = Dealer()
        filename = "app/cars.txt"
        with open(filename, "r") as f:
            lines = f.readlines()
            for l in lines:
                self.dealer.parseFileLine(l)
    
        #test_rent_car
        self.dealer.rent(0, 1, "Kolega kolegi")
        self.assertNotIn(0, self.dealer.magazine)
        self.assertIn("Kolega kolegi", self.dealer.rented)
        
        # test_return_car
        self.dealer.rtrn(0, 5, "Kolega kolegi")
        self.assertNotIn("Kolega kolegi", self.dealer.rented)
        self.assertIn(0, self.dealer.magazine)
    
        # test_buy_car
        self.dealer.sell(0, "Kolega kolegi")
        self.assertIn(0, self.dealer.sold)
    
        # test_buy_unavailable_car
        with self.assertRaises(ValueError):
            self.dealer.sell(0, "Kolega kolegi")
    
        # test_rent_unavailable_car
        with self.assertRaises(ValueError):
            self.dealer.rent(0, 5, "Kolega kolegi")

        # test_return_not_rented
        with self.assertRaises(ValueError):
            self.dealer.rtrn(0, 100, "Kolega kolegi")


if __name__ == "__main__":
    unittest.main()