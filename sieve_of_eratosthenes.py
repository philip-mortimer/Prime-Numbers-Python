"""
    Copyright 2020 Philip Mortimer
    
    This file is part of Philip Mortimer Example Programs.
    
    Philip Mortimer Example Programs is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public License as 
    published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.
    
    Philip Mortimer Example Programs is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Philip Mortimer Example Programs.  If not, see 
    <https://www.gnu.org/licenses/>.
"""


# Largest prime number in sequence will be largest prime <= N.
N = 100

# Specifies how many numbers are to be printed on each line 
# when printing the prime numbers.
NUMBERS_PER_LINE = 20


import numpy
import math

def sieve_of_eratosthenes(n):
    """
    n:   determines size of largest prime in the sequence - see comments
         below
       
    Iterator which generates a sequence of prime numbers using the sieve 
    of Eratosthenes algorithm. It is based on 
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes.
        
    It generates a sequence of all primes in range 2..max_prime inclusive
    where max_prime is largest prime <= n.
    """  
    assert (n >= 2),"n must be >= 2"
    
    # Create an array indexed from 2..n with a11 elements initialised to True.
    # The algorithm will set is_prime[num] to False if num is not prime.
    is_prime = numpy.full(n+1, True)
    
    max_i = math.floor(math.sqrt(n))
    i = 2
    while i <= max_i:
        if is_prime[i]: 
            for j in range(i*i, n+1, i):
                is_prime[j] = False
        i += 1
    
    # Output the primes.
    for i in range(2, n+1):
        if is_prime[i]:
            yield(i)


def test_sieve_of_eratosthenes(n, numbers_per_line):
    print("Prime numbers between 2 and {} are as follows:".format(n))
    count = 1   
    for i in sieve_of_eratosthenes(n):
        print(i, end=' ') 
        if count % numbers_per_line == 0:
            print()
        count += 1
    

if __name__ == '__main__':
    test_sieve_of_eratosthenes(N, NUMBERS_PER_LINE)
