class Person:
    def __init__(self, name, gender, age, occupation, birthday, height, hobbies, family):
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.birthday = birthday
        self.height = height,
        self.hobbies = hobbies or []
        self.family = family or {}

    def getRelatives(self):
        family = []
        for i in self.family:
            family.append(self.family[i])
        
        return family

    def getSimilarHobby(self, inputHobby):
        for i in self.hobbies:
            i = i.lower()
            if i == inputHobby:

                print("You Have a Similar Hobby To: " + self.name)
                print("Hobby: " + i)

# john = Person("John", "Male", "18", "Student", "05/08/2000", "5'8", ["Basketball", "Fishing"], {"Dad": "Steve", "Mom": "Daisy"})

# family = john.getRelatives()
# print(family)

# john.getSimilarHobby(input("Enter a Hobby: "))

class Polygon:

    def __init__(self, numOfSides):
        self.numOfSides = numOfSides
        self.sides = []

    def inputSides(self):
        for i in range(0, self.numOfSides):
            side = int(input("Side"+str(i + 1)+" Length= "))
            self.sides.append(side)
        
    def displaySides(self):
        for i in self.sides:
            print("Side" + str(i + 1) + " = " + str(self.sides[i]))



    

    
        

