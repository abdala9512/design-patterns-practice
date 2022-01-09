"""Liskov Substitution Principle"""


class Rectangle:

    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width
    
    @property
    def area(self):
        return self._width * self._height

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
    
    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'

# PROBABLY WE DON'T NEED A SQUARE CLASS
class Square(Rectangle):

    def __init__(self, size) -> None:
        Rectangle.__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width =self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width =self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10 # THIS SETTER ONLY WORKS IN RECTANGLE, IT'S NOT POSSIBLE  EXTEND THE RECTANGLE CLASS
    expected = int(w*10)
    assert expected == rc.area
    print(f'rectangle area: {rc.area}, expected area: {expected}')

rc= Rectangle(2,3)
use_it(rc)

sq= Square(5)
use_it(sq)