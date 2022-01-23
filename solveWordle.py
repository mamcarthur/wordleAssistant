from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import sys
import in_terminal as wordle


def inputValidGuess(word):
    action = ActionChains(browser)
    for letter in word:
        action.send_keys(letter)
    action.send_keys(Keys.ENTER)
    action.perform()
    sleep(1)


def scrape_feedback(round_):
    browser.implicitly_wait(10)
    correct = list("-----")
    misplaced = list("-----")
    wrong = list("-----")
    guess = browser.find_element_by_xpath(
        f"/html/body/div[1]/div[1]/div[1]/div[{round_}]"
    )
    for i in range(5):
        tile = guess.find_element_by_xpath(
            f'//*[@id="app"]/div[1]/div[1]/div[{round_}]/div[{i+1}]'
        )
        letterValue = tile.text.lower()
        status = tile.get_attribute("class").split()[-1]
        if status == "correct":
            correct[i] = letterValue
        elif status == "misplaced":
            misplaced[i] = letterValue
        else:
            wrong[i] = letterValue
    return "".join(correct), "".join(misplaced), "".join(wrong)


def main():
    try:
        if sys.argv[1] == "-t":
            wordle.main()
            return
        day = int(sys.argv[1])
    except:
        print("To auto-solve an archived Wordle:    python3 wordleSolver.py [day]")
        print("To manually solve in the terminal:   python3 wordleSolver.py -t")
        exit()
    freq_dict = wordle.getFrequencyDict()
    wordbank = wordle.generateWordBank(freq_dict)
    global browser
    browser = webdriver.Chrome()
    try:
        browser.get(f"https://metzger.media/games/wordle-archive/?day={day}")
        print(browser.title)
        for k in range(6):
            bestwords = wordle.getBestWords(wordbank, freq_dict, print_=False)
            inputValidGuess(bestwords[0])
            sleep(1)
            correct, misplaced, wrong = scrape_feedback(k + 1)
            sleep(1)
            if "-" not in correct:
                print(wordle.Colors.green(correct.upper()))
                print(f"Solved in {k+1} tries")
                return
            wordbank = wordle.filterRemainingWords(wordbank, correct, misplaced, wrong)

    finally:
        sleep(3)
        browser.close()


if __name__ == "__main__":
    main()
