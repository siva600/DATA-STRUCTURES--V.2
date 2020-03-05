# single object creation
# https://www.youtube.com/watch?v=6IV_FYx6MQA
# singleton using self.
class SingeleTon(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(SingeleTon, self).__new__(self)
            self.y = 10
        return self._instance


# https://www.youtube.com/watch?v=wElVjMlYVAw
# singleton using cls instance.
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
print(obj.y)
obj.y = 20
print(obj.y)

obj2 = SingeleTon()
print(obj2.y)

print(id(obj))
print(id(obj2))


# ************************************
# Create a singleton using a decorator.
def singleton3(myClass):
    instances = {}  # create a instance dict to store instances.

    # passing the args and kwargs to accept any items in myClass
    def create_instance(*args, **kwargs):
        if myClass not in instances:
            # if the instance is not in out dict assign a new instance here.
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return create_instance

# assign the decorator to the destiny singleton class
@singleton3
class TestClass(object):
    pass


x = TestClass()
x.data = 10
print(x.data)

y = TestClass()
print(y.data)

