#aleks calderon
#4.16.2019
#dictionary with keys 1-20 and values are cubes of keys

autoDict = {}

for x in range(1, 21):
#    autoDict = {x}
#    for x, a in autoDict():
    autoDict[x] = x ** 2
    print(x, autoDict[x])
    
