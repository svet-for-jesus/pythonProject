# Нужно вернуть список, который состоит из элементов, общих для этих двух списков
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def returnMatches(a, b):
 matches = []
 for i in a:
  if i in b:
   matches.append(i)
 return matches
print (returnMatches(a, b))

# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 -
# числа, третий - операция, которая должна быть произведена над
# ними. Если третий аргумент +, сложить их; если —, то вычесть; * —
# умножить; / — разделить (первое на второе). В остальных случаях
# вернуть строку "Неизвестная операция".

try:
 arg1 = float(input("Введите число 1: "))
 arg2 = float(input("Введите число 2: "))
 operation = input("Введите тип математической операции (+ сложить, или - вычесть, или * умножить, или / разделить: ")
 def arithmetic(arg1, arg2, operation):
  match operation:
   case "+": result = arg1+arg2
   case "-": result = arg1-arg2
   case "*": result = arg1*arg2
   case "/": result = arg1/arg2
  print(f"Результат математической операции {operation}: ", result)

 arithmetic(arg1, arg2, operation)

except:
 print("Неизвестная операция")