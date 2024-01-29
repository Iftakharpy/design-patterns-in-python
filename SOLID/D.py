"""
D - Dependency Inversion Principle

D in SOLID stands for Dependency Inversion Principle. This principle states that,
high-level modules should not depend on low-level modules. Instead, they should
both depend on abstractions. This essentially means we should not care about how
the low-level modules are implemented works and we should only care about the abstractions.

Note: This does not relate to the dependency inversion principle of object-oriented
programming.
"""

from abc import ABC, abstractmethod
from enum import Enum


class Relationship(Enum):
	PARENT = 1
	CHILD = 2
	SIBLING = 3

class Person:
	def __init__(self, name):
		self.name = name


class Relationships:
	def __init__(self):
		self.relations = []

	# Here the low-level module is using 3 element tuples to 
	# store the relationships in a list.
	def add_parent_and_child(self, parent, child):
		# parent is parent of child
		self.relations.append(
			(parent, Relationship.PARENT, child)
		)
		# child is child of parent
		self.relations.append(
			(child, Relationship.CHILD, parent)
		)


class Research:
	# Here the high-level module(Research) is using the low-level module
	# to get the relationships and then filter them.
	def __init__(self, relationships):
		relations = relationships.relations
		for r in relations:
			# Here the high-level module is depended on the implementation
			# of the low-level module. This is a violation of the Dependency
			# Inversion Principle. If the implementation of the low-level module
			# changes, then the high-level module will also have to change.
			# We should avoid this, and instead depend on abstractions.
			if r[0].name == 'John' and r[1] == Relationship.PARENT:
				print(f'John has a child called {r[2].name}.')


# Here we are creating a list of people.
parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# Here we are creating a Relationships object and adding the relationships
# to it.
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

# Here we are creating a Research object and passing the Relationships object
# to it.
Research(relationships)



"""
Here we are creating an abstract class for the low-level module.
"""
class RelationshipBrowser(ABC):
	@abstractmethod
	def find_all_children_of(self, name):
		pass

"""
Here we are creating a low-level module, which implements the abstract class.
This is a better implementation, because now the high-level module now depends
on the abstraction, and not the implementation of the low-level module.
"""
class BetterRelationships(RelationshipBrowser):
	def __init__(self):
		self.relationships = []

	def add_parent_and_child(self, parent, child):
		self.relationships.append(
			(parent, Relationship.PARENT, child)
		)
		self.relationships.append(
			(child, Relationship.CHILD, parent)
		)

	def find_all_children_of(self, name):
		for r in self.relationships:
			if r[0].name == name and r[1] == Relationship.PARENT:
				yield r[2].name


"""
Here we are creating a high-level module, which depends on the abstraction
of the low-level module. This is a better implementation, because now the
high-level module is not depended on the implementation of the low-level
module.

Now, if the implementation of the low-level module changes to a database storage,
then the high-level module will not have to change. This is because the high-level
module is only depended on the abstraction RelationshipBrowser.
"""
class BetterResearch:
	def __init__(self, browser):
		for p in browser.find_all_children_of('John'):
			print(f'John has a child called {p}.')


# Here we are creating a list of people.
parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# Here we are creating a BetterRelationships object and adding the relationships
# to it.
relationships = BetterRelationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

# Here we are creating a BetterResearch object and passing the BetterRelationships
# object to it.
BetterResearch(relationships)

