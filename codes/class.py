class Addition:

    # parameterized constructor
    # __init__ is used to pass parameters in a class... these parameters can be
    # accessed by each and every functions inside the class
    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    def showAnswer(self):
        print(self.answer)
    # the parameters passed by the __init__ method are stored in self.  variables.
    # to access these variables we must pass self as a variable in these functions 
    def display(self,x):
        print("Addition of two numbers = " + str(self.answer))
        #this x is not passed using __init__. so we can only use it inside this function
        print(x*x)
    
    def calculate(self):
        self.answer = self.first + self.second
    
    # even to call a function inside another one, we need to use the self keyword
    def minus(self):
        self.answer = self.first - self.second 
        self.showAnswer()

    # even if we don't use the parameters, we must pass the self parameter in all 
    # functions  inside the class
    def multiply(self,a,b):
        print(a*b)

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)
 
# perform Addition
obj.calculate()
 
# display result
obj.display(4)

obj.minus()
obj.multiply(2,6)