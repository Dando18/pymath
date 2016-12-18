import Polynomial


class Monomial(object):

    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power

    def degree(self):
        return self.power

    def eval(self, value):
        return self.coeff * (value ** self.power)

    def print_eval(self, value):
        s = self.pretty_print().replace('x', '('+str(value)+')')
        s += ' == ' + str(self.eval(value))
        return s

    def add(self, other):
        self += other

    def __add__(self, other):
        if type(other) is Monomial:
            if self.power == other.power:
                return Monomial(self.coeff + other.coeff, self.power)
            else:
                return Polynomial([self, other])
        elif type(other) is float or type(other) is int:
            return Polynomial([self, Monomial(other, 0)])

    def sub(self, other):
        self -= other

    def __sub__(self, other):
        if type(other) is Monomial:
            if self.power == other.power:
                return Monomial(self.coeff - other.coeff, self.power)
            else:
                return Polynomial([self, -other])
        elif type(other) is float or type(other) is int:
            return Polynomial([self, Monomial(-other, 0)])

    def mul(self, other):
        self *= other

    def __mul__(self, other):
        if type(other) is Monomial:
            return Monomial(self.coeff * other.coeff, self.power + other.power)
        elif type(other) is float or type(other) is int:
            return Monomial(self.coeff * other, self.power)

    def div(self, other):
        self /= other

    def __truediv__(self, other):
        if type(other) is Monomial:
            return Monomial(self.coeff / other.coeff, self.power - other.power)
        elif type(other) is float or type(other) is int:
            return Monomial(self.coeff / other, self.power)

    def pow(self, power):
        self **= power

    def __pow__(self, power, modulo=None):
        if type(power) is float or type(power) is int:
            return Monomial(self.coeff ** power, self.power * power)

    def negate(self):
        self.coeff *= -1

    def __neg__(self):
        return Monomial(-self.coeff, self.power)

    @staticmethod
    def to_superscript(string):
        string = string.replace('0', '⁰')
        string = string.replace('1', '¹')
        string = string.replace('2', '²')
        string = string.replace('3', '³')
        string = string.replace('4', '⁴')
        string = string.replace('5', '⁵')
        string = string.replace('6', '⁶')
        string = string.replace('7', '⁷')
        string = string.replace('8', '⁸')
        string = string.replace('9', '⁹')
        return string

    def pretty_print(self):
        s = ""
        if self.coeff < 0:
            s += "- "
        else:
            s += "+ "
        if abs(self.coeff) != 1 or self.power == 0:
            s += str(abs(self.coeff))
        if self.power != 0:
            s += "x"
            if self.power != 1:
                s += Monomial.to_superscript(str(self.power))
        return s

    def __str__(self):
        return ("- " if self.coeff < 0 else "+ ") + str(abs(self.coeff)) + "x^" + str(self.power)
