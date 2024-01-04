print('Привет!')

from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    current_date = datetime.now()
    birth_date = datetime(birth_year, birth_month, birth_day)

    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

    return age

# Ввод даты рождения от пользователя
birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите месяц рождения: "))
birth_day = int(input("Введите день рождения: "))

# Вычисление возраста
age = calculate_age(birth_year, birth_month, birth_day)

# Вывод результата
print(f"Ваш возраст: {age} лет")
