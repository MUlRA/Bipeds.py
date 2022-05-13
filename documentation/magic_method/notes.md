# Magic methods notes

## What are magic methods
Magic methods are known methods that a class can implement for built in behavior.
For example:
`str([1,2,3])` returns `[1, 2, 3]`
How does python knows how to print a list? It's because of the list class implementation of the `__str__` method.

Here is a more concrete example.
``
class Badass(object):
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport.lower()

    def __str__(self):
        return "{name} is a badass. His age is {age} and he won all the prizes playing {sport}.".format(name=self.name,
                                                                                                        age=self.age,
                                                                                                        sport=self.sport)
print(str(Badass("Nick", 21, "Professionnal Marco Polo")))
``
Which returns `Nick is a badass. His age is 21 and he won all the prizes playing Professionnal Marco Polo.`

The magic methods that can be implemented can serve for comparison characters like: =,<,>,etc...
Before going and reading the docs here keep in mind that they are also referred to as Dunder methods. Don't know why I 
never use that term myself.
Here is a list of the implementable methods:
https://www.tutorialsteacher.com/python/magic-methods-in-python#:~:text=Python%20%2D%20Magic%20or%20Dunder%20Methods,class%20on%20a%20certain%20action.

and here is the complete documentation:
https://docs.python.org/3/reference/datamodel.html#basic-customization

Magic methods are automation for classes because they are the source of implementing behaviors we are used too with most
basic type class. 

Now no ones knows what you can implement by heart, but a quick search online for `python implementing smaller then`
returns interesting sites and one of which with that example which I will vendor.
This example shows how now we can compare a person to sort them.
```
class Person:
    def __init__(self, age):
        self.age = age
    def __lt__(self, other):
        return self.age < other.age
alice = Person(10)
bob = Person(12)
print(alice < bob)
# True
print(bob < alice)
# False
```

Now in the case of sorting people by their name or age or salary, as long as the doc string reflects and document the 
coded behavior.