"""
O - Open/Closed Principle (Open for extension, closed for modification)

When a new functionality is needed, we should be able to extend a class's behavior, without modifying it.
Some benefits of this principle are:
	1. Less code to maintain.
	2. Less bugs.
	3. Less side effects.
	4. Less coupling.
	5. Less ripple effects.
"""

from typing import Iterator, Iterable
from abc import ABC, abstractmethod
from enum import Enum


class MakePrintable:
	def __str__(self):
		return f"{self.__class__.__name__}({", ".join([f"{v}" for k, v in vars(self).items()])})"
		
	def __repr__(self):
		return str(self)

class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4

class Size(Enum):
	SMALL = 1
	MEDIUM = 2
	LARGE = 3

class Product(MakePrintable):
	def __init__(self, name: str, color: Color, size: Size):
		self.name = name
		self.color = color
		self.size = size
	

"""
This is bad because if we add new attributes to the Product class, we will have to modify the filter class.
And suppose we add just 1 more attribute, then we will have to add more methods to cover all the filtering.
Let's say we add a new attribute gender. The new methods we will have to add are:
	1. filter_by_gender
	2. filter_by_color_and_gender
	3. filter_by_size_and_gender
	4. filter_by_color_size_and_gender

Now, imagine over time our Product class which will be almost impossible to maintain all the combination of filter 
methods. Also if we want to change something we will have to modify the previously written code. Which is not 
always possible when we are using an external library. But in the process of modifying you might break previously 
tested specifications. This is not good.
"""
class ProductFilter:
	def filter_by_color(self, products: Iterable[Product], color: Color) -> Iterator[Product]:
		for p in products:
			if p.color == color:
				yield p

	def filter_by_size(self, products: Iterable[Product], size: Size) -> Iterator[Product]:
		for p in products:
			if p.size == size:
				yield p

	def filter_by_size_and_color(self, products: Iterable[Product], size: Size, color: Color) -> Iterator[Product]:
		for p in products:
			if p.size == size and p.color == color:
				yield p


"""
To solve the problem we can use the Open/Closed Principle. We are going to use the Specification Pattern which is 
one of the Enterprise Patterns.
"""
class Filter(ABC):
	@abstractmethod
	def filter(self, items: Iterable[Product], spec: 'Specification') -> Iterator[Product]:
		pass

class Specification(ABC):
	@abstractmethod
	def is_satisfied(self, item: Product) -> bool:
		pass
	
	# This overwrites the `&` operator. So we can write large_and_green = large & green
	# Here large and green are two Specification objects.
	# Unfortunately, we can not overwrite `and` operator. Because it is not possible in Python.
	def __and__(self, other: 'Specification') -> 'Specification':
		return AndSpecification(self, other)

	# This overwrites the `|` operator. So we can write large_and_green = large | green
	# Here large and green are two Specification objects.
	# Unfortunately, we can not overwrite `or` operator. Because it is not possible in Python.
	def __or__(self, other: 'Specification') -> 'Specification':
		return OrSpecification(self, other)

class AndSpecification(Specification):
	def __init__(self, *args: Specification):
		self.args = args

	def is_satisfied(self, item: Product) -> bool:
		return all(map(lambda spec: spec.is_satisfied(item), self.args))

class OrSpecification(Specification):
	def __init__(self, *args: Specification):
		self.args = args

	def is_satisfied(self, item: Product) -> bool:
		return any(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
	def filter(self, items: Iterable[Product], spec: Specification) -> Iterator[Product]:
		for item in items:
			if spec.is_satisfied(item):
				yield item



class SizeSpecification(Specification, MakePrintable):
	def __init__(self, size: Size):
		self.size = size
		
	def is_satisfied(self, item: Product) -> bool:
		return item.size == self.size

class ColorSpecification(Specification, MakePrintable):
	def __init__(self, color: Color):
		self.color = color

	def is_satisfied(self, item: Product) -> bool:
		return item.color == self.color




# products
apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)
banana = Product("Banana", Color.YELLOW, Size.SMALL)
grape = Product("Grape", Color.YELLOW, Size.SMALL)
pineapple = Product("Pineapple", Color.YELLOW, Size.LARGE)
mango = Product("Mango", Color.YELLOW, Size.MEDIUM)
orange = Product("Orange", Color.YELLOW, Size.MEDIUM)

products = [apple, tree, house, banana, grape, pineapple, mango, orange]

# old filter
pf = ProductFilter()
print("Green products (old):")
for p in pf.filter_by_color(products, Color.GREEN):
	print(f" - {p}")
print()

# new filter
bf = BetterFilter()
print("Green products (new):")
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
	print(f" - {p}")

print("Large products:")
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
	print(f" - {p}")

print()
print("Large and green items:")
# This is possible because of the __and__ method in the Specification class.
# Otherwise we would have written AndSpecification(large, green)
large_and_green = large & green
for p in bf.filter(products, large_and_green):
	print(f" - {p}")

print()
print("Large or green items:")
# This is possible because of the __or__ method in the Specification class.
# Otherwise we would have written OrSpecification(large, green)
large_or_green = large | green
for p in bf.filter(products, large_or_green):
	print(f" - {p}")

# Because of this excellent design pattern we can combine the specifications in any way we want.
# Examples:
# 1. large_and_green = large & green
# 2. large_or_green = large | green
# 3. large_and_green_or_yellow = (large & green) | yellow
# 4. large_and_green_or_yellow = large & (green | yellow)
# and so on...
