from Polynomial import Polynomial
from Monomial import Monomial
from LinearInterpolater import LinearInterpolator


# polynomial
mon0 = Monomial(1, 2)
mon1 = Monomial(1, 1)
mon2 = Monomial(-1, 0)

pol0 = Polynomial([mon0, mon1])
pol0.add(mon2)
pol1 = Polynomial([Monomial(1, 2), Monomial(1, 0)])


print(pol0.pretty_print())
print(pol0.print_eval(5))
print(pol0 - pol1)
print(pol1 * pol0)


#linear interpolation
x = list(range(0, 10))
li = LinearInterpolator(x, [i**2 for i in x])

