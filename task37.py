# Преобразователь валют: Создайте приложение, которое конвертирует сумму из одной валюты в другую по заранее заданным курсам.
import tkinter as tk

root=tk.Tk()
root.title("Конвертор валют GUI") # название программы
label1=tk.Label(root, text='Введите сумму и единицу измерения валюты: ')
label2=tk.Label(root, text='Введите единицу конвертации валюты: ')
label3=tk.Label(root, text='Результат конвертации: ')
result=tk.Label(root, bg='#ffaaaa', text=' ', font=('Comic Sans MS', 24, 'bold'), )
entryСurrency=tk.Entry(root) # создание поля ввода текста

# курс валют
exchange ={
   "USD": {"USD": 1.18, "RUB": 86.00},
   "EUR": {"EUR": 0.85, "RUB": 73.00},
   "RUB": {"USD": 0.014, "EUR": 0.012}
          }
#for dict in range(len(exchange)):
 #   for element in range(len(dict)):
 #       print(exchange[dict][element])

def clear(): entryСurrency.delete(0,tk.END)
def on_button_click(value): entryСurrency.insert(tk.END,value)
def on_button_clickConv(value):
    entryСurrency.insert(tk.END,value)
    valute = entryСurrency.get()
    if valute.endswith(' RUB в RUB = ') or valute.endswith(' EUR в EUR = ') or valute.endswith(' USD в USD = '):
        resultConversation =valute.replace(" RUB в RUB = ", '')
        resultConversation =valute.replace(" EUR в EUR = ", '')
        resultConversation = valute.replace(" USD в USD = ", '')
        entryСurrency.insert(tk.END,resultConversation)

    elif valute.endswith(' RUB в USD = '):
        deleteValute =valute.replace(" RUB в USD = ", '')
        resultConversation=float(deleteValute)*float(exchange.get("RUB").get("USD"))
        entryСurrency.insert(tk.END,resultConversation)

    elif valute.endswith(' RUB в EUR = '):
        deleteValute =valute.replace(" RUB в EUR = ", '')
        resultConversation=float(deleteValute)*float(exchange.get("RUB").get("EUR"))
        entryСurrency.insert(tk.END,resultConversation)

    elif valute.endswith(' EUR в RUB = '):
        deleteValute =valute.replace(" EUR в RUB = ", '')
        resultConversation=float(deleteValute)*float(exchange.get("EUR").get("RUB"))
        entryСurrency.insert(tk.END,resultConversation)
      
    elif valute.endswith(' EUR в USD = '):
        deleteValute =valute.replace(" EUR в USD = ", '')
        resultConversation=float(deleteValute)*float(exchange.get("RUB").get("EUR"))/float(exchange.get("RUB").get("USD"))
        entryСurrency.insert(tk.END,resultConversation)

    elif valute.endswith(' USD в EUR = '):
        deleteValute =valute.replace(" USD в EUR = ", '')
        resultConversation=float(deleteValute)*float(exchange.get("RUB").get("USD"))/float(exchange.get("RUB").get("EUR"))
        entryСurrency.insert(tk.END,resultConversation)


buttonRUB = tk.Button(root, text="Рубли", command=lambda: on_button_click(" RUB "), width=8, height=2)
buttonEUR = tk.Button(root, text="Евро", command=lambda: on_button_click(" EUR "), width=8, height=2)
buttonUSD = tk.Button(root, text="Доллар", command=lambda: on_button_click(" USD "), width=8, height=2)
buttonRUBConv = tk.Button(root, text="Рубли", command=lambda: on_button_clickConv("в RUB = "), width=8, height=2)
buttonEURConv = tk.Button(root, text="Евро", command=lambda: on_button_clickConv("в EUR = "), width=8, height=2)
buttonUSDConv = tk.Button(root, text="Доллар", command=lambda: on_button_clickConv("в USD = "), width=8, height=2)
buttonClear =tk.Button(root, text="Очистить", command=clear, width=8, height=2)

finEntry=entryСurrency.get()
# currency = eval(fin)

entryСurrency.grid(row=0, column=0, columnspan=3 ) # размещение поля ввода текста в GUI приложение
label1.grid(row=1, column=0, columnspan=3) # Текст: Введите сумму и единицу измерения валюты:
buttonRUB.grid(row=2, column=0)
buttonEUR.grid(row=2, column=1)
buttonUSD.grid(row=2, column=2)


label2.grid(row=3, column=0, columnspan=3) # текст: Введите единицу конвертации валюты:
buttonRUBConv.grid(row=4, column=0)
buttonEURConv.grid(row=4, column=1)
buttonUSDConv.grid(row=4, column=2)

label3.grid(row=5, column=0, columnspan=3) # текст: Результат конвертации валюты
result.grid(row=6, column=0, columnspan=2)
buttonClear.grid(row=6, column=2) # Кнопка очистить
root.mainloop()