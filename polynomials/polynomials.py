from numbers import Number
import numpy
from numpy import convolve

class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + tuple(numpy.subtract((0),other.coefficients[common:]))
            

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented
        
    def __rsub__(self, other):
        return Polynomial(tuple(numpy.subtract((0),(self - other).coefficients)))
    
    
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial(tuple(convolve(self.coefficients,other.coefficients)))
            
        elif isinstance(other, Number):
            return Polynomial(tuple(numpy.multiply(self.coefficients, other)))   
        
    def __rmul__(self, other):
        return self*other

    
    def __pow__(self, other):
        if other == 0:
            return 1
        else:
            i = 1
            p0=self
            while i < other:
                p0=p0*self 
                i += 1
            return Polynomial(tuple(p0.coefficients))

    def __call__(self, other):
            val=self.coefficients[0]
            for x in range(1,len(self.coefficients)):
                val = val + self.coefficients[(len(self.coefficients)-x)]*(other**(len(self.coefficients)-x))
                
            return val

