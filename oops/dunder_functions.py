# dunder methods/ magic methods include : __init__(), __len(), __contains__(), __new__(), __slots__(), __getitem__(), __iter__()
# https://rszalski.github.io/magicmethods/

class Countries:
    def __init__(self):
        self._members = ['India', 'America', 'England', 'Russia', 'China']

    def __len__(self):
        return len(self._members)

    def __contains__(self, item):
        return item in self._members

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._members.pop(item)

    def __iter__(self):
        while self._members:
            yield self._members.pop()


union = Countries()  # initialize the object

print "Get 1st item:", union[0]     # use get item to fetch an item from the created object.

for item in union:  # use union as iterator to fetch one by one using generator.
    print "generated item:", item

print "length: ", len(union)   # finally get length of items. This would return 0.

union2 = Countries()
print "length for 2nd object: ", len(union2)
