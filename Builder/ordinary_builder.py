"""
Builder is a creational design pattern that lets you construct complex objects step by step.

When piecewise object construction is complicated, provide an API for doing it succinctly.
"""



class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []
    
    def __str__(self):
        return self.__str(0)

    def __str(self, indent):
        lines = []
        indentation = ' ' * (indent * self.indent_size)
        # Opening tag
        lines.append(f'{indentation}<{self.name}>')

        # Inner Text
        if self.text:
            lines.append(f'{indentation} {self.text}')
        
        # Child Elements
        for element in self.elements:
            lines.append(element.__str(indent + 1))

        # Closing tag
        lines.append(f'{indentation}</{self.name}>')
        return '\n'.join(lines)
    

    """
    This breaks the open-closed principle, because we are depending on the
    HtmlBuilder class. So, when HtmlBuilder changes, this class will also
    need to change.

    But this is ok since Builder and the classes it builds are usually 
    tightly coupled anyway.

    This gives an alternative way to create an HtmlElement object. Instead 
    of calling HtmlBuilder which might be a little hard to remember, we can
    just call HtmlElement.create() which is easier to remember and relate to.
    """
    @staticmethod
    def create(name):
        return HtmlBuilder(name)



class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)
    
    def __str__(self):
        return str(self.__root)

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)
    
    # Not fluent, this does not allow us to chain methods
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
    
    # Fluent, this allows us to chain methods
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self
    

# Non-fluent builder
builder_not_fluent = HtmlBuilder('ul')
builder_not_fluent.add_child('li', 'hello')
builder_not_fluent.add_child('li', 'world')
print('Ordinary builder:')
print(builder_not_fluent)

# Fluent builder
builder_fluent = HtmlBuilder('ul')
builder_fluent \
    .add_child_fluent('li', 'hello') \
    .add_child_fluent('li', 'world')
print()
print('Fluent builder:')
print(builder_fluent)


# This is a better way to create HtmlElement with fluent builder
builder = HtmlElement.create('ul')
builder \
    .add_child_fluent('li', 'hello') \
    .add_child_fluent('li', 'world')
print()
print('Better way to create an HtmlElement object:')
print(builder)
