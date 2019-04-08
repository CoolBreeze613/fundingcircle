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
    
    Output should look like:
    ```
    $ python3 run.py 10
    -	2	3	5	7	11	13	17	19	23	29	

    2	4	6	10	14	22	26	34	38	46	58	

    3	6	9	15	21	33	39	51	57	69	87	

    5	10	15	25	35	55	65	85	95	115	145	

    7	14	21	35	49	77	91	119	133	161	203	

    11	22	33	55	77	121	143	187	209	253	319	

    13	26	39	65	91	143	169	221	247	299	377	

    17	34	51	85	119	187	221	289	323	391	493	

    19	38	57	95	133	209	247	323	361	437	551	

    23	46	69	115	161	253	299	391	437	529	667	

    29	58	87	145	203	319	377	493	551	667	841
    ```   

2. To run the tests, type the following on command line at the same path where the git project was downloaded:
    ```
    python3 test.py
    ```

**Time Complexity**
 
 **is_prime:** 
 Time to determine if a number m is prime. Upper time bound: O(sqrt(m)) 
 
 Optimizations : 
 1. Iterate only until the square root of the number, as all possible factors of a number lie in that limit.
 2. Skip even numbers except for 2
 3. For an odd number, only check odd divisors
 
 **get_first_n_primes:** 
 Time to find first N primes: N * sqrt(m)
 
 **multiplication_table:**
 Time to print the multiplication table: N * N => O(n^2)
 
 Since the multiplication table has to be printed out in its entirety, the overall time complexity cannot be better than O(n^2)
 
 **Tests**
 
 Unit testing and Test Driven Development was used for developing this solution where weakness of the solution were first pointed out with failed tests and then fixed in the main.py in iterations.
