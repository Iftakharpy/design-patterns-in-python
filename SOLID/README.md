# Summary

This is a simple summary of the SOLID principles. More explained examples can be found in the files.


## S - Single Responsibility Principle

- A class should have only one reason to change.
- Separation of concerns - different classes handling different, independent tasks/problems.
- If a class has more than one responsibility, it becomes coupled. A change to one responsibility results to modification of the other responsibility.
- Separation of concerns is the core to software design. So, we need to create classes that handle only one thing/job.


## O - Open Closed Principle

- Classes should be open for extension but closed for modification.
- We should be able to add new features to an object without modifying it.


## L - Liskov's Substitution Principle

- We should be able to substitute a base type for a subtype.
- More formally, the subtypes must be substitutable for their base types.


## I - Interface Segregation Principle

- Don't put too much into an interface; split into separate interfaces.
- YAGNI - You Ain't Going to Need It.


## D - Dependency Inversion Principle

- High-level modules should not depend upon low-level ones; use abstractions.