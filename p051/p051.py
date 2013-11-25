#--------------------------------------------------------------------#

def f1(max):
    print("f1")

    # dict is a dictionary of:
    #
    # dict[length][last_digit] = some_list
    #
    # where some_list is the list of primes whose last digit is last_digit
    # and have length amount of digits. Only within each some_list
    # will we be able to form families. If two primes have different
    # amount of digits, obviously won't belong to the same family.
    # Also the last digit of any two members of a family must coincide.
    # Otherwise, it should be the digit that changes within the family,
    # and as it must be any 8 from [0..9], some of the "primes" would
    # not be prime, i.e. some would have to end in either 5 or an even
    # digit,
    # and as it must be any 8 from [0..9], some of the "primes" would
    # not be prime, i.e. some would have to end in either 5 or an even
    # digit..
    dict = {}

    # Sieve to find all primes up to max:
    composites = {}
    for mult in range(3,max,2):
        if not mult in composites:
            lp = len(str(mult))
            last_digit = str(mult)[-1]
            if not lp in dict:
                dict[lp] = {}

            if not last_digit in dict[lp]:
                dict[lp][last_digit] = []

            dict[lp][last_digit].append(mult)

            for i in range(mult*mult, max, 2*mult):
                composites[i] = True
    
    for length in sorted(dict.keys())[1:]: # ignore first one (length-1)
        print(length)
        for k,v in dict[length].items():
            print(k,dict[length][k])

#--------------------------------------------------------------------#

class Family(object):

    def __init__(self):
        self.members = []

    def can_join(self, newmember):
        '''
        Returns True if newmember can be a member of Family.
        '''

        for member in self.members:
            # Any 2 members of same family end in same digit:
            if str(member)[-1] != str(newmember)[-1]:
                return False

            s = []
            for a,b in zip(str(member), str(newmember)):
                if a != b:
                    s.append(b)
            
            for e in s[1:]:
                if e != s[0]:
                    return False

        print(newmember, s)
        return True

    def join(self, newmember):
        self.members.append(newmember)

    def __str__(self):
        return str(self.members)

#--------------------------------------------------------------------#

import timeit

# f1():
t = timeit.Timer('f1(100)', "from __main__ import f1")
t1 = t.timeit(number=1)

print("\nTimes:\n")
print(t1) # ~ s
