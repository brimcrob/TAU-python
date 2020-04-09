class Person:
    def __init__(self,firstname, lastname, health, status):
        "intialize attributes to be used in/available for all\
        class methods in this class and for the class objects created\
        by this class"

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "all people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))


    def emote(self):
         "random emotions for each person"
         emotion = random.randrange(1,3)
         if emotion == 1:
             print("{} is feeling happy today".format(self.firstname))
         elif emotion == 2:
             print("{} is feeling sad today".format(self.firstname))


    def status_change(self):
        "Persons health dependent on score"
        if self.health == 100:
            print("{} is totally healty!".format(self.firstname))
        elif self.health >= 76:
            print("{} is not feeling great".format(self.firstname))
        elif self.health >=51:
            print("{} is feeling unwell".format(self.firstname))
        elif self.health >= 40:
            print("{} should go to the doctor!".format(self.firstname))
        else:
            print("{} is unconious. ".format(self.firstname))

Maria = Person("Maria","Black", 100, status=True)
Rey = Person("Rey", "Jones", 88, status=False )
Lee = Person("Lee","Smith", 72, status=True)

print("{} is my friend? {} ".format(Maria.firstname,Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()


Maria.status_change()
Rey.status_change()
Lee.status_change()




