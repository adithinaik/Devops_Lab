
import unittest
from app import greet


class TestGreeting(unittest.TestCase):

    def test_greet_returns_correct_message(self):
        self.assertEqual(
            greet("DevOps"),
            "Hello, DevOps! Welcome to Jenkins CI."
        )

    def test_greet_with_different_name(self):
        self.assertEqual(
            greet("Adithi"),
            "Hello, Adithi! Welcome to Jenkins CI."
        )


if __name__ == "__main__":
    unittest.main()
