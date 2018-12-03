import numpy as np

class cone:
    def __init__(self, radius, height, slant_height):
        self.radius = radius
        self.height = height
        self.slant_height = slant_height

    def surface_area(self):
        return np.pi*self.radius*(self.slant_height+self.radius)
    def volume(self):
        return (1/3)*np.pi*self.radius**2*self.height




new_cone = cone(5,10,2)



class Second_Derivative:
    def __init__(self,f):
        self.f = f

    def __call__(self,x, h = 0.01):
        return (self.f(x - h) - 2*self.f(x) + self.f(x + h))/h**2
    


f1 = lambda x: np.sin(x)

fdd = Second_Derivative(f1)

print('Partial value',fdd(np.pi/2))


class Polynomial:
    def __init__(self, p):
        self.p = p
    
    def __call__(self, x):
        s = 0
        for key in self.p:
            if key != 0:
                s += int(self.p[key])**int(key)*x
            else:
                s += self.p[key]*x
        return s

    def __add__(self, other):
        result_p = {}

        if len(self.p) > len(other.p):
            result_p = self.p
            for key in other.p:
                result_p[key] += other.p[key]
        else:
            result_p = other.p
            for key in self.p:
                result_p[key] += self.p[key]

        res = Polynomial(result_p)
        res = res._removeZeros()

        # return Polynomial(result_p)
        return res
    

    def __sub__(self, other):
        result_p = {}

        if len(self.p) > len(other.p):
            result_p = other.p
            for key in self.p:
                result_p[key] -= other.p[key]
        else:
            result_p = self.p
            for key in other.p:
                result_p[key] -= other.p[key]
        

        res = Polynomial(result_p)
        res = res._removeZeros()
    

        #return Polynomial(result_p)
        return res

    def __mul__(self, other):
        result_p = {}
        c = self.p
        d = other.p
        if len(self.p) > len(other.p):
            for key in self.p:
                for key2 in self.p:
                    try:
                        result_p[key+key2] += c[key]*d[key2]
                    except:
                        result_p[key+key2] = c[key]*d[key2]
        else:
            for key in other.p:
                for key2 in other.p:
                    try:
                        result_p[key+key2] += c[key]*d[key2]
                    except:
                        result_p[key+key2] = c[key]*d[key2]

        res = Polynomial(result_p)
        res = res._removeZeros()

        #return Polynomial(result_p)
        return res


    def __str__(self):
        s = ''
        for key in self.p:
            if self.p[key] != 0:
                s += ' + %g*x^%d' %(self.p[key], key)
        #fix layout
        s = s.replace('+ -','- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('*1', '')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':
            s = s[3:]
        if s[0:3] == ' - ':
            s = '-' + s[3:]
        if s == '':
            s = '0'
        return s


    def __repr__(self):
        s = self.__str__()
        s = s.replace('^', '**')
        return s

        
    def __eq__(self, other):
        return self.p == other.p 
    
    def __len__(self):
        return max(self.p)


    def differentiate(self):
        result_p = {}
        for key in self.p:
            if key == 0:
                result_p[key] = 0
            else:
                result_p[key-1] = key*self.p[key]
        return Polynomial(result_p)


    def derivate(self):
        dp = Polynomial(self.p)
        dp = dp.differentiate()
        return dp

    def _removeZeros(self):
    
        self.dict = {i: self.dict[i] for i in self.dict if self.dict[i] != 0}

        return(self.dict)


    
        

new = Polynomial({0: 3, 3: 2, 6: 4})
new2 = Polynomial({0: 3, 3: -2, 6: 4})



# print(len(new*new2))
# print(new*new2)
# print(new-new2)
# print(new-new2)

print(new)
print(new.derivate())
# print(new)

f = lambda x: eval(repr(new))
# print(f(5))


print(new(5))






# a.__add__(b) --> a + b

# a * b


