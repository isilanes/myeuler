def n(i, max=1000):
    return int((max-1)/i)

def m(i, max=1000):
    return int(i*n(i,max)*(n(i,max) + 1)/2)

max = 1000
t = m(3,max) + m(5,max) - m(15,max)
print(t)
