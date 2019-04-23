
class inventory:
    def __init__(self, x):
        self.x = x
        self.observers = []
    
    def update_observers(self):
        for observer in self.observers:
            observer.update()

    def new_inventory(self, y):
        self.x += y
        self.update_observers()

    def attach(self, *observers):
        for observer in observers:
            self.observers.append(observer)


        

class observer:
    def __init__(self, object):
        self.calls = 0
        self.attached_object = object

    def update(self):
        self.calls += 1
        print('Observer has detected changes to %s'%self.attached_object)
        print('Total calls: %s'%self.calls)
        print('Inventory: %s'%self.attached_object.x)
    
    def get_attachment(self):
        print(self.attached_object.__name__)



i = inventory(10)
c = observer(i)
i.attach(c)

i.new_inventory(60)
i.new_inventory(30)
i.new_inventory(-39)






