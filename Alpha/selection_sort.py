# selection sort with O(n*n) worst timing complexity.

def selection_sort(l):
    for start in range(len(l)):
        min =  start
        for j in range(min, len(l)):
            if l[j] < l[min]:
                min = j
        (l[start], l[min]) = (l[min], l[start])
    return l

print selection_sort([1,2,9,10,0,5])

