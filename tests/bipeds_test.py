import unittest

from GameOfLife import Bipeds

BOB = Bipeds.Human("Bob", 1980, "man")
CATH = Bipeds.Human("Cath", 1990, "woman")
ZACH = Bipeds.Human("Zach", 1960, "man")
ALICE = Bipeds.Human("Alice", 2010, "woman")

POPULATION = [
    BOB,
    CATH,
    ZACH,
    ALICE,
]


class Test_Human(unittest.TestCase):
    def test_sorting(self):
        """
        Can the test sort by names Humans in a list.
        """
        expected_result = list(POPULATION)
        expected_result.sort(key=lambda x: x.name)
        list_of_humans = list(POPULATION)
        list_of_humans.sort()
        self.assertEqual(list_of_humans, expected_result)

    def test_equality(self):
        """
        Can we compare humans to determine if they are the same by there data alone.
        """
        self.assertTrue(Bipeds.Human("Cath", 1990, "woman") == Bipeds.Human("Cath", 1990, "woman"))
        self.assertTrue(Bipeds.Human("Cath", 1990, "woman") != Bipeds.Human("Henry", 1330, "man"))


class Test_Population(unittest.TestCase):
    def test_filter_gender(self):
        """
        Can you filter the population by gender.
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
        Can you filter a population by it's generation.
        """
        population = Bipeds.Population(POPULATION)
        expected_result = {
            'genx': [BOB],  # 1965-1980
            'zoomers': [ALICE],  # 1997-2022
            'boomers': [ZACH],  # 1955-1964
            'mill': [CATH],  # 1981-1996
        }

        x = 0
        for gen, gen_expected_result in expected_result.items():
            with self.subTest(i=x):
                self.assertEqual(population.filter_generation(gen), gen_expected_result,
                                 msg="This gen: {}, fails to sort properly.".format(gen))
            x += 1

    def test_sort(self):
        """
        Can you sort a population by name and age. We are testing mostly that the custom logic for sort is made here.
        We are expecting the method name to be sort and it will act differently if the class Population.sort_method is
        set to age or name.
        """
        population = Bipeds.Population(POPULATION)
        holder = [(pop.name, pop) for pop in population.pop_list]
        holder.sort(key=lambda x: x[0])
        with self.subTest(i=0):
            population.sort_method = 'name'
            correct_answer = [person for _, person in holder]
            self.assertEqual(correct_answer, population.sort(),
                             msg="Sort method of the Human class doesn't support sorting by name.")
        holder = [(pop.birthday, pop) for pop in population.pop_list]
        population.sort_method = "age"
        with self.subTest(i=1):
            holder.sort(key=lambda x: x[0])
            correct_answer = [person for _, person in holder]
            self.assertEqual(correct_answer, population.sort(),
                             msg="Sort method of the Human class doesn't support sorting by age.")
