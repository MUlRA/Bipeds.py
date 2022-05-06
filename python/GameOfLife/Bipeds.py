
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
        This is a function that filter humans in a list against a given gender
        :param value: given gender
        :return: list of human
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
            'boomers': range(1955,1964),
            'genx': range(1965, 1981),
            'genz': range(1997, 2013),
            'gena': range(2010, 2021),
            'zoomers': range(1997,2022),
            'mill': range(1981, 1997)
        }
        gen_range = gen_mapping[gen.lower()]

        if gen.lower() != gen_mapping:
            "Not a supported generation"
            return []
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

