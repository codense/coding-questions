# Question: Find the maximum decimal number without zeroes and with no equal digits in a row, such that the sum of its digits is 𝑛.

# Input: Each test contains multiple test cases. The first line contains a single integer 𝑡.
# The only line of each test case contains an integer 𝑛 - the required sum of the digits.

# Output: For each test case print the maximum number you can obtain.

t = int(input())
for _ in range(t):
    
    n = int(input())
    
    i = 1
    if n%3 == 0 or n%3 == 2:
        i = 2
        
    while n > 0:
        print(i, end="")
        n=n-i
        i = 3 - i
        
    print()
