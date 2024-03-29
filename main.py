import json
from difflib import get_close_matches

# Load the JSON data
data = json.load(open("data.json"))

# Define a function to translate a word
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()] 
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
        decide = input("Press 'y' for yes or 'n' for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return "Pugger your paw steps on working keys."
        else:
            return "You have entered wrong input. Please enter just 'y' or 'n'."
    else:
        print("You have entered wrong keys. Try again.")

# Ask user for input and translate the word
word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
