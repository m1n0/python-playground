import string
import random


class NameGenerator:
    """Name Generator class"""

    input_str = "What letter do you want? Enter 'vowel' for vowels, 'consonant' for consonants, " \
                "'letter' for any letter: "
    vowels = 'aeiouy'
    consonants = 'bcdfghjklmnpqrstvwxz'

    @staticmethod
    def generate_names(n_names: int = 1, length: int = 3):
        """Generates names of desired length and composition"""
        user_input = [input(NameGenerator.input_str) for i in range(length)]

        names = []
        for i in range(n_names):
            name = ''
            for i in range(length):
                if user_input[i] == 'vowel':
                    name += random.choice(NameGenerator.vowels)
                elif user_input[i] == 'consonant':
                    name += random.choice(NameGenerator.consonants)
                elif user_input[i] == 'letter':
                    name += random.choice(string.ascii_lowercase)
                else:
                    name += user_input[i]
            names.append(name)

        return names

if __name__ == "__main__":
    print(NameGenerator.generate_names(int(input('Enter desired length:'))))