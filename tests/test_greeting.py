import unittest

from greeting import greeting


class GreetingTests(unittest.TestCase):
    def test_greets_a_person(self):
        self.assertEqual(greeting("Ada"), "Hello, Ada!")

    def test_trims_leading_and_trailing_whitespace(self):
        self.assertEqual(greeting("  Ada  "), "Hello, Ada!")

    def test_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            greeting("")

    def test_rejects_whitespace_only_name(self):
        with self.assertRaises(ValueError):
            greeting("   ")


if __name__ == "__main__":
    unittest.main()
