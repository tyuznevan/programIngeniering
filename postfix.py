def evaluate_expression(expr):
    """Вычисляет математическое выражение, используя два стека."""
    numbers = []
    operators = []
    i = 0
    n = len(expr)

    while i < n:
        if expr[i] == ' ':
            i += 1
            continue
error
        # Если цифра или точка (вещественное число)
        if expr[i].isdigit() or expr[i] == '.':
            num = ''
            while i < n and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            numbers.append(float(num) if '.' in num else int(num))

        # Если оператор
        elif expr[i] in '+-*/^':
            # Обрабатываем операторы с учётом приоритета
            while (operators and operators[-1] != '(' and
                precedence(operators[-1]) >= precedence(expr[i])):
                apply_operator(numbers, operators.pop())
            operators.append(expr[i])
            i += 1

        # Если открывающая скобка
        elif expr[i] == '(':
            operators.append(expr[i])
            i += 1

        # Если закрывающая скобка
        elif expr[i] == ')':
            while operators[-1] != '(':
                apply_operator(numbers, operators.pop())
            operators.pop()  # Удаляем '('
            i += 1

        else:
            raise ValueError(f"Неизвестный символ: {expr[i]}")

    # Обрабатываем оставшиеся операторы
    while operators:
        apply_operator(numbers, operators.pop())

    return numbers[0]

def precedence(op):
    """Возвращает приоритет оператора."""
    if op in '+-':
        return 1
    elif op in '*/':
        return 2
    elif op == '^':
        return 3
    return 0

def apply_operator(numbers, op):
    """Применяет оператор к двум верхним числам в стеке."""
    b = numbers.pop()
    a = numbers.pop()
    if op == '+':
        numbers.append(a + b)
    elif op == '-':
        numbers.append(a - b)
    elif op == '*':
        numbers.append(a * b)
    elif op == '/':
        numbers.append(a / b)
    elif op == '^':
        numbers.append(a ** b)

# Пример использования
expr = "3 + 4 * (2 - 1)"
result = evaluate_expression(expr)
print(f"Результат: {result}")  # Вывод: 7.0