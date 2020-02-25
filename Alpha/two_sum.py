def two_sum(ls, target):
    d = {}
    for i in range(len(ls)):
        val = ls[i]
        if val in d:
            return d[val], val
        else:
            d[target-val] = val
            print(d)
    return False
ls = [2,4,6]
print(two_sum(ls,10))