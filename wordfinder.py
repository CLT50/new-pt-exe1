"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Finds random words from dictionary.
    
    >>> wf = WordFinder("word.txt")
    7 words read

    >>> wf.random() in ["apple", "orange", "banana", "grapes", "blueberries", "strawberries", "mango"]
    True

    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("specialwords.txt")
    10 words read

    >>> swf.random() in ["apple", "banana", "orange", "mango", "pear", "celery", "asparagus", "lettuce", "spinach", "cabbage"]
    True

    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments/also ignore words that start with special character."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("*")]
    