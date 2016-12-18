## pymath

**pymath** is a python mathematics library.



## Examples

* Polynomials and Monomials
```python
mon0 = Monomial(1, 2) 
mon1 = Monomial(1, 1)
mon2 = Monomial(-1, 0)

pol0 = Polynomial([mon0, mon1])
pol0.add(mon2)
pol1 = Polynomial([Monomial(1, 2), Monomial(1, 0)])

print(pol0.pretty_print())  # x² + x - 1
print(pol0.print_eval(5))   # (5)² + (5) - 1 == 29
print(pol0 - pol1)          # + 0x^2 + 1x^1 - 2x^0
print(pol1 * pol0)          # + 1x^4 + 1x^3 + 0x^2 + 1x^1 - 1x^0
```


