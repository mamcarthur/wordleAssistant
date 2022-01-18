# Wordle Assistant

Wordle Assistant solves [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzles, either autonomously or with your help. 

Wordle is a popular game in which a player has six chances to guess a five-letter word. Guesses must be real English words. After each guess, the player receives feedback for each letter: green if it's correct, yellow if a letter appears in the word but is in the wrong spot, and gray if it's completely wrong. 

Wordle Assistant draws from a corpus of over 10,000 five-letter words and uses word frequency data to select a best guess each round. It also tries to use common letters in its guesses, which is effective at cutting down the number of remaining possibilities. However, it always attempts to guess correctly and will never choose an impossible word just to eliminate more letters, which is a strategy of some players.

Because the [official site](https://www.powerlanguage.co.uk/wordle/) only has one puzzle at a time, Wordle Assistant plays on a [site](https://metzger.media/games/wordle-archive/?levels=select) which has archived past daily puzzles. If you would like help solving a puzzle on the official site, or if you only want to use it for hints, you can manually enter your guess in "terminal mode."

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [selenium](https://selenium-python.readthedocs.io/) and [nltk](https://www.nltk.org/).

```bash
pip install selenium
pip install nltk
```
It is possible you will need a newer version of ChromeDriver, which you can download [here](https://chromedriver.chromium.org/downloads).

Clone the repository.

## Usage

To let it solve archived puzzles in a browser, give it the day (between 1 and 212 at the time of writing) as an argument in your terminal. For example, for [Day 22](https://metzger.media/games/wordle-archive/?day=22):
```bash
python3 solveWordle.py 22
```
https://user-images.githubusercontent.com/45470793/149936989-58f282ed-6c87-47b1-8185-1f9655da9c1f.mov

To get help with a game you're playing on your own, use the ```-t``` flag for "terminal mode":
```bash
$ python3 solveWordle.py -t
```
It will give you a recommendation and a list of alternative options. As long as you provide feedback correctly, you can guess any word of your choosing; it doesn't have to be among the recommendations. You can see an example of proper feedback below, where "e" is the only correctly placed letter, "a" is somewhere in the word but misplaced, and "r," "i" and "s" do not appear in the word at all. 
```


TRY: RAISE

	Alts:
	1. ARISE
	2. AROSE
	3. IRATE
	4. ORATE
	5. SNARE
	6. STARE
	7. LEARN
	8. RENAL
Give correctly placed letters. Example: ---S-		----e
Give correct but misplaced letters. Example: --O--	-a---
Give wrong letters. Example: AR--E			r-is-
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
