#22 Дан список с числами. После каждого однозначного числа вставьте еще такое же.
digit = [4324, 1, 252, 35, 6, 2342, 6, 4523, 32, 6, 10]
i: int =0
while i<len(digit):
    if len(str(digit[i]))==1:
        digit.insert(i+1, digit[i])
        i+=2
    else:
        i+=1
print(digit)

#23. Дан список: Найдите сумму элементов этого списка
list1 = [ [11, 12, 13], [14, 15, 16], [17, 17, 19] ]
list2 = [ [21, 22, 23], [24, 25, 26], [27, 27, 29] ]
list3 = [ [31, 32, 33], [34, 35, 36], [37, 37, 39] ]

# Объединим все списки в один
combined_list = list1 + list2 + list3
total_sum = 0

# Итерируем по каждому подсписку и по каждому элементу в них
for sublist in combined_list:
    for element in sublist:
        total_sum += element

print("Сумма элементов всех списков:", total_sum)

#24 Дано число. Проверьте, что у этого числа есть только один делитель, кроме него самого и единицы.
digit_input = int(input("Введите число для проверки"))
if digit_input < 2:
    print("Число должно быть больше 1.")
else:
    divisors = []  # Список для хранения делителей

    # Проверяем делимость на числа от 2 до sqrt(digit_input)
    for i in range(2, int(digit_input**0.5) + 1):
        if digit_input % i == 0:
            divisors.append(i)
            # Если нашли более одного делителя, выходим из цикла
            if len(divisors) > 1:
                break

    # Проверяем, добавился ли делитель, и нет ли у числа других делителей
    if len(divisors) == 1:
        # Проверяем, есть ли соответствующий делитель
        corresponding_divisor = digit_input // divisors[0]
        if corresponding_divisor != divisors[0]:  # Убедимся, что делитель не одинаковый
            print(f"{digit_input} имеет только один делитель: {divisors[0]}")
        else:
            print(f"{digit_input} является простым числом.")
    else:
        print(f"{digit_input} имеет более одного делителя.")

#25 Выведите в консоль все числа в промежутке от 10 до 1000, у которых предпоследняя цифра четная.
for number in range(10, 1001):
    # Получаем предпоследнюю цифру
    penultimate_digit = (number // 10) % 10
    # Проверяем, является ли она четной
    if penultimate_digit % 2 == 0:
        print(number)
