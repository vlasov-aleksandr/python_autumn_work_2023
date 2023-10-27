# задание 17-2
print('задание 17-2')
def upper_decorator(func):
    def wrapper(*args,**kwargs):
        res=[]
        for x in args:
            if type(x) == str:
             res.append(x.upper())
        for y in kwargs:
            if type(kwargs[y]) == str:
                res.append(kwargs[y].upper())
        return res
    return wrapper
@upper_decorator
def func(*args,**kwargs):
    return
print (func(1, 'a', 2, 'bcd, 345', '678', 'EFG', 'h9IJk'))

print()

# задание 17-3
print('задание 17-3')
class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def Colour(self):
        print(self.colour)
        
    def Square(self):
        print(self.square)

a = Shape('Red', 10)
b = Shape('Blue', 15)

a.Colour()
b.Colour()

a.Square()
b.Square()
