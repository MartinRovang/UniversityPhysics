

class Silly:

    def _get_silly(self):
        print("You are getting silly")
        return self._silly
    
    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value 

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly 

    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")





s = Silly()
s.silly = 'funny'
s.silly 

del s.silly



class Silly2:

    @property
    def silly(self):
        print("You are getting silly")
        return self._silly
    
    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value 


    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly 





s = Silly2()
s.silly = 'funny'
s.silly 

del s.silly