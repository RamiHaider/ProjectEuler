# Question is simple: Find the sum of all a values from 1 to 10^7, such that, for i in range of mod n value, find the largest a value s.t. a^2 = a for mod n. For example, we look at n = 3. the only possiblilities are 1 & 2, since a < n. anyways, 1^2 = 1 = 1, so for mod 3, and actually it looks like the default will always be 0. anyways, 2^2 = 4, but in mod 3 it is equal to 1, so a^2 != a in mod 3. Now, we take 1, and we do that check for each number, and then find the sum of them. 

# For each number in range (1-10) find the largest of of that number -1, such that, that number squared 

#Begin at 5, Look at the range from 1 - 5, compute for each value, if i^2 % 5 = i % 5, then save that number, and just do a counter, we can set a flag to 0, and update it if it is the largets number, then do for the next number
# import math

# limit = 100
# total = 0


# for x in range(1,limit + 1):
#     for i in range(x-1,0,-1):
#         if (i * i - i) % x == 0:
#             total += i
#             print(f'at the value {x} the largest value is {i} and the new sum is {total}')
#             break
# print(total + 1)



# Python Program to find prime numbers in a range
#import time
# list_Primes = []
# def SieveOfEratosthenes(n):
      
#     # Create a boolean array "prime[0..n]" and 
#     # initialize all entries it as true. A value 
#     # in prime[i] will finally be false if i is
#     # Not a prime, else true.
#     prime = [True for i in range(n+1)]
     
#     p = 2
#     while(p * p <= n):
          
#         # If prime[p] is not changed, then it is 
#        # a prime
#         if (prime[p] == True):
              
#             # Update all multiples of p
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1
#     c = 0
 
#     # Print all prime numbers
#     for p in range(2, n):
#         #print(p)
#         if prime[p]:
#             list_Primes.append(p)
#             #print(p)
#             #print(len(list_Primes))
#             c += 1
#     return c
 

# c = SieveOfEratosthenes(10000000)
# print("Total prime numbers in range:", c)
# print(list_Primes[-1])





###Next Step, Find If the given list of numbers from 1 - 1000 are factorizable by a prime number powered, i.e., 

# import math

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def get_primes_between(a, b):
#     primes = []
#     for num in range(a, b + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# def check_divisibility_by_primes_between_sqrt_and_num(number):
#     sqrt_value = int(math.sqrt(number))
#     primes = get_primes_between(sqrt_value, number)
#     divisible_primes = [prime for prime in primes if number % prime == 0]
#     return divisible_primes

# def check_all_numbers(limit):
#     results = {}
#     for number in range(1, limit + 1):
#         divisible_primes = check_divisibility_by_primes_between_sqrt_and_num(number)
#         results[number] = divisible_primes
#     return results

# # Check for numbers between 1 and 200
# limit = 200
# results = check_all_numbers(limit)

# # Print the results
# for number, divisible_primes in results.items():
#     if divisible_primes:
#         print(f'The number {number} is divisible by the prime numbers between its square root and itself: {divisible_primes}')
#     else:
#         print(f'The number {number} is not divisible by any prime numbers between its square root and itself.')
# 
# Solution to Project Euler problem 407
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import eulerlib


# If a^2 = a mod n, then this is also true for any m that divides n.
# Let's focus on the moduli that are prime powers, p^k.
# 
# Claim: The only solutions of a^2 = a mod p^k are a = 0, 1 mod p^k.
# Proof:
#   First note that a = 0 mod p^k is always a solution. Now consider the case of 0 < a < p^k.
#   Let a = b * p^j, where 0 < b < p^j and b is coprime with p (thus j is as large as possible).
#   Then (b p^j)^2 = b p^j mod p^k, expanding to b^2 p^2j = b p^j mod p^k.
#   Divide all of the equation (including the modulus) by p^j, giving b^2 p^j = b mod p^(k-j).
#   b is coprime with p (and therefore p^(k-j)), so b^-1 exists.
#   Multiply both sides by b^-2 to get b^-1 = p^j mod p^(k-j).
#   b is coprime with p, so b is not a power of p unless j = 0, i.e. p^j = 1 = b.
#   So when a != 0, a = 1 is the only solution.
# 
# If we factor n as a product of prime powers, i.e. n = p0^k0 * p1^k1 * ... where
# all the p's are distinct (and thus all the k's are as large as possible), then we have
# a system of congruences {a = 0,1 mod p0^k0; a = 0,1 mod p1^k1; ...}.
# Using the Chinese remainder theorem, we can solve these congruences to obtain the
# 2^N distinct solutions (where N is the number of distinct prime factors of n).
# The largest solution among these is what we want for the M() function.
def compute():
	LIMIT = 10**7
	
	smallestprimefactor = eulerlib.list_smallest_prime_factors(LIMIT)
	
	ans = 0
	for i in range(1, LIMIT + 1):
		# Compute factorization as coprime prime powers. e.g. 360 = {2^3, 3^2, 5^1}
		factorization = []
		j = i
		while j != 1:
			p = smallestprimefactor[j]
			q = 1
			while True:
				j //= p
				q *= p
				if j % p != 0:
					break
			factorization.append(q)
		
		solns = [0]
		modulus = 1
		for q in factorization:
			# Use Chinese remainder theorem; cache parts of it
			recip = pow(q, -1, modulus)
			newmod = q * modulus
			solns = [((0 + (x    ) * recip * q) % newmod) for x in solns] + \
			        [((1 + (x - 1) * recip * q) % newmod) for x in solns]
			modulus = newmod
		
		ans += max(solns)
	return str(ans)


if __name__ == "__main__":
	print(compute())