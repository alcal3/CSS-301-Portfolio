#aleks calderon
#4.23.2019
#list reversal - recursive 

wordList = ["Sunday", "Monday", "Tuesday"]

def reverse(words):
    
    return[words[-1]] + reverse(words[:-1]) if words else []

print(reverse(wordList))
                              
