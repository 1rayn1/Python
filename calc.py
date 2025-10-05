def evaluate_expression(expression):
    expression = expression.replace('x', '*').replace('X', '*').replace('÷', '/').replace('^', '**')
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error: {e}"

while True:
        expr = input("Enter expression here(Enter nothing to exit): ")
        if not expr:
            break
        answer = evaluate_expression(expr)
        print(f"Result: {answer}")