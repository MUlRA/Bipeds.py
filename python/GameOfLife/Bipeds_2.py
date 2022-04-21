from pprint import pprint
from Lists import people_list


class Human():
    def __init__(self, name, birthday, gender):
        self.name = name
        self.birthday = birthday
        self.gender = gender

    def generation(self):
        if self.birthday in range(1990, 2000):
            return "Gen X"
        else:
            return "Not Gen X"


class Population:
    def __init__(self, humans):
        self.population = people_list
        self.pop_list = humans
        self.function = input("Please select function; \n")
        print(self.function)


    def main(self):
        function = self.function.lower()
        if "gender" in function:
            value = input("Please input Gender; \n")
            print(value)
            population.filter_gender(value)

        if "genera" in function:
            value = input("Please input Generation; \n")
            print(value)
            population.filter_generation(value)

        if "name" in function:
            self.sort_name()
        else:
            print("This is not a function, please try again!")

    def filter_gender(self, value):
        fgend_list = []
        value = self.value.lower()
        for people in self.pop_list:
            people.gender.lower()
            if people.gender == value:
                fgend_list.append(people.name)

        fgend_list.sort()
        return fgend_list

    def filter_generation(self):
        """
        filter_generation must go through all humans in population and make a new list of humans to return if they match the given generation.
        It has one generation
        """
        value = self.value.lower()
        genx_list = []
        # 1965-80
        mill_list = []
        # 1981-96
        genz_list = []
        # 1997-12
        gena_list = []
        # 2010-20
        if "x" in value:
            for people in self.pop_list:
                if people.birthday in range(1965, 1980):
                    genx_list.append(people.name)
                    return genx_list

            else:
                return "There is no Gen X in the given list!"

        if "mil" in value:
            for people in self.pop_list:
                if people.birthday in range(1981, 1996):
                    mill_list.append(people.name)
                    return mill_list

            else:
                return "There is no millennial in the given list!"

        if "alpha" in value:
            for people in self.pop_list:
                if people.birthday in range(2010, 2020):
                    gena_list.append(people.name)
                    return gena_list

            else:
                return "There is no Gen Alpha in the given list!"

        if "z" in value:
            for people in self.pop_list:
                if people.birthday in range(1997, 2012):
                    genz_list.append(people.name)
                    return genz_list

            else:
                return "There is no Gen Z in the given list"

        genx_list.sort()
        mill_list.sort()
        genz_list.sort()
        gena_list.sort()

    def sort_name(self):
        sorted_list = []
        for people in self.pop_list:
            sorted_list.append(people.name)
        sorted_list.sort()
        return sorted_list


people_list = [
    Human("Bob", 2006, "Robot"),
    Human("Cath", 1980, "Female"),
    Human("Zach", 2012, "Male"),
    Human("Alice", 1995, "Female"),
]

population = Population(people_list)
