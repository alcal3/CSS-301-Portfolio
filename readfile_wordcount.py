#aleks calderon
#4.23.2019
#reads file and creates dictionary that includes all words. counts how many times a word occurs

textD = {}

f = open("testText.txt", "r")

def buildTextD(words):
    for x in words:
        if x not in textD:
#adds word to dictionary
            textD[x] = 1
        else:
#adds number of time words occur in text
            textD[x] = textD[x] + 1

for line in f:
#splits words by space
    w = line.split()
    buildTextD(w)

print(textD)

f.close()
