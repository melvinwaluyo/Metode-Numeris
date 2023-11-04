import sympy as sp
from sympy import exp

# Define a function for Newton-Raphson method
def newtonR(f, x0):
    x = sp.symbols('x')
    df = sp.diff(f, x)
    e = 10**-6
    N = 100
    for i in range(N):
        f_x0 = f.subs(x, x0)
        print("Newton-Raphson | %d   | %f    | %f    " % (i, x0, f_x0))
        if abs(f_x0) < e:
            return x0, i
        df_x0 = df.subs(x, x0)
        if df_x0 == 0:
            print("Zero derivative in Newton-Raphson")
            return None
        x0 = x0 - f_x0 / df_x0
    print("Maximum iteration in Newton-Raphson")
    return x0, i

# Define a function for the Secant method based on Newton-Raphson
def secant(f, x0, x1):
    x = sp.symbols('x')
    e = 10**-6
    N = 100
    for i in range(N):
        f_x0 = f.subs(x, x0)
        f_x1 = f.subs(x, x1)
        print("Secant | %d   | %f    | %f    " % (i, x0, f_x0))
        if abs(f_x1) < e:
            return x1, i
        if abs(f_x0 - f_x1) < e:
            print("Secant method is not converging")
            return None
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2


# Define the symbol 'x'
x = sp.symbols('x')

# Define the function 'f'
f = -0.5*9.8*x**2 + 30*x - 45

# Set the initial guesses for both methods
x0_newton = 2
x0_secant = 2
x1_secant = 3

# Calculate the root using Newton-Raphson
x_root_newton, iteration_newton = newtonR(f, x0_newton)

# Result for Newton-Raphson method
print('Newton-Raphson Result : ', x_root_newton)
print('In %d iterations' % iteration_newton)
print("\n")

# Calculate the root using the Secant method
secant_result = secant(f, x0_secant, x1_secant)
    
# Print the results or a message if Secant method did not converge
if secant_result is not None:
    x_root_secant, iteration_secant = secant_result
    print('Secant Result : ', x_root_secant)
    print('In %d iterations' % iteration_secant)
