"""
L - Liskov's Substitution Principle

L in SOLID stands for Liskov's Substitution Principle. The idea here is that, 
when we have a base class and a derived class, then the derived class should 
be able to substitute the base class without any unexpected behavior.
"""



class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


"""
Here we have a derived class Square of Rectangle. And we have a function use_it, 
which takes a Rectangle object and does something with it. Now, if we pass a Rectangle 
object to this function, everything is fine. But if we pass a Square object to this 
function, then we get an unexpected result.

The reason for this is that the Square class overrides the width and height properties, 
and sets them to the same value. This is not the same behavior as the Rectangle class, 
and therefore, the Square class is not a proper substitute for the Rectangle class. This 
is a violation of the Liskov's Substitution Principle.
"""
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


"""
The solution to this problem is to not use inheritance in this case. Instead, we can
use composition. We can create a separate class, called RectangleFactory, which will
create Rectangle objects. And we can create another class, called SquareFactory, which
will create Square objects. And then we can pass these objects to the use_it function.
"""
def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)


"""
The solution to this problem is to not use inheritance in this case. Instead, we can
use composition. We can create a separate class, called RectangleFactory, which will
create Rectangle objects. And we can create another class, called SquareFactory, which
will create square by using same value in width and height. And then we can pass these 
objects to the use_it function.

Now, if we run this code, we get the expected result. The RectangleFactory creates a
Rectangle object, and the SquareFactory creates a Square object. And we can pass these
objects to the use_it function, and we get the expected result.
"""
class RectangleFactory:
	@staticmethod
	def create_rectangle(width, height):
		return Rectangle(width, height)
     
class SquareFactory:
	@staticmethod
	def create_square(size):
		return Rectangle(size, size)
     
rcf = RectangleFactory()
rc = rcf.create_rectangle(3, 4)
use_it(rc)

sqf = SquareFactory()
sq = sqf.create_square(5)
use_it(sq)


