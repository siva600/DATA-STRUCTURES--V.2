# single object creation
# https://www.youtube.com/watch?v=6IV_FYx6MQA
class SingeleTon(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(SingeleTon, self).__new__(self)
            self.y = 10
        return self._instance


# https://www.youtube.com/watch?v=wElVjMlYVAw
class SingleTon2(object):
    # new method is basically used ofr creating an object. This is called for object creation and instance.
    def __new__(cls, *args, **kwargs):
        # check is there any attribute available ..
        if not hasattr(cls, '_instance'):
            # create the actual object using super keywoed. and stored in cls attribute instance
            cls._instance = super(SingleTon2, cls).__new__(cls)
        # if it already has the _instance attribute it will return the existing object
        return cls._instance



obj = SingeleTon()
print obj.y
obj.y = 20
print obj.y

obj2 = SingeleTon()
print obj2.y

print(id(obj))
print(id(obj2))

