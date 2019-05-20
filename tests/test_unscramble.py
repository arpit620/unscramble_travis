import pytest
from unscramble import Unscramble
from collections import defaultdict
# import sys
import sys,os
sys.path.append(os.path.realpath('..'))

print("Sys Path = " , sys.path)

@pytest.fixture
def unscramble():
    words = Unscramble("Search")
    return words


def test_load_dictionary(unscramble):
    # words = Unscramble("Search")
    dictionary = unscramble._load_dictionary(path = "../data/")
    assert isinstance(dictionary, list), "Dictionary not a list"
    assert len(dictionary) > 1, "Dictionary is less than 100"


def test_get_word_lenghts(unscramble):
    # words = Unscramble("Search")
    word_lengths = unscramble._get_word_lengths(upto=4)
    assert word_lengths == [6, 5, 4], "Word length not matching"


def test_create_permutations():
    words = Unscramble("Search")
    word_permutations = words._create_permutations(upto=4)
    assert isinstance(word_permutations, list), "Not a list"
    assert len(word_permutations) > 1700

    total = words._total_permutations(word_permutations)
    assert total == 1800, "Permutations not 1800"


def test_get_defaultdict():
    words = Unscramble("Hello")
    sample_words = ["Hello", "World", "This", "is", "random", "string"]
    dictionary = words._get_defaultdict(sample_words)
    assert isinstance(dictionary, defaultdict), "Defaultdict not returned"


def test_find_words():
    words = Unscramble("Hello")
    dict_words = words.find_words(path = "../data/")
    assert len(dict_words[5]) == 1, "Length not 1"
    assert len(dict_words[4]) == 3, "Length not 3"
    assert len(dict_words[3]) == 0, "Length more than 0"
    assert len(dict_words[6]) == 0, "Length more than 0"
