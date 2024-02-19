class person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def talk(self):
        print(f"HEllo. I am {self.name}")
    def vote(self):
        if self.age < 18:
            print("You are not eligible to vote")
        else:
            print(f"You are {self.age} years old. You are aligible to vote")
obj1 = person("Kim", "Male", 21)
obj2 = person("Jackson", "Female", 41)
obj3 = person("Kimutai", "male", 23)
obj1.talk()
obj1.vote()
obj2.talk()
obj2.vote()
obj3.talk()
obj3.vote()