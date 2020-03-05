# single object creation
# https://www.youtube.com/watch?v=6IV_FYx6MQA
class SingeleTon(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(SingeleTon, self).__new__(self)
            self.y = 10
        return self._instance


obj = SingeleTon()
print obj.y
obj.y = 20
print obj.y

obj2 = SingeleTon()
print obj2.y

print(id(obj))
print(id(obj2))

