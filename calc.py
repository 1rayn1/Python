from sympy import symbols, Eq, solve
import re

def evaluate_expression(expression):
    expression = expression.replace('x', '*').replace('X', '*').replace('÷', '/').replace('^', '**')
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error: {e}"

def solve_equation(equation):
    x = symbols('x')
    equation = equation.replace('X', 'x').replace('÷', '/').replace('^', '**')
    try:
        left, right = equation.split('=')
        left = re.sub(r'(\d)(x)', r'\1*x', left)
        right = re.sub(r'(\d)(x)', r'\1*x', right)
        eq = Eq(eval(left, {"x": x}), eval(right, {"x": x}))
        solution = solve(eq, x)
        return solution if solution else "No solution found"
    except Exception as e:
        return f"Error: {e}"


while True:
    expr = input("Enter expression or equation (Enter nothing to exit): ")
    if not expr:
        break
    if '=' in expr:
        answer = solve_equation(expr)
        print(f"Solution for x: {answer}")
    else:
        answer = evaluate_expression(expr)
        print(f"Result: {answer}")