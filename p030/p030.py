def f1():
    nums = []
    for i in range(2,354294): # 354294 is 6*9**5
        d = [ int(x)**5 for x in str(i) ]
        if sum(d) == i:
            nums.append(i)

    return sum(nums)

#-------------------------------------------------------------------------#

res = f1()

print(res)
