# Design patterns

This repository contains snippets of code that demonstrate the use of design patterns in Python.
These are part of the course that I am learning from the course [Design Patterns in Python](https://www.udemy.com/course/design-patterns-python/) by [Dmitri Nesteruk](https://www.udemy.com/user/dmitrinesteruk/).

Two of the best resources I came across for learning design patterns are:
- [Sourcemaking](https://sourcemaking.com/design_patterns)
- [Refactoring Guru](https://refactoring.guru/design-patterns).


## Table of contents

- [Design patterns](#design-patterns)
	- [Table of contents](#table-of-contents)
	- [SOLID design principles](#solid-design-principles)
	- [Gama categorization of design patterns](#gama-categorization-of-design-patterns)
		- [Summary of these categories](#summary-of-these-categories)
			- [Creational design patterns](#creational-design-patterns)
			- [Structural design patterns](#structural-design-patterns)
			- [Behavioral design patterns](#behavioral-design-patterns)
	- [Creational design patterns](#creational-design-patterns-1)
	- [Structural design patterns](#structural-design-patterns-1)



## [SOLID design principles](./SOLID/)

These are introduced by Robert C. Martin eg. Uncle Bob.


## Gama categorization of design patterns

Design patterns are categorized into three categories. This is called the Gama categorization of design patterns. The name comes from one of the authors of the book [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides. The authors are also known as the Gang of Four (GoF).

The three categories are:

1. Creational design patterns
2. Structural design patterns
3. Behavioral design patterns

### Summary of these categories

#### Creational design patterns

- Deal with the creation of objects. 
- Explicit (constructor) vs implicit (DI, reflection, etc.).
- Wholesale (single statement) vs piecewise (step-by-step).


#### Structural design patterns

- Concerned with the structure (e.g., class members).
- Many patterns are wrappers that mimic the underlying class' interface.
- Stress the importance of good API design.


#### Behavioral design patterns

- They are all different; no central theme.


## Creational design patterns

Creational design patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation. They provide a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes. The basic form of object creation could result in design problems or add complexity to the design. Creational design patterns solve this problem by controlling this object creation.

Here are some examples of creational design patterns:

1. **Singleton Pattern**: This pattern ensures that a class has only one instance, and provides a global point of access to it. It is used in logging, driver objects, caching, thread pool, database connections, etc.
2. **Factory Method Pattern**: This pattern provides a way to delegate the instantiation logic to child classes. It is used in classes that have some generic processing in a class but required subclass to decide which class to instantiate.
3. **Abstract Factory Pattern**: This pattern provides a way to encapsulate a group of individual factories that have a common theme. It is useful when the system has to be independent from how its products are created, composed, and represented.
4. **Builder Pattern**: This pattern builds a complex object using simple objects and using a step-by-step approach. It is useful when you need to create an object with lots of possible configuration options.
5. **Prototype Pattern**: This pattern involves creating new objects by copying existing objects. It's useful when object creation is time-consuming, and you want to avoid redundancy in the initialization process.

Each of these patterns can be used to control and manage the way objects are created based on the requirements of your software.


## Structural design patterns

Structural patterns are concerned with object composition and typically identify simple ways to realize relationships between different objects. They help ensure that when one part of a system changes, the entire structure of the system doesn't need to do the same. They also help in recasting parts of the system which don't fit a particular purpose into those that do.

Here are some examples of structural design patterns:

1. **Adapter Pattern**: This pattern allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.
2. **Bridge Pattern**: This pattern decouples an abstraction from its implementation so that the two can vary independently. It is used when a class has two (often orthogonal) dimensions of change.
3. **Composite Pattern**: This pattern composes objects into tree structures and then works with these structures as if they were individual objects. It is used when you want to represent part-whole hierarchies of objects.
4. **Decorator Pattern**: This pattern dynamically adds/overrides behavior in an existing method of an object. It is used when you want to add state to individual objects at run-time.
5. **Facade Pattern**: This pattern provides a simplified interface to a complex subsystem. It is used when you want to provide a simple interface to a complex subsystem.
6. **Flyweight Pattern**: This pattern reduces the cost of complex object models by dividing them into two parts: a core (intrinsic) part and a variable (extrinsic) part. It is used when you need to create a large number of similar objects.
7. **Proxy Pattern**: This pattern provides a placeholder for another object to control access, reduce cost, and reduce complexity. It is used when you need to represent a complex/expensive object with a simpler one.
8. **Private Class Data Pattern**: This pattern helps to reduce the accessibility of class attributes by separating them into another class. It is used when you need to separate the data from the behavior that manipulates the data.
