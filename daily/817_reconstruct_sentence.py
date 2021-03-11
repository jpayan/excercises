"""
[MEDIUM]
This problem was asked by Microsoft

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible
reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
['bedbath', 'and', 'beyond'].
"""
from typing import List


# Problem with this is python's recursion depth limit (max 990), so for inputs
# bigger than 990, it will fail.
# Recursion level limit can be overridden by
#     import sys
#     sys.setrecursionlimit(new_limit)
# Which is not recommended :)
def reconstruct_sentence(words: List[str], sentence: str) -> List[str] or None:
    reconstruct = []
    reconstruct_sentence_helper(words, sentence, reconstruct)
    if ''.join(reconstruct) == sentence:
        return reconstruct


def reconstruct_sentence_helper(words: List[str], sentence: str,
                                reconstruct: []) -> List[str] or None:
    for i, word in enumerate(words):
        if sentence.startswith(word):
            reconstruct.append(word)
            reconstruct_sentence_helper(words, sentence[len(word):],
                                        reconstruct)
            break


# LeetCode solutions:
# https://leetcode.com/problems/word-break/discuss/43788/4-lines-in-Python
def word_break(words: List[str], sentence: str) -> bool:
    ok = [True]
    for i in range(1, len(sentence) + 1):
        outcomes = []
        for j in range(i):
            ok_segment = ok[j]
            sentence_segment = sentence[j:i]
            outcomes.append(ok_segment and sentence_segment in words)
        ok += any(outcomes),
    return ok[-1]


def word_break_2(words: List[str], sentence: str) -> bool:
    ok = [True]
    max_len = max(map(len, words + ['']))
    words = set(words)
    for i in range(1, len(sentence) + 1):
        outcomes = []
        for j in range(max(0, i - max_len), i):
            outcomes.append(ok[j] and sentence[j:i] in words)
        ok += any(outcomes),
    return ok[-1]


def test(actual_result: List[str] or None, expected_result: List[str] or None):
    error_message = f'{actual_result} != {expected_result}'
    try:
        if isinstance(expected_result, list) and isinstance(expected_result[0],
                                                            list):
            error_message = f'{actual_result} not in {expected_result}'
            assert actual_result in expected_result
        else:
            assert actual_result == expected_result
    except AssertionError:
        raise Exception(error_message)


if __name__ == '__main__':
    # Tests that the sentence can be constructed
    words = ['quick', 'brown', 'the', 'fox']
    sentence = 'thequickbrownfox'
    test(reconstruct_sentence(words, sentence),
         ['the', 'quick', 'brown', 'fox'])

    # Tests that the sentence can be constructed with extra words
    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    sentence = 'bedbathandbeyond'
    test(reconstruct_sentence(words, sentence),
         [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']])

    # Tests that the sentence can not be constructed
    words = ['quick', 'brown', 'the', 'fox']
    sentence = 'shouldreturnnone'
    test(reconstruct_sentence(words, sentence), None)

    # Tests that the sentence can not be constructed when part of the
    # sentence is not in the words
    words = ['should', 'return']
    sentence = 'shouldreturnnone'
    test(reconstruct_sentence(words, sentence), None)

    assert not word_break(words, sentence)
    assert not word_break_2(words, sentence)
    words = ['quick', 'brown', 'the', 'fox']
    sentence = 'thequickbrownfox'
    assert word_break(words, sentence)
    assert word_break_2(words, sentence)

    from timeit import timeit

    print("SHORT INPUT")
    # 0.04855309998674784 s
    print(timeit(lambda: reconstruct_sentence(words, sentence), number=10000))
    # 0.3338475000055041 s
    print(timeit(lambda: word_break(words, sentence), number=10000))
    # 0.1519888000038918 s
    print(timeit(lambda: word_break_2(words, sentence), number=10000))

    from random import choice
    from string import ascii_lowercase

    sentence = ''.join(choice(ascii_lowercase) for i in range(990))
    words = [char for char in sentence]
    print("LONG INPUT")
    # 2.8604491999867605 s
    print(timeit(lambda: reconstruct_sentence(words, sentence), number=1000))
    # 3829.796891799997 s
    print(timeit(lambda: word_break(words, sentence), number=1000))
    # 0.6658393000107026 s
    print(timeit(lambda: word_break_2(words, sentence), number=1000))
