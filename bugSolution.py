def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return "Error: Cannot divide by zero when both inputs are zero"
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error_solution(0, 0)
print(result)
result = function_with_uncommon_error_solution(5, 0)
print(result)
result = function_with_uncommon_error_solution(0, 5)
print(result)
result = function_with_uncommon_error_solution(10, 2)
print(result)