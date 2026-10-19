import unittest

from greeting import greeting


class GreetingTests(unittest.TestCase):
    def test_greets_a_person(self):
        self.assertEqual(greeting("Ada"), "Hello, Ada!")


if __name__ == "__main__":
    unittest.main()
