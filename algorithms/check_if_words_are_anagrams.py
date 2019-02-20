from typing import Dict


def are_anagrams(word1: str, word2: str) -> bool:
    return get_letter_count(word1) == get_letter_count(word2)


def get_letter_count(word: str) -> Dict[str, int]:
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1    
        else:
            letter_count[letter] = 1
    return letter_count


if __name__ == '__main__':
    word1 = "arc"
    word2 = "car"

    print(are_anagrams(word1, word2))
