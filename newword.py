#aleks calderon
#4.22.2019
#counts the letters within a word each time it appears
word = "efuienefe"

#new_word is dictonary but is currently empty
new_word = {}
for x in word:
    #if the letter is in the word once it will equal 1
    if x not in new_word:
        new_word[x] = 1
    else:
        #if the word is in there more than once it will equal the amount it appears in the word
        new_word[x] += 1
print(new_word)
