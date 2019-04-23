#aleks calderon
#4.23.2019
#recursive function part b
def fac(number):
    if number < 1:
        return 1
    else:
        return number * fac(number - 1)
print(fac(10))
