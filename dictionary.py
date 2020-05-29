import json 
from difflib import get_close_matches

Data =json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in Data:
        return Data[word]
    elif word.title() in Data:
        return Data[word]
    elif word.upper() in Data: 
        return Data[word.upper()]
    elif len(get_close_matches(word,Data.keys())) > 0:
        print("Did You mean %s instead" %get_close_matches(word,Data.keys())[0])
        decide=input("Press Y for Yes and N For No ")
        if decide=="y":
            return Data[get_close_matches(word,Data.keys())[0]]
        elif decide =="n":
            return ("Pugger your paw steps on Wrong keys")
        else:
            return("You Heve Enterted Wrong input please just y and n")
    else:
        print("Pugger your paw steps on Wrong keys")

word=input("Enter the word you want to search")
output=translate(word)

if type(output) == list:
    for item in output:
        print(item)
    
else: 
    print(output)
