'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(number):
    num_str = str(number)
    # Compare each character in the string starting from the outside and moving in
    # e.g "11211" will compare str[0] == str [-1] then str[1] == str[-2] etc
    for i in range(0, int(len(num_str) / 2)):
        if (num_str[i] != num_str[- (i + 1)]):
            return False

    return True

largestPalindrome = 0

# Check each number between the highest and lowest possible 3 digit numbers
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        if(isPalindrome(product) and product > largestPalindrome):
            largestPalindrome = (product)

print(largestPalindrome)