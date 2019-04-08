import unittest
import main


class TestPrimeTable(unittest.TestCase):

    def test_is_prime(self):
        # expected True
        self.assertTrue(main.is_prime(2))
        self.assertTrue(main.is_prime(29))

        # expected False
        self.assertFalse(main.is_prime(1))
        self.assertFalse(main.is_prime(4))
        self.assertFalse(main.is_prime(-11))

    def test_get_first_n_primes(self):
        self.assertEqual(main.get_first_n_primes(0), [])
        self.assertEqual(main.get_first_n_primes(5), [2, 3, 5, 7, 11])

        # no primes returned for floats
        self.assertEqual(main.get_first_n_primes(5.7), [])

        # no primes returned for strings
        self.assertEqual(main.get_first_n_primes("a"), [])

    def test_multiplication_table(self):
        self.assertEqual(main.multiplication_table([2,3,5]), "-\t2\t3\t5\t\n2\t4\t6\t10\t\n3\t6\t9\t15\t\n5\t10\t15\t25\t\n")
        self.assertEqual(main.multiplication_table([]), "")


if __name__ == '__main__':
    unittest.main()
