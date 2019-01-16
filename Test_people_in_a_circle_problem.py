import unittest
from people_in_a_circle_problem import *

class Test_PeopleInACircleProblem(unittest.TestCase):
    def setUp(self):
        print("Running Test", self._testMethodName)

    def test_for_10_people_last_person_standing_is_4(self):
        person = PeopleInACircleProblem(10)
        self.assertEqual(person.last_person_standing(), 4)

    def test_for_1000_people_last_person_standing_is_976(self):
        person = PeopleInACircleProblem(1000)
        self.assertEqual(person.last_person_standing(), 976)

    def test_for_10_people_last_person_standing_is_not_5(self):
        person = PeopleInACircleProblem(10)
        self.assertNotEqual(person.last_person_standing(), 5)


if __name__ == "__main__":
    unittest.main()