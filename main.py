class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    oPersona1 = Person("Olson", 19)
    print(oPersona1.name)
    print(oPersona1.age)