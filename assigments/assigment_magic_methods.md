# Magic method assignment
This assigment is to make sure we can compare the human class. We must be able to check if they are the same.
We must be able to sort a population also in 2 ways. Therefore, make a new property to the class example: 
`population.sort_method = 'age'`
`population.sort_method = 'name'`
Sorting a list of human should always sort by name, but a Population
should be able to sort by age and name.
Also, if we have two Humans declared we should be able to know if they are equal.
That would look like:
```
Human(Erica,21,'female') == Human(Erica,21,'female')
True
```
To implement, look at the `__eq__` method and check if Human.age == the other Human.age + all the other sub-properties 
like gender and name.
