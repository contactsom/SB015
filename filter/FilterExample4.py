'''
letterlist = ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't','M', 'o', 'n', 'd', 'a', 'y']

Requirement : I want to filter this list and get the only vowel
'''

def getVowel(listoflatters):
    listofvowel=['a','e','i','o','u']

    if(listoflatters in listofvowel):
        print("Vowel")

letterlist = ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't','M', 'o', 'n', 'd', 'a', 'y']
vowelList=list(filter(getVowel,letterlist))
print(vowelList)
