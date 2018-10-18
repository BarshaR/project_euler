'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import time

num = 600851475143
last_prime_factor = 0
highest_prime = 0

def isPrime(number):
    if (number == 1):
        return False
    for i in range(2, number - 1):
        if (not number % i):
            return False
    return True

start = time.time()

# Loop through all odd numbers below the square root
for j in range(3, int(num ** 0.5) + 1, 2):
    # Check if j is a factor
    if num % j == 0:
        last_num = num / j
        # The highest factor will be the complement of the lowest factor
        # Therefore, check the highest factor
        if isPrime(int(last_num)) and last_num > highest_prime:
            highest_prime = last_num
        elif isPrime(int(j)) and j > highest_prime:
            # Traverse through factors lower than the square root if prime factors 
            # greater than sqrt don't exist
            highest_prime = j

print(highest_prime)
print((time.time() - start) * 1000)

