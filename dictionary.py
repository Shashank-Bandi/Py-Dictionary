'''Dictionary program to fetch the meaning of entered word. Matches the wrongly entered word to its greatest accuracy of 60%'''

#importing json to hold the data in key value pairs
import json
import difflib as dl#importing difflib to match the closest word
data = json.load(open('data.json'))#Loading the data from Json to a dictionary
#Function to return the meaning of the entered word
def meaning(x):
    if x in data:
        return data[x]
    else:
        return "No such word Exists"


def search(word):
    if word.upper() in data:#This logic checks if the entered word is an ACRONYM or not
        print()    
        print(meaning(word))
        print()
        

    elif word.title() in data:#This logic checks if the first letter is capital as in proper nouns and returns the meaning
        print()
        print(meaning(word))
        print()    

    elif word.lower() not in data:#This logic is used to get the closest match for the wrongly entered word
        old = word.lower()
        word = dl.get_close_matches(word,data.keys())[0]
        choice = input("Did you mean {} instead of {}?[Y|N]:".format(word,old))
        if choice.lower() =='y':
            print()
            print(meaning(word))
            print()
        elif choice.lower()!='y' and choice.lower()!='n':
            choice1=input("Please Select something from Y and N only:")
            if choice1.lower() =='y':
                print()
                print(meaning(word))
                print()
            else:
                print()
                print(meaning(old))
                print()
        else:
             print()   
             print(meaning(old))
             print()
             
    else:#This will print the meaning if non of the above conditions are met
        print(meaning(word))
        print()
        print()
word=input("Enter a word you want to search:")
search(word)
#The loop will run infinetly based on users decisions
while True:
    option = input("Do you want to search for another word if yes please enter the word if no press q:")
    if option.lower()=='q':
        print("Thanks for using this dictionary:)")
        break
    else:
        word = option
        search(word)
        



    
