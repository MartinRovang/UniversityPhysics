import pickle


class Fruit():
    def __init__(self, x):
        self.name = x


fruit = Fruit('Apple')



pickle.dump(fruit, file = open('pick.pkl', 'wb'))


# myfruit = pickle.load(file = open('pick.pkl', 'rb'))

