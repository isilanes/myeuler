max = 4000000

last1 = 1
last2 = 2
sum = 2
while True:
    new = last1 + last2

    if new > max:
        break

    if not new % 2: # even
        sum += new
    last1 = last2
    last2 = new

print(sum)
