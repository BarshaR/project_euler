'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

number = 0

def dividesIntoRange(max_num, num):
    for i in range(1, max_num + 1):
        if (num % i != 0):
            return False
    return True

counter = 2520
while (number == 0):
    if (not dividesIntoRange(20, counter)):
        counter += 2520
    else:
        number = counter

print(number)