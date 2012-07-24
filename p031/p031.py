def f1(amount):
    # values = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
    combos  = 1 # the 2-pounds-equals-2-pounds combo
    combos += 1 # the   2x100p combo
    combos += 1 # the   4x 50p combo
    combos += 1 # the  10x 20p combo
    combos += 1 # the  20x 10p combo
    combos += 1 # the  40x  5p combo
    combos += 1 # the 100x  2p combo
    for i in range(2): # 100p
        for j in range(4): # 50p
            tot = i * 100 + j * 50
            if tot > 199:
                if tot == 200: combos += 1
                break
            for k in range(10): # 20p
                tot = i*100 + j*50 + k*20
                if tot > 199:
                    if tot == 200: combos += 1
                    break
                for l in range(20): # 10p
                    tot = i*100 + j*50 + k*20 + l*10
                    if tot > 199: 
                        if tot == 200: combos += 1
                        break
                    for m in range(40): # 5p
                        tot = i*100 + j*50 + k*20 + l*10 + m*5
                        if tot > 199:
                            if tot == 200: combos += 1
                            break
                        for n in range(100): # 2p
                            tot = i*100 + j*50 + k*20 + l*10 + m*5 + n*2
                            if tot > 199:
                                if tot == 200: combos += 1
                                break
                            # 1p:
                            if i*100 + j*50 + k*20 + l*10 + m*5 + n*2 < 200: # then put 1p until 200p
                                combos += 1

    return combos

#-------------------------------------------------------------------------#

res = f1(200)

print(res)
