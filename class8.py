from abc import ABC ,abstractmethod
class bcd (ABC):
    def print(self,x):
        print("passed value:", x)
    @abstractmethod
    def task(self):
        print("we are in bcd task")
class test__class(bcd):
    def task (self):
        print("we are inside test class")
test__obj = test__class()
test__obj.task()
test__obj.print(100)
