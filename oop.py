class Person:
    def __init__(self):
        self.age=20
        self.name="Joey"

    def saySomething(self):
        print("Good Morning!")
        print("my name is", self.name)
        print(f"and I am {self.age}")
        print("It is time to go! :)")


p = Person()
p.saySomething()