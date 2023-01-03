import unittest

from dealer import Dealer


class Test_Dealer(unittest.TestCase):

    def test_parse_file_line(self):
        dealer = Dealer()
        dealer.parse_file_line('Fiat,10000,200')
        self.assertTrue(dealer.magazine[0].make == 'Fiat')
        self.assertTrue(dealer.magazine[0].sell_price == 10000)
        self.assertTrue(dealer.magazine[0].rent_price == 200)

    def test_add_client(self):
        dealer = Dealer()
        dealer.add_client("Jan", "Kowalski", "ul. 11 listopada")
        self.assertTrue(dealer.clients[0].first_name == 'Jan')
        self.assertTrue(dealer.clients[0].last_name == 'Kowalski')
        self.assertTrue(dealer.clients[0].address == 'ul. 11 listopada')

    def test_parse_input_line_and_operations(self):
        dealer = Dealer()
        dealer.parse_file_line('Fiat,10000,200')
        dealer.add_client("Jan", "Kowalski", "ul. 11 listopada")
        dealer.parse_input_line('rent,0,0')
        self.assertTrue(dealer.magazine[0].rent_date is not None)
        self.assertEqual(dealer.magazine[0].client_id, 0)

        dealer.parse_input_line('return,0,0')
        self.assertTrue(dealer.magazine[0].return_date is not None)

        dealer.parse_input_line('buy,0,0')
        self.assertTrue(len(dealer.clients[0].bought) > 0)


class Test_Client(unittest.TestCase):

    def test_overloads(self):
        dealer = Dealer()
        dealer.add_client("Jan", "Kowalski", "Ul. Jana")
        dealer.parse_file_line('Fiat,10000,200')
        dealer.clients[0] << dealer.magazine[0]
        self.assertTrue(dealer.magazine[0].rent_date is not None)
        dealer.clients[0] >> dealer.magazine[0]
        self.assertTrue(dealer.magazine[0].return_date is not None)
        dealer.clients[0] + dealer.magazine[0]
        self.assertTrue(len(dealer.clients[0].bought) > 0)


if __name__ == "__main__":
    unittest.main()
