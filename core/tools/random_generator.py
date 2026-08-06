import random
import string


class RandomTool:

    def random_number(self, start: int, end: int):

        return random.randint(start, end)

    def random_choice(self, items):

        return random.choice(items)

    def random_password(self, length=12):

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        return "".join(
            random.choice(characters)
            for _ in range(length)
        )