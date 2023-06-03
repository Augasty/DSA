class Math:
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def show(self):
        print(self.answer)

    def plus(self):
        self.answer = self.first + self.second
        self.show()

    def minus(self):
        self.answer = self.first - self.second
        self.show()

    def multiply(self):
        self.answer = self.first * self.second
        self.show()


obj = Math(4,2) 

# obj.show()  #gives the error (AttributeError: 'Math' object has no attribute 'answer')
            #as self.answer is not defined yet.

obj.plus() #self.answer = 6
obj.minus() #self.answer is updated, and is now = 2
obj.multiply() #self.answer is updated once again , and is now = 8


obj.show() #self.answer = 8 , last updated value