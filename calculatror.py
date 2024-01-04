print('это калькулятор')

# Программа калькулятора на Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"

# Ввод чисел от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Ввод операции от пользователя
operation = input("Выберите операцию (+, -, *, /): ")

# Выполнение выбранной операции
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Ошибка: неверная операция"

# Вывод результата
print(f"Результат: {result}")
