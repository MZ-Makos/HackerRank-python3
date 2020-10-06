"""
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign initalAge to age after confirming the argument passed as initailAge is not negative; if a negative argument is passed as initialAge, the constructor should set age to 0 and print 'Age is not valid, setting age to 0.'. In addition, you must write the following instance methods:

- yearPasses() should increase the age instance variable by 1.
- amIOld() should perform the following conditional actions:
    - If age <13 , print You are young..
    - If age>=13 and age <18, print You are a teenager..
    - Otherwise, print You are old..
"""


class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        #age = int(input())
        if initialAge > 0:
            self.age = initialAge
        else:
            print('Age is not valid, setting age to 0.')
            self.age = 0
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 18:
            print("You are old.")
        else:
            print("You are a teenager.")
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input()) #number of cases
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

    