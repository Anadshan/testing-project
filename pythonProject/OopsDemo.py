# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods,  class variables, instance variables, constructor etc
# self keyword is mandatory for calling variable names into method
# instant and class variables have whole different purpose
# new keyword is not required when you create object

class Calculator:
    num = 100  # class variable

    def __init__(self, a, b):

        self.firstNumber = a
        self.secondNumber = b
        print("i am called automatically when object is created")



    def getData(self):
        print("Executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # syntax to create object in python
obj.getData()
print(obj.num)
print(obj.Summation())

obj1 = Calculator(4, 9)  # syntax to create object in python
obj1.getData()
print(obj1.num)
print(obj1.Summation())
