num0 = 600851475143
factors = []

num = num0
max = num
cum = 1

last = 2
while num > last:
    for i in range(last,max):
        print(i)
        while not num % i:
            factors.append(i)
            num = num/i
            cum = cum*i
            last = i
            print(i, num, cum)
        
        if cum == num0:
            break

print(factors)
