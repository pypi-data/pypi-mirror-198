PRODUCTION = True
if PRODUCTION:
    from nepalithar.helper import *
else:
    from helper import CasteHelper
import random

class Caste():
    """
    A class for working with caste-related data in Nepal.

    The Caste class provides methods for detecting caste names in input strings,
    generating random caste names, and splitting a full name into a list of names and caste names.

    """

    def __init__(self):
        """
        Constructor for the Caste class, initializes a CasteHelper object.
        """
        self.helper = CasteHelper()

    def detect(self, input_string: str) -> list:
        """
        Detects the position of caste names in the input string.

        Args:
            input_string: A string containing the input text.

        Returns:
            A list of tuples containing the index and caste name of each detected caste in the input string.
        """
        word_list = input_string.strip().split(" ")
        index = [(i, word) for i, word in enumerate(word_list) if self.helper._is_present(word.upper())]
        return index

    def is_caste(self,caste: str) -> bool:
        """
        Checks whether the given string is a valid caste name.

        Args:
            caste: A string representing the caste name.

        Returns:
            A boolean value indicating whether the given string is a valid caste name.
        """

        return self.helper._is_present(caste)

    def get(self, n: int = 1) -> list:
        """
        Generates n random caste names.

        Args:
            n: The number of caste names to generate (default is 1).

        Returns:
            A list of n random caste names.
        """
        return self.helper._get_random_caste(n)

    def get_position(self, string: str) -> list:
        """
        Gets the position of caste names in the given input string.

        Args:
            string: A string containing the input text.

        Returns:
            A list of integers representing the position of caste names in the input string.
        """
        caste_in = self.detect(string)
        caste_in_list = [position for position, _ in caste_in]
        return caste_in_list
    
    def split_name(self, string: str) -> list:
        """
        Splits a full name into a list of names and caste names.

        Args:
            string: A string representing the full name.

        Returns:
            A list of strings representing the individual names and caste names.
        """
        name_bucket = []
        string = string.strip()
        raw_name = string.split(" ")
        caste_index = self.get_position(string)
        total_caste_found = len(caste_index)
        if total_caste_found <= 1:
            name_bucket.append(string)
        elif (total_caste_found > 1):
            previous = 0
            for _, index in enumerate(caste_index):
                if index + 1 < len(raw_name) and self.helper._is_present(raw_name[index]) and self.helper._is_present(raw_name[index + 1]):
                    pass
                else:
                    name_bucket.append(' '.join(raw_name[0 if len(name_bucket) == 0 else previous + 1:index + 1]))
                    previous = index
        return ([name.title() for name in name_bucket])
