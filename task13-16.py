#13 Перебор букв в словах
#Есть массив со словами, в котором есть хотя бы одно слово. Надо
#найти максимально длинное общее начало каждого слова. Если такого нет — вывести пустую строку. не выполнил!!!!
from sys import prefix

words = ["flower", "flow", "flight"]
def longest_common_prefix(words):
    # Начнем с первого слова как общего префикса
    prefix = words[0]
    print(prefix)
    for word in words[1:]:
        # Сравниваем текущий префикс с каждым словом
        while word[:len(prefix)] != prefix:
            # Если не совпадает, обрезаем префикс
            prefix = prefix[:-1]
            # Если префикс стал пустым, возвращаем пустую строку
            if not prefix:
                return ""

    return prefix

result = longest_common_prefix(words)
print(result)

#14 Дано число. Выведите в консоль первую цифру этого числа
chislo = input("Введите число")
print(chislo[0])

#15 Дана строка. Если в этой строке более одного символа, выведите в консоль предпоследний символ этой строки.
stroka = input("Введите строку")
print(stroka[-2])

#16 Дана некоторая строка: 'abcde'. Получите список ее символов: ['a', 'b', 'c', 'd', 'e']
str = "abcde"
new_str=[]
for i in str: new_str.append(i)
print(new_str)