def subset(s):
    # using recursion
    if s == []:
        return [[]]
    else:
        a = subset(s[1:])
        return a + [[s[0]] + b for b in a]

def subset2(s):
    a = [[]]
    for i in range(len(s)+ 1):
        for j in range(i+1, len(s)+1):
            a.append(s[i:j])
    return a

s = [1,2,3]
print(subset(s))
print(subset2(s))