"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Machine to create unique incrementing serial numbers.
    
    >>> word_finder = WordFinder("simple.txt")
    4 words in file

    >>> word_finder.random() in ["# Words", "engineer", "engineering", "engineership"]
    True

    """

    def __init__(self, file):
        """class constructor"""
        words_file = open(file)
        self.filename = file
        self.words = self.get_words(words_file)
        self.words_count = len(self.words)
        print(f"{len(self.words)} words in file")
    

    def __repr__(self):
        """Representation of class"""
        return f"<WordFinder (file={self.filename}, words={self.words_count})>"


    def get_words(self, words_file):
        """Returns the full list of words from file"""
        return [w.strip() for w in words_file]
    

    def random(self):
        """Returns a random word from self's words"""
        return choice(self.words)



class SpecialWordFinder(WordFinder):
    """Extends WordFinder Class.

    >>> special_word_finder = SpecialWordFinder("simple.txt")
    3 words in file

    >>> special_word_finder.random() in ["engineer", "engineering", "engineership"]
    True

    >>> special_word_finder.random() in ["# Words"]
    False

    """
    def __init__(self, file):
        """subclass constructor"""
        super().__init__(file)
    

    def __repr__(self):
        """Representation of class"""
        return f"<SpecialWordFinder (file={self.filename}, words={self.words_count})>"

    def get_words(self, words_file):
        """Returns the list of words from file without empty lines or comments"""
        return [w.strip() for w in words_file if w.strip() and not w.startswith("#")]
    

    

    

    

