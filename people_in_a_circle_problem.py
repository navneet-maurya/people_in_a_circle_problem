import sys

class PeopleInACircleProblem(object):
    # This program will find the last alive person if 0th index person from [people_stack] kills
    # 1st index people, then sword get passed to the 3rd index person and so on till last person standing.

    #  This is is the class variable initializer, which will allow class to initialize class level variables.
    #  params: Integer [number_of_people]
    def __init__(self, number_of_people):
        self.number_of_people = number_of_people

    def last_person_standing(self):
        """Return the last survival with n people."""
        # After each round, the gap between the person who survived doubles. So after one round,
        # the survivors are every 2nd person; after two rounds, every 4th person, after three rounds, every 8th person, and so on.
        # When there are an even number of people, the first person remains the first survivor in the next round.
        # But when there are an odd number of people, the third person becomes the first survivor in the next round.
        # So to solve this problem, we don't need to remember all the survivors,
        # we only need to remember the first survivor, the gap between survivors, and the total number of survivors.


        first = 0
        gap = 1
        while self.number_of_people > 1:
            gap *= 2
            self.number_of_people, odd = divmod(self.number_of_people, 2)
            if odd:
                first += gap
        return first


if __name__ == "__main__":
    number_of_people = sys.argv[1]
    people = PeopleInACircleProblem(int(number_of_people))
    print(f"Index of a Last Person Alive: {people.last_person_standing()}")