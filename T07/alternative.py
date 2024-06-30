
#File alternative.py for Practical Task 1 on T07
#Function for read string and convert alternate lower / upper case character

def alternate_chr(words):
    convertedChar = ""
    #  converting every character into upper/lower case accordingly
    for i in range((len(words))):
        #Odd number upper case, Even number lower case
        if i % 2 == 0:
            convertedChar += (words[i].upper())
        else:
            convertedChar += (words[i].lower())
    
    return convertedChar

#Function for read string and convert alternate lower / upper case word

def alternate_words(sentence):
    convertedWords = ""
    convertedWordsList = sentence.split(" ")
    #  converting every word into upper/lower case accordingly
    for i in range((len(convertedWordsList))):
        #Odd number lower case, Even number upper case
        if i % 2 == 0:
            convertedWordsList[i] = (convertedWordsList[i].lower())

        else:
            convertedWordsList[i] = (convertedWordsList[i].upper())

        
        convertedWords = " ".join(convertedWordsList)    
    return convertedWords

#First Part test for the alternative character (Lower case / Upper case)change 
firstTest = "Hello World"
print("First test is converting characters!")
print(f"Original: {firstTest}")
print(f"Alternative: {alternate_chr(firstTest)}")
#Second Part test for the alternatvie words (Lower case / Upper case)change 
secondTest = "I am learning to code"
print("Second test is converting words!")
print(f"Original: {secondTest}")
print(f"Alternative: {alternate_words(secondTest)}")