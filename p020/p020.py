'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

#-------------------------------------------------------------------------#

def f1(num):
    prod = 1
    for i in range(2,num+1):
        prod = prod * i

    sum = 0
    for digit in str(prod):
        sum += int(digit)
        
    return sum

#-------------------------------------------------------------------------#

res = f1(99)

print(res)
