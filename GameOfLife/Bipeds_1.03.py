from pprint import pprint


class Human:
    def __init__(self, name, birthday, gender):
        self.name = name
        self.birthday = birthday
        self.gender = gender


class Population:
    def __init__(self, humans):
        self.pop_list = humans

    def filter_gender(self, value):
        fgend_list = []
        value = value.lower()
        for people in self.pop_list:
            if people.gender.lower() == value:
                print(people.name)
                fgend_list.append(people)
        fgend_list.sort()
        return fgend_list

    def filter_generation(self, gen):
        """
             filter_generation must go through all humans in population and make a
              new list of humans to return if they match the given generation.
             It has one generation
             """

        #key, value
        gen_list = []
        gen_mapping = {
                'genx': range(1965, 1980),
                'genz': range(1997, 2012),
                'gena': range(2010, 2020),
                'mill': range(1981, 1996)
            }
        for key, r in gen_mapping.items():
            if key in gen.lower():
                print(r)
                for people in self.pop_list:
                    if people.birthday in r:
                        gen_list.append(people)
                        print(people.name)
                    else:
                        continue
                gen_list.sort()
                return gen_list
        print(gen_mapping[self])

    def sort_name(self):
        sorted_list = []
        for people in self.pop_list:
            sorted_list.append(people.name)
        sorted_list.sort()
        print(sorted_list)
        return sorted_list


people_list = [
    Human("Bob", 2006, "Robot"),
    Human("Cath", 1980, "Female"),
    Human("Zach", 2012, "Male"),
    Human("Alice", 1995, "Female"),
]

population = Population(people_list)
population.filter_gender('female')
""" 
'genx': range(1965, 1980),
'genz': range(1997, 2012),
'gena': range(2010, 2020),
'mill': range(1981, 1996)"""
