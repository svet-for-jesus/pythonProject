# Дана строка. Проверьте, что эта строка состоит только из четных цифр

a = [4890, 979868, 97680, 684, 76, 7672, 5351]

def check_even_digits(num):
    # Преобразуем число в строку и проверяем каждую цифру
    for digit in str(num):
        if int(digit) % 2 != 0:  # Если цифра нечетная
            return False
    return True

all_even = True  # Флаг для проверки всех чисел

for number in a:
    if not check_even_digits(number):
        print("Список содержит нечетные цифры. Цикл проверки завершен")
        all_even = False
        break

if all_even:
    print("Список состоит только из четных цифр. Цикл проверки завершен")

print("Конец программы")

