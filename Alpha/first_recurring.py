# given 'ABCA' - return A
# given 'BCABA' - return B - first recurring is B

def recurring(s):
    d = {}
    for item in s.lower():
        if item not in d:
            d[item] = 1
        else:
            print(d)
            return item
    return None
print(recurring('ABCDcadajkfahfoqjfpqobqn'))

