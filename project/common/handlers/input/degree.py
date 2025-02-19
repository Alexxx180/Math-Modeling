"""
print("If the polynomial of the denominator of the system's characteristic equation (transfer function is given as: ")
print("a0*s^n + a1*s^(n-1) + ... + a(n-1)*s + an")
print("Enter the degree of the denominator polynomial")

degree = int(input('Degree: '))
coefficients = []
for x in range (0, degree+1):
    coefficient = int(input(str('Enter coefficient '+ 'a' + str(x) + ": ")))
    coefficients.append(int(coefficient))
print(coefficients)
print("To be stable, all of the system's denominator polynomial coefficients must be greater than zero")
"""
