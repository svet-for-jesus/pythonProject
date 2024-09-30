#26 Сформируйте с помощью циклов следующий список
# [
# ['x', 'x', 'x'],
# ['x', 'x', 'x'],
# ['x', 'x', 'x'],
# ]

list=["x", "x", "x"]
my_list=[]
for element in range(len(list)):
    my_list.append(list)
print(my_list)
print()
for row in my_list:
    for elem in row:
           # print(newlist)
           print(elem, end=' ')
    print()
#27 Дан текст со знаками препинаний. Получите список предложений этого текста.
text = "sep=None — строка-разделитель, при помощи которой требуется разбить исходную строку. Может содержать как один, так и несколько символов. Если не указан, то используется специальный алгоритм разбиения, для которого разделителем считается последовательность пробельных символов."
print(text.rsplit(sep=".", maxsplit=-1) )

#28  Дан произвольный двухмерный список:
#[
#[11, 12, 13, 14, 15],
#[21, 22, 23, 24, 25],
#[31, 32, 33, 34, 35],
#[41, 42, 43, 44, 45],
#[51, 52, 53, 54, 55]
#]
#Получите список элементов его главной диагонали: [ 11, 22, 33, 44, 55 ]

list = [ [11, 12, 13, 14, 15], [21, 22, 23, 24, 25], [31, 32, 33, 34, 35], [41, 42, 43, 44, 45], [51, 52, 53, 54, 55] ]
newlist=[]
i=0
for sublist in list:
    for element in sublist:
        newlist.append(sublist[i])
        i+=1
        break
print(newlist)

# 29. Спросите у пользователя целое число. В ответ выведите разложение этого числа на простые множители.
#digit = int(input("Введите целое число для разложения его на простые множители "))
#result=[]
#for i in range(2, digit-1):
#    while digit %i ==0:
#        digit = digit/i
#        i+=1
#    result.append(digit)
# 21print(result)

 # 29. Спросите у пользователя целое число. В ответ выведите разложение этого числа на простые множители.

def check_digit(digit_input):
    while digit_input % 2 ==0:
        result.append(digit_input)
        digit_input //= 2
    # digit_input должно быть нечетным, поэтому начинаем с 3 и пробуем все нечетные числа
    for i in range(3, int(digit_input**0.5) + 1, 2):
        while digit_input % i ==0:
            result.append(digit_input)
            digit_input //=i
    if digit_input>2:
        result.append(digit_input)
        return result

digit = int(input("Введите целое число: "))
result=[]
if digit<=0:
        print("Введенное число меньше или равно нулю. Программа завершает работу")
        exit()
else:
        fin_result = check_digit(digit)
print("Разложение на простые множители:", fin_result)