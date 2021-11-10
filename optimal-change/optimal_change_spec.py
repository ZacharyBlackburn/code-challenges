import unittest
from optimal_change import optimal_change

class OptimalChangeTestCase(unittest.TestCase):
    
    def test_returns_an_str(self):
        """
        Test should return a str.
        """
        results = optimal_change(10, 20)
        self.assertEqual(type(results), str)
    
    def test_returns_str_if_no_change_given(self):
        """
        Test should return a str indicating that there is no change.
        """
        results = optimal_change(10, 10)
        expected = "There is no change for an item that costs $10 with an amount paid of $10."
        self.assertEqual(results, expected)

    def test_returns_str_if_not_enough(self):
        """
        Test should return a str indicating that there isn't enough money.
        """
        results = optimal_change(10, 5)
        expected = "$5 is not enough to cover $10, you need an extra $5 to purchase this item."
        self.assertEqual(results, expected)

    def test_returns_str_with_no_cost(self):
        """
        Test should return a str showing no change.
        """
        results = optimal_change(0, 0)
        expected = "There is no change for an item that costs $0 with an amount paid of $0."
        self.assertEqual(results, expected)
    
    def test_returns_str_with_coin_amount_1(self):
        """
        Test should return a str showing how much change is left.
        """
        results = optimal_change(62.13, 100)
        expected = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        self.assertEqual(results, expected)

    def test_returns_str_with_coin_amount_2(self):
        """
        Test should return a str showing how much change is left.
        """
        results = optimal_change(10.27, 1000)
        expected = "The optimal change for an item that costs $10.27 with an amount paid of $1000 is 9 $100 bills, 1 $50 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 4 $1 bills, 2 quarters, 2 dimes, and 3 pennies."
        self.assertEqual(results, expected)

    def test_returns_str_with_coin_amount_3(self):
        """
        Test should return a str showing how much change is left.
        """
        results = optimal_change(10.00, 100.00)
        expected = "The optimal change for an item that costs $10.0 with an amount paid of $100.0 is 1 $50 bill, and 2 $20 bills."
        self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()