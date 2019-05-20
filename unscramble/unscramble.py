from itertools import permutations
from tqdm import tqdm
from collections import defaultdict

# from tqdm import tqdm_notebook as tqdm


class Unscramble:
    """To Do
    """

    def __init__(self, word):
        """To Do
        """
        self.word = word.lower()

    def _load_dictionary(self, path = "../data/"):
        """To Do
        """
        fileName = path + "words_alpha.txt"
        # fileName = "../data/words_alpha.txt"
        dictionary = [line.rstrip("\n") for line in open(fileName)]
        return dictionary
        # self.dictionary = ["hello", "world", "hell", "ehll", "ehl"]

    def _get_word_lengths(self, upto):
        """ To Do
        """
        orig_word_len = len(self.word)
        word_lengths = list(reversed(range(orig_word_len + 1)))
        word_lengths = word_lengths[:-upto]
        return word_lengths

    def _create_permutations(self, upto=4, exact_length=None):
        """To Do
        """
        self._all_permutations = []

        # Returns a list of int which specify word lengths
        self.word_lengths = self._get_word_lengths(upto)

        if exact_length is not None:
            self.word_lengths = [exact_length]

        for length in tqdm(self.word_lengths, desc="Generating possible words"):
            possible_words = permutations(self.word, length)
            possible_words = map(lambda x: "".join(x), list(possible_words))
            possible_words = list(possible_words)
            self._all_permutations.append(possible_words)

        possible_words = [
            word for word_list in self._all_permutations for word in word_list
        ]
        possible_words = list(set(possible_words))
        return possible_words

    def _total_permutations(self, possible_words):
        """To Do
        """
        return len(possible_words)

    def _get_defaultdict(self, actual_words):
        """To Do
        """
        dict_words = defaultdict(list)
        for word in actual_words:
            dict_words[len(word)].append(word)

        return dict_words

    def _print_dict(self, actual_words):
        """To Do
        """
        for no_of_char, word_list in sorted(actual_words.items(), reverse=True):
            print("\n---------------------------------------\n")
            print(no_of_char, " letter words: \n")
            print(word_list)

        print("\n---------------------------------------\n")

    def find_words(self, upto=4, exact_length=None):
        """To Do
        """
        dictionary = self._load_dictionary()
        possible_words = self._create_permutations(upto, exact_length)
        actual_words = [
            word
            for word in tqdm(possible_words, desc="Dictionary Lookup")
            if word in dictionary
        ]

        actual_words = self._get_defaultdict(actual_words)
        self._print_dict(actual_words)
        # self.actual_words = get_dictionary(self.actual_words)
        return actual_words
