# using quick sort for a given list of items
# steps : 
# 1. pick a pivot
# 2. move the items less than pivot to left side
# 3. move the items greater than pivot to right side
# 4. if the result is not sorted, follow the process recursively for # left items and right items
# in place sorting not extra space needed.
# https://medium.com/basecs/pivoting-to-understand-quicksort-part-1-75178dfb9313

def quick_sort(sequence):
  length = len(sequence)
  if len(sequence) <= 1:
    return sequence
  else:
    pivot = sequence.pop()  # here picking last item as the pivot.
    # pivot = len(sequence)//2
    # print(pivot)
  
  items_lower = []
  items_greater = []
  for item in sequence:
    if item > pivot:
      items_greater.append(item)
    else:
      items_lower.append(item)
  
  return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

sequence = [4,5,10,0,1,2,8, 11, 20,20,20, 25]
print(quick_sort(sequence))