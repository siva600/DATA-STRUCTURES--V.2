# two sum.


# find a pair with sum as 7.

# x = []
# def two_sum(ls):
#    (i,k) = (0, i+1)
#    while i < len(ls):
#        if ls[i] + ls[k] == 7:
#            x.append((ls[i], ls[k]))
#         (i, k) = (i+1, k+1)
#         two_sum(ls[i:k])
# l = [1,2,3,4,5,5,2]
# print(two_sum(l))

class Solution:
    def twosum(self, lst, target):
        dict = {}
        for i in range(0, len(lst)):
            val = lst[i]
            if (target - val) in dict:
                return dict[target - val], i
            # print(dict)
            dict[val] = i + 1


lst = [2, 7, 11, 15]
target = 22
s = Solution()
print(s.twosum(lst, target))