import unittest

from GameOfLife import Bipeds

BOB = Bipeds.Human("Bob", 1980, "Male")
CATH = Bipeds.Human("Cath", 1990, "Female")
ZACH = Bipeds.Human("Zach", 1960, "Male")
ALICE = Bipeds.Human("Alice", 2010, "Female")

POPULATION = [
    BOB,
    CATH,
    ZACH,
    ALICE,
]


class Test_Population(unittest.TestCase):
    def test_filter_gender(self):
        """

        :return:
        """
        population = Bipeds.Population(POPULATION)
        expected_result = {
            'man': [BOB, ZACH],
            'woman': [CATH, ALICE]
        }
        for gender, people_list in expected_result.items():
            self.assertEqual(population.filter_gender(gender), people_list)

    def test_filter_generation(self):
        """

        :return:
        """
        population = Bipeds.Population(POPULATION)
        expected_result = {
            'genx': [BOB],  # 1965-1980
            'zoomers': [ALICE],  # 1997-2022
            'boomers': [ZACH],  # 1955-1964
            'mill': [CATH],  # 1981-1996
        }

        for gen, expected_result in expected_result.items():
            self.assertEqual(population.filter_generation(gen), expected_result)

    def test_sort_name(self):
        """

        :return:
        """
        population = Bipeds.Population(POPULATION)
        names = [pop.name for pop in population.pop_list]
        names.sort()
        self.assertEqual(names, population.sort_name())
