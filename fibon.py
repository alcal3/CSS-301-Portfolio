#aleks calderon
#4.23.2019
#recursive function to computer first 100 values in Fibonacci

f = open("fibSequence.txt", "w")

def F(n):
    if n<= 1:
        return(n)
    else:
        return (F(n-1)+F(n-2))

for x in range(10):
    i = F(x)
    f.write(str(i))
    f.write("\n")

f.close
    
    
