"""
Data types:
1. Fundamental DT:
    1. int
    2. float
    3. boolean
    4. String
    5. complex
2. Non-Fundamental DT:(collection DT)
    1. list
    2. tuple
    3. set
    4. dictionary
"""
x = 10
y = 12e3
print(x, type(x))
print(y, type(y))
c1 = 4 + 5j
c2 = complex(2,-2)
print(c1.real, c1.imag)
print(c1 + c2)
print(c1 * c2)
print(c1 / c2)
print(c1 - c2)