"""
This implementation aims to solve the problem of the need to modify the base 
builder class to add new functionality. This is done by creating a new builder
class that inherits from the previous builder class and adds the new functionality.
"""


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f"{self.name} born on {self.date_of_birth} works as a {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == "__main__":
    pb = PersonBirthDateBuilder()
    me = (
        pb.called("Dmitri").works_as_a("quant").born("1/1/1980").build()
    )  # this does NOT work in C#/C++/Java/...
    print(me)


"""
Personally I don't like this implementation. Overtime it would be 
very difficult to keep track of all the different inherited classes.
So, below is my opinionated implementation of the builder pattern.
"""
from abc import ABC
from copy import deepcopy


class PersonBuilderInterface(ABC):
    def __init__(self, person: Person | None = None, copy=True) -> None:
        if person is None:
            self.person = Person()
        else:
            if copy:
                self.person = deepcopy(person)
            else:
                self.person = person

    def build(self) -> Person:
        return self.person


class PersonInfoBuilder(PersonBuilderInterface):
    def called(self, name: str) -> PersonInfoBuilder:
        self.person.name = name
        return self


class PersonJobBuilder(PersonBuilderInterface):
    def works_as_a(self, position: str) -> PersonJobBuilder:
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonBuilderInterface):
    def born(self, date_of_birth: str) -> PersonBirthDateBuilder:
        self.person.date_of_birth = date_of_birth
        return self


"""
This implementation is more verbose, but it is more explicit and easier to
understand. But this might be a burden if you have a lot of different builders.
But I think it is worth it to make the builder understandable to the user.

Note: Here I had to override the builder methods to return the correct type
to allow for python's LSP to work properly. This would not have been necessary 
if I did not care about editor intellisense. In that case I could have just
Wrote the class like this:

>>> class OpinionatedPersonBuilder(PersonBirthDateBuilder, PersonInfoBuilder, PersonJobBuilder):
>>>     pass
"""
class OpinionatedPersonBuilder(
    PersonBirthDateBuilder, PersonInfoBuilder, PersonJobBuilder
):
    def called(self, name: str) -> 'OpinionatedPersonBuilder':
        return super().called(name)
    
    def works_as_a(self, position: str) -> 'OpinionatedPersonBuilder':
        return super().works_as_a(position)
    
    def born(self, date_of_birth: str) -> 'OpinionatedPersonBuilder':
        return super().born(date_of_birth)


if __name__ == "__main__":
    pb = OpinionatedPersonBuilder()
    me = (
        pb.called("Dimitri").works_as_a("chef").born("1/1/1980").build()
    )
    print(me)
