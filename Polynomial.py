import copy
from Monomial import Monomial


class Polynomial(object):

    monomials = []  # type: [Monomial]

    def __init__(self, monomials):
        self.monomials = copy.deepcopy(monomials)
        self.sort()

    def degree(self):
        return self.monomials[0].power

    def eval(self, value):
        sum = 0
        for mono in self.monomials:
            sum += mono.eval(value)
        return sum

    def print_eval(self, value):
        s = self.pretty_print().replace('x', '('+str(value)+')')
        s += ' == ' + str(self.eval(value))
        return s

    def add(self, other):
        if isinstance(other, Polynomial):
            self.monomials.append(other.monomials)
        elif isinstance(other, Monomial):
            self.monomials.append(other)
        elif isinstance(other, float) or isinstance(other, int):
            self.monomials.append(Monomial(other, 0))
        self.sort()

    def __add__(self, other):
        poly = None
        if type(other) is Polynomial:
            poly = Polynomial(self.monomials + other.monomials)
        elif isinstance(other, Monomial):
            poly = Polynomial(self.monomials + [other])
        elif type(other) is float or type(other) is int:
            poly = Polynomial(self.monomials + [Monomial(other, 0)])
        poly.reduce()
        return poly

    def sub(self, other):
        if isinstance(other, Polynomial):
            self.monomials.append(other.monomials)
        elif isinstance(other, Monomial):
            self.monomials.append(other)
        elif isinstance(other, float) or isinstance(other, int):
            self.monomials.append(Monomial(other, 0))
        self.sort()

    def __sub__(self, other):
        poly = None
        if type(other) is Polynomial:
            poly = Polynomial(self.monomials + [-mon for mon in other.monomials])
        elif type(other) is Monomial:
            poly = Polynomial(self.monomials + [-other])
        elif type(other) is float or type(other) is int:
            poly = Polynomial(self.monomials + [-Monomial(other, 0)])
        poly.reduce()
        return poly

    def mul(self, other):
        self *= other
        self.sort()

    def __mul__(self, other):
        poly = None
        if type(other) is Polynomial:
            new = []
            for s in self.monomials:
                for o in other.monomials:
                    new.append(s * o)
            poly = Polynomial(new)
        elif type(other) is Monomial:
            poly = Polynomial([mono * other for mono in self.monomials])
        elif type(other) is float or type(other) is int:
            poly = Polynomial([mono * other for mono in self.monomials])
        poly.reduce()
        return poly

    def div(self, other):
        self /= other

    def __truediv__(self, other):
        return self.__divmod__(other)[0]

    def __mod__(self, other):
        return self.__divmod__(other)[1]

    def __divmod__(self, other):
        poly = None
        rem = 0
        if type(other) is Polynomial:
            out = copy.deepcopy(self.monomials)
            normalizer = other.monomials[0].coeff
            for i in range(self.degree() + 1 - other.degree()):
                out[i].coeff /= normalizer
                coeff = out[i].coeff
                if coeff != 0:
                    for j in range(1, other.degree() + 1):
                        out[i + j].coeff += -other.monomials[j].coeff * coeff
            separator = -other.degree()
            for mono in out:
                mono.power -= 1
            poly = Polynomial(out[:separator])
            rem = out[len(out)-1].coeff
        elif type(other) is Monomial:
            poly = Polynomial([mono / other for mono in self.monomials])
        elif type(other) is float or type(other) is int:
            poly = Polynomial([mono / other for mono in self.monomials])
        poly.reduce()
        return poly, rem

    def derivative(self):
        mono = []
        for i, mon in enumerate(self.monomials):
            mono[i] = Monomial(mon.coeff * mon.power, mon.power - 1)
        return Polynomial(mono)

    def differentiate(self):
        for mono in self.monomials:
            mono.coeff *= mono.power
            mono.power -= 1

    def negate(self):
        for i, mono in enumerate(self.monomials):
            self.monomials[i] = -self.monomials[i]

    def __neg__(self):
        mono = [-mon for mon in self.monomials]
        return Polynomial(mono)

    def sort(self):
        self.monomials.sort(key=lambda x: x.power, reverse=True)

    def reduce(self):
        for i, mono in enumerate(self.monomials):
            if i != len(self.monomials) - 1:
                if self.monomials[i].power == self.monomials[i+1].power:
                    self.monomials[i].coeff += self.monomials[i+1].coeff
                    self.monomials.remove(self.monomials[i+1])
                    continue
            if mono.coeff == 0:
                self.monomials.remove(mono)

    def pretty_print(self):
        s = ""
        for i, mono in enumerate(self.monomials):
            if i != 0:
                s += " " + mono.pretty_print()
            else:
                s += mono.pretty_print()
        if s.startswith('+'):
            s = s[1:]
        return s

    def __str__(self):
        s = ""
        for mono in self.monomials:
            s += " " + str(mono)
        return s
