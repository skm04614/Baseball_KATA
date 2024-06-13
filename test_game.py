from unittest import TestCase

from game import baseball_game


class Test(TestCase):
    def test_invalid_argument(self):
        invalid_args = ("a", "ab", "abc", "abcd", "1a", "a1", "1", "12", "1234")
        valid_arg = "456"

        for invalid_arg in invalid_args:
            with self.assertRaises(ValueError):
                baseball_game(valid_arg, invalid_arg)
            with self.assertRaises(ValueError):
                baseball_game(invalid_arg, valid_arg)

    def test_x_ball_y_strike(self):
        expected_to_arguments = {
            (False, 0, 0): (("456", "123"), ("246", "357"), ("987", "654"), ("109", "584"), ("382", "971")),
            (False, 1, 0): (("456", "125"), ("246", "327"), ("487", "654"), ("105", "584"), ("114", "331")),
            (False, 2, 0): (("456", "625"), ("276", "327"), ("467", "654"), ("145", "584"), ("113", "331")),
            (False, 3, 0): (("456", "645"), ("273", "327"), ("465", "654"), ("845", "584"), ("123", "312")),
            (False, 0, 1): (("123", "453"), ("383", "327"), ("689", "654"), ("899", "813"), ("193", "999")),
            (False, 1, 1): (("523", "453"), ("373", "327"), ("649", "654"), ("839", "813"), ("798", "988")),
            (False, 2, 1): (("543", "453"), ("372", "327"), ("645", "654"), ("831", "813"), ("667", "766")),
            (False, 0, 2): (("153", "453"), ("337", "327"), ("655", "654"), ("888", "818"), ("012", "212")),
            (True, 0, 3): (("123", "123"), ("456", "456"), ("789", "789"), ("441", "441"), ("555", "555"))
        }

        for expected, arguments in expected_to_arguments.items():
            for args in arguments:
                self.assertEqual(expected, baseball_game(*args))
                self.assertEqual(expected, baseball_game(*args[::-1]))
