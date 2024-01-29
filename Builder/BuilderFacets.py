"""
Here the Person class has many attributes, and the PersonBuilder is a facade that
allows us to set them step by step. The PersonAddressBuilder and PersonJobBuilder
are both subclasses of PersonBuilder, and they are responsible for setting the
attributes related to address and job, respectively.

The PersonBuilder class has two properties, lives and works, which return instances
of PersonAddressBuilder and PersonJobBuilder, respectively. And since both of these
inherit from PersonBuilder and provide fluent methods for setting the attributes, we
can chain them together to set all the attributes of a Person object as necessary.
"""
from copy import deepcopy


class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}\n"
            + f"Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}"
        )


class PersonBuilder:  # facade
    def __init__(self, person: Person | None = None, copy=False) -> None:
        if person is None:
            self.person = Person()
        else:
            if copy:
                self.person = deepcopy(person)
            else:
                self.person = person

    def __str__(self) -> str:
        return f"\nBuilder({str(self.person)})\n"

    @property
    def lives(self) -> "PersonAddressBuilder":
        return PersonAddressBuilder(self.person)

    @property
    def works(self) -> "PersonJobBuilder":
        return PersonJobBuilder(self.person)

    def build(self) -> Person:
        return self.person


class PersonAddressBuilder(PersonBuilder):
    def at(self, street_address: str) -> "PersonAddressBuilder":
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode: str) -> "PersonAddressBuilder":
        self.person.postcode = postcode
        return self

    def in_city(self, city: str) -> "PersonAddressBuilder":
        self.person.city = city
        return self


class PersonJobBuilder(PersonBuilder):
    def at(self, company_name: str) -> "PersonJobBuilder":
        self.person.company_name = company_name
        return self

    def as_a(self, position: str) -> "PersonJobBuilder":
        self.person.position = position
        return self

    def earning(self, annual_income: int) -> "PersonJobBuilder":
        self.person.annual_income = annual_income
        return self


pb = PersonBuilder()
# Below we are using the PersonBuilder facade to set the attributes
# of a Person object step-by-step. And this is quite easy to read and understand.
person_a = (
    pb
        .lives
            .at("123 London Road")
            .in_city("London")
            .with_postcode("SW12BC")
        .works
            .at("Fabrikam")
            .as_a("Engineer")
            .earning(123000)
        .build()
)

print("Person A:", person_a)
print()

# When we are using the PersonBuilder facade, we are not directly interacting with
# the Person class. Instead, we are using the PersonBuilder facade to set the
# attributes of a Person object step-by-step. So this means we can use lives and works
# properties repeatedly to create multiple Person objects with different attributes.
person_b = (
    pb
        .works
            .at("Google")
            .as_a("Software Engineer")
            .earning(100000)
        .build()
)
person_c = (
    pb
        .lives
            .at("40710 1st Street")
            .in_city("New York")
            .with_postcode("10001")
        .build()
)

print("Person B:", person_b)
print()
print("Person C:", person_c)
print()

# We can also make modification to existing person object
pb = PersonBuilder(person_a)
person_d = (
    pb
        .lives
            .at("5689 Richmond Road")
            .in_city("Lisbon")
            .with_postcode("12345")
        .build()
)

print("Person D:", person_d)
print()
print("Person A:", person_a)
print()

# To avoid modifying the original person object, we can use deepcopy
pb = PersonBuilder(deepcopy(person_a))
person_e = (
    pb
        .lives
            .at("321 London Road")
            .in_city("London")
            .with_postcode("SW12BC")
        .build()
)

print("Person E:", person_e)
print()
print("Person A:", person_a)
print()


# Or we can use the copy parameter in the PersonBuilder constructor
pb = PersonBuilder(person_a, copy=True)
person_f = (
    pb
        .lives
            .at("321 London Road")
            .in_city("London")
            .with_postcode("SW12BC")
        .build()
)

print("Person F:", person_f)
print()
print("Person A:", person_a)
print()
