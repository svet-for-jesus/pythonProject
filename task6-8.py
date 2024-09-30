# Времена года/ Написать функцию season, принимающую 1 аргумент — номер
# месяца (от 1 до 12), и возвращающую время года, которому этот
# месяц принадлежит (зима, весна, лето или осень)
from calendar import month
from re import match

number = int(input("Введите номер месяца: "))
try:
 def season (number):
    match number:
        case number if 1<=number <=2 or number == 12:print("Время года зима")
        case number if 3 <= number <= 5:print("Время года весна")
        case number if 6 <= number <= 8: print("Время года лето")
        case number if 9 <= number <= 11: print("Время года осень")
        case number if 0< number or number >12: print("Месяц введен не корректно")

 season (number)
except:
    print("Данные введены не корректно")

    #Пользователь делает вклад в размере a рублей сроком на years лет
# под 10% годовых (каждый год размер его вклада увеличивается на
# 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

vklad = int(input("Введите размер вклада: "))
time_vklad = int(input("Введите срок вклада: "))
time =0;
while time_vklad >=time:
    vklad = round(0.1*vklad+ vklad)
    print(f"Ваш вложения за {time} год составляет {vklad}")
    time+=1
print(f"В конце срока вклада ваши накопления составят {vklad}")

#8. Простые числа
#Написать функцию is_prime, принимающую 1 аргумент — число от 0
#до 1000, и возвращающую True, если оно простое, и False - иначе.
chislo = int(input("Введите число для проверки"))
def is_prime(chislo):
    if chislo % 2==0: print("Это простое число")
    if chislo % 2 > 0: print("Это нечетное число")
is_prime(chislo)