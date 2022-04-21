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
        """

        :param value:
        :return:
        """
        fgend_list = []
        value = value.lower()
        for people in self.pop_list:
            if people.gender.lower() == value:
                fgend_list.append(people)
        return fgend_list

    def filter_generation(self, gen):
        """
             filter_generation must go through all humans in population and make a
              new list of humans to return if they match the given generation.
             It has one generation
             """

        # key, value
        hum_gen_list = []
        gen_mapping = {
            'genx': range(1965, 1980),
            'genz': range(1997, 2012),
            'gena': range(2010, 2020),
            'mill': range(1981, 1996)
        }
        for key, gen_range in gen_mapping.items():
            if key == gen.lower():
                for people in self.pop_list:
                    if people.birthday in gen_range:
                        hum_gen_list.append(people)
                return hum_gen_list

    def sort_name(self):
        """
        This is a function that goes through the names of a given list of human and return it sorted.
        :return: list of humans
        """
        sorted_list = []
        for people in self.pop_list:
            sorted_list.append(people)
        sorted_list.sort()
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

