import unittest
from app.dealer import Dealer


class Test_dealer(unittest.TestCase):

    def test_parse_file_line(self):
        dealer = Dealer()
        dealer.parseFileLine("Audi,100,100000")
        self.assertDictEqual(dealer.magazine,
                             {0: {
                                "make": "Audi",
                                "rent": 100,
                                "sell": 100000,
                                "history": []
                             }})
    
    def test_rent_car(self):
        dealer = Dealer()
        dealer.parseFileLine("Audi,100,100000")
        dealer.rent(0, 0, "Kolega kolegi")
        self.assertDictEqual(dealer.magazine, {})
        self.assertIn("Kolega kolegi", dealer.clients)
    
    def test_sell_car(self):
        dealer = Dealer()
        dealer.parseFileLine("Audi,100,10000")
        dealer.sell(0, "Kolega kolegi")
        self.assertDictEqual(dealer.magazine, {})
        self.assertIn(0, dealer.sold)
    
    def test_parse_user_input(self):
        dealer = Dealer()
        dealer.parseFileLine("Audi,100,10000")
        dealer.parseInputLine("rent,Kolega kolegi,0,0")
        self.assertIn("Kolega kolegi", dealer.rented)
        self.assertNotIn(0, dealer.magazine)
