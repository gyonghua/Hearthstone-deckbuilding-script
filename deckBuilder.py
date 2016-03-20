#! python3
import pyautogui
from os import listdir

files = listdir(r"C:\Users\pandasr\Dropbox\programming\pythonStuff\decklists") #get absolute directory of decklists

for file in files:  #print deck list from directory
    if file.endswith(".txt"):
        print (file[:-4])

chooseDeck = input("what deck do you want to build?")

while not "{}.txt".format(chooseDeck) in files:     #check if user input is correct
    chooseDeck = input("Deck does not exist. Choose again.")

deck = open(r"C:\Users\pandasr\Dropbox\programming\pythonStuff\decklists\{}.txt".format(chooseDeck))

deckList = deck.read().split("\n")

for card in deckList:
    if card == "stalagg":
    #Exceptions for cards that appears on second position
        pyautogui.moveTo(932, 946, duration=0.15)
        pyautogui.click()
        pyautogui.typewrite(str(card))
        pyautogui.press("enter")
        pyautogui.moveTo(600, 355, duration=0.15)
        pyautogui.click()
    elif card.isspace():
        pass
    else:
        pyautogui.moveTo(932, 946, duration=0.15)
        pyautogui.click()
        pyautogui.typewrite(str(card))
        pyautogui.press("enter")
        pyautogui.moveTo(399, 355, duration=0.15)
        pyautogui.click()

close("{}.txt".format(chooseDeck))
