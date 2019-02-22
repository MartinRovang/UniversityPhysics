#%%


class A:
    def __init__(self):
        self.a = 5
    




class B(A):

    def __init__(self):
        super().__init__()
        self.b = a


a = B()
print(a.a)