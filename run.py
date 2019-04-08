import math
import sys
import main


def run(number_of_primes):
    prime_nums = main.get_first_n_primes(number_of_primes)
    multiplication_table = main.multiplication_table(prime_nums)
    print(multiplication_table)


if (__name__ == '__main__'):
    number_of_primes = int(sys.argv[1])
    run(number_of_primes)
