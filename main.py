import math


def is_prime(num):
    """
    Given a number, determine if it is a prime number
    :param num: integer
    :return: boolean
    """
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0:
        return False

    limit = math.floor(math.sqrt(num))
    for divisor in range(3, 1 + limit, 2):
        if num % divisor == 0:
            return False
        divisor += 1
    return True


def get_first_n_primes(num):
    """
    Given a limit, get that many prime numbers starting from 2
    :param num: number of primes to return
    :return: list of primes for given limit
    """
    if not isinstance(num, int):
        return []
    primes = []
    number = 2
    while len(primes) < num:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes


def multiplication_table(numbers):
    """
    Given a list of primes, print multiplication table
    :param numbers: list of prime numbers
    :return: multiplication table as a formatted string to be printed
    """
    if not len(numbers):
        return ""
    table = "-\t"
    for num in numbers:
        table += f"{num}\t"
    table += "\n"
    for idx1, num1 in enumerate(numbers):
        table += f"{num1}\t"
        for idx2, num2 in enumerate(numbers):
            table += f"{num1*num2}\t"
        table += "\n"
    return table


