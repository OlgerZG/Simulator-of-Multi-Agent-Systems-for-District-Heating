import sympy as sp
from sympy import sin


class SimpleInputs:
    Step = 1
    
    # Define a symbolic variable 'x'
    x = sp.symbols('x')
    
    # Define Slope as a symbolic expression involving 'x'
    Slope = x
    
    # Use 'sin' from sympy for the Step_sin expression
    Step_sin = 1 + sin(x)