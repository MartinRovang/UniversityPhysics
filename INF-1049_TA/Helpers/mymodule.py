def greeting(name):
  print("Hello, " + name)


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}



class person:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def Show_All(self):
        print('Name: %s, Position: %s, Age: %d'%(self.name, self.position, self.age))
