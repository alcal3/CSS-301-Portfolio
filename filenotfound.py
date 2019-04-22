#aleks calderon
#4.16.2019
#file not found error replaced with print statement to allow program to run

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:
    print("File not found.")
