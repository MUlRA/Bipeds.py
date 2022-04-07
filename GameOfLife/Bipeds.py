from pprint import pprint


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
        self.pop_list = humans

    def filter_gender(self, value):
        fgend_list = []
        value = value.lower()
        for people in self.pop_list:
            if people.gender.lower() == value:
                fgend_list.append(people.name)
        fgend_list.sort()
        return fgend_list

    def filter_generation(self, gen):
        """
             filter_generation must go through all humans in population and make a new list of humans to return if they match the given generation.
             It has one generation
             """

        #key, value
        gen = gen.lower()
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
                return gen_list
        print(gen_mapping[self])

    def (self, value):

        value = value.lower()
        genx_list = []
        # 1965-80
        mill_list = []
        # 1981-96
        genz_list = []
        # 1997-12
        gena_list = []
        # 2010-20

        #key, value. Mapper|Dictionary
        gen_mapping = {
            'genx': range(1965, 1980),
            'genz': range(1997, 2012),
            'gena': range(2010, 2020),
            'mill': range(1981, 1996)
        }
        if "auto" in value.lower():
            for people in self.pop_list:
                for key, z in gen_mapping.items():
                    if people.birthday in z:
                        genx_list.append(people.name)
            return genx_list
        else:
            return genx_list
            pprint("There is no human in the given list!")

        if "x" in value:
            for people in self.pop_list:
                if people.birthday in range(1965, 1980):
                    genx_list.append(people)
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
pprint(population.find("mill"))
