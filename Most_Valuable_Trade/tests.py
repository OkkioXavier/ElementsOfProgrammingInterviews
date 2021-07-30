import unittest

from Most_Valuable_Trade.main import search_for_best_sale_price, linear_search


class TestCases(unittest.TestCase):
    def test_ascending_first_minus_last_returned(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result1 = search_for_best_sale_price(array)
        result2 = linear_search(array)
        self.assertEqual(8, result1.best_sale_price)
        self.assertEqual(8, result2)

    def test_random_highest_diff_returned(self):
        array = [100, 80, 50, 60, 800, 500, 4, 3, 1]
        result1 = search_for_best_sale_price(array)
        result2 = linear_search(array)
        self.assertEqual(750, result1.best_sale_price)
        self.assertEqual(750, result2)

    def test_descending_lowest_loss_returned(self):
        array = [100, 80, 50, 30, 25, 10, 5, 0]
        result1 = search_for_best_sale_price(array)
        result2 = linear_search(array)

        # Which of these assertions is correct? Probably -5?
        self.assertEqual(-5, result1.best_sale_price)
        self.assertEqual(0, result2)


if __name__ == '__main__':
    unittest.main()
