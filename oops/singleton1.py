# single object creation
class SingleTon:
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(SingleTon, self).__new__(self)
            self.y = 10
        return self._instance

obj = SingleTon()
obj.y = 10
print(obj.y)

# 
obj2 = SingleTon()
print(obj.y)


print(id(obj))
print(id(obj2))

