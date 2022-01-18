import nltk

try:
    nltk.data.find("corpora/words")
    nltk.data.find("corpora/brown")
except:
    nltk.download("words")
    nltk.download("brown")

from nltk.corpus import brown, words
from nltk.probability import FreqDist
from collections import Counter


class Colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"

    def green(text):
        return Colors.GREEN + text + Colors.ENDC

    def yellow(text):
        return Colors.YELLOW + text + Colors.ENDC

    def red(text):
        return Colors.RED + text + Colors.ENDC

    def blue(text):
        return Colors.BLUE + text + Colors.ENDC


def most_common_letters(wordlist):
    c = Counter()
    for word in wordlist:
        c.update(list(word))
    return c.most_common()


def strongest_words(wordlist, freqdict):
    letter_rankings = dict(most_common_letters(wordlist))
    return sorted(
        wordlist,
        reverse=True,
        key=lambda word: (
            word in freqdict,
            sum(letter_rankings.get(letter, 0) for letter in set(word)),
            freqdict.get(word, -1),
        ),
    )


def getFrequencyDict():
    five_letter_words = [word for word in brown.words() if len(word) == 5]
    freq_dict = dict(FreqDist(five_letter_words).items())
    return freq_dict


def getBestWords(wordbank, freq_dict, print_=False):
    ten_best_words = strongest_words(wordbank, freq_dict)[:10]
    if print_:
        print("\nTRY:", Colors.blue(f"{ten_best_words[0].upper()}\n"))
        print("\tAlts:")
        for i, word in enumerate(ten_best_words[1:-1]):
            print(f"\t{i+1}. {word.upper()}")
    return ten_best_words


def generateWordBank(freq_dict):
    return list(set(word.lower() for word in words.words() if len(word) == 5))


def printGuess(correct_letters, misplaced_letters, wrong_letters):
    for i in range(5):
        if wrong_letters[i] != "-":
            print(Colors.red(wrong_letters[i].upper()), end="")
        elif misplaced_letters[i] != "-":
            print(Colors.yellow(misplaced_letters[i].upper()), end="")
        else:
            print(Colors.green(correct_letters[i].upper()), end="")
    print()


def manualFeedback(k):
    correct_letters = input("Give correctly placed letters. Example: ---S-\t\t").lower()
    if "-" not in correct_letters:
        return correct_letters, None, None
    misplaced_letters = input(
        "Give correct but misplaced letters. Example: --O--\t"
    ).lower()
    wrong_letters = input("Give wrong letters. Example: AR--E\t\t\t").lower()
    return correct_letters, misplaced_letters, wrong_letters


def filterRemainingWords(wordbank, correct_letters, misplaced_letters, wrong_letters):
    revised_wordbank = []
    for word in wordbank:
        none_wrong = all(
            letter not in word
            for letter in wrong_letters
            if letter != "-"
            and letter not in misplaced_letters
            and letter not in correct_letters
        )
        misp_present = all(
            letter in word for letter in misplaced_letters if letter != "-"
        )
        none_misp = all(
            word[i] != letter
            for i, letter in enumerate(misplaced_letters)
            if letter != "-"
        )
        all_correct = all(
            word[i] == letter
            for i, letter in enumerate(correct_letters)
            if letter != "-"
        )
        if none_wrong and misp_present and none_misp and all_correct:
            revised_wordbank.append(word)
    return revised_wordbank


def main():
    freq_dict = getFrequencyDict()
    wordbank = generateWordBank(freq_dict)
    getBestWords(wordbank, freq_dict, print_=True)
    for k in range(6):
        correct_ltrs, misplaced_ltrs, wrong_ltrs = manualFeedback(k)
        if "-" not in correct_ltrs:
            print(Colors.green(correct_ltrs.upper()))
            print(f"Solved in {k+1} tries")
            return
        wordbank = filterRemainingWords(
            wordbank, correct_ltrs, misplaced_ltrs, wrong_ltrs
        )
        printGuess(correct_ltrs, misplaced_ltrs, wrong_ltrs)
        getBestWords(wordbank, freq_dict, print_=True)

    print("I'm sorry I failed you")


if __name__ == "__main__":
    main()
