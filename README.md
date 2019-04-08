# fundingcircle
Funding Circle Coding Challenge: Write a program that prints out a multiplication table of the first 10 prime numbers

**Installation Instructions**

This problem was solved using Python and assumes you have the latest Python version (3.x) installed on the machine.

In case Python is not available on your machine, use the following steps to install Python based on your OS:

1. Go to [Python.org](https://www.python.org/downloads/)  downloads page here and download the latest Python installer package
2. Run the Python installer package and install Python 3 onto your machine
3. Check if python 3 was successfully installed using the following command:   
    ```
    python3 --version
    ```

**Run Book**

1. This program takes input N (number of primes) as this allow it to run for 10 or any N. To print the multiplication table for first 10 prime numbers on command line, go to the path that the git project was downloaded and type the following command:
    ```
    python3 run.py 10
    ```
2. To run the tests, type the following on command line at the same path where the git project was downloaded:
    ```
    python3 test.py
    ```

**Time Complexity**
 
 **is_prime(num):** 
 Time to determine if a number m is prime. Upper time bound: O(sqrt(m)) 
 Optimizations : 
 1. Iterate only until the square root of the number, as all possible factors of a number lie in that limit.
 2. Skip even numbers except 2
 
 **get_first_n_primes** 
 Time to find first N primes: N * sqrt(m)
 
 **multiplication_table**
 Time to print the multiplication table: N * N => O(n^2)
 
 Since the multiplication table has to be printed out in its entirety, the overall time complexity cannot be better than O(n^2)
