"""Open Close Principle"""

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:

    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

# OCP = open for extension, closed for modification

class ProductFilter:
    # PRINCIPLE VIOLATION
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p
    
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

# Specification: Base class
class Specification:
    def is_satisfied(self, item):
        pass

    # Combine specifications
    def __and__(self, other):
        return AndSpecification(self, other)

# filter: Base class
class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):

    def __init__(self, color) -> None:
        super().__init__()
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):

    def __init__(self, size) -> None:
        super().__init__()
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        super().__init__()
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old): ')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f'- {p.name} is green')

    bf = BetterFilter()
    print('Green products (new): ')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'- {p.name} is green')

    print('Large products (new): ')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f'- {p.name} is large')

    print('Large Blue items')
    large = SizeSpecification(Size.LARGE)
    blue = ColorSpecification(Color.BLUE) 
    # large_blue = AndSpecification(large, blue)
    large_blue = large & blue
    for p in bf.filter(products, large_blue):
        print(f'- {p.name} is large and blue')
