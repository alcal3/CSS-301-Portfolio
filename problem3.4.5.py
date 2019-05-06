#aleks calderon
#5.2.2019
#creating a class w/method that prints greeting and students name

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def myfunc(self):
        print("Good morning, " + self.name)

p1 = Student("Aleks", "Communications")
p1.myfunc()

p1.major = "Criminal Justice"
            
print(p1.major)
