#aleks calderon
#4.22.2019
#asks user for number. error if user inputs a number higher than 20
number = int(input("Please input a number:"))

if number < 20:
    print("Good job!")
else:
    raise Exception("Error: Number is higher than 20.")
