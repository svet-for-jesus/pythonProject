import tkinter as tk

root = tk.Tk()
root.title("Конвертер валют GUI")  # название программы

# Текстовые метки
label1 = tk.Label(root, text='Введите сумму и единицу измерения валюты: ')
label2 = tk.Label(root, text='Введите единицу конвертации валюты: ')
label3 = tk.Label(root, text='Результат конвертации: ')
result = tk.Label(root, bg='#ffaaaa', text=' ', font=('Comic Sans MS', 24, 'bold'))
entryCurrency = tk.Entry(root)  # создание поля ввода текста

# Курс валют
exchange = {
    "USD": {"USD": 1.0, "RUB": 86.00, "EUR": 0.85},
    "EUR": {"EUR": 1.0, "RUB": 73.00, "USD": 1.18},
    "RUB": {"RUB": 1.0, "USD": 0.014, "EUR": 0.012}
}

def clear():
    entryCurrency.delete(0, tk.END)
    result.config(text=' ')

def convert_currency():
    valute = entryCurrency.get().strip()
    try:
        amount_str, from_currency = valute.split(' ')
        amount = float(amount_str)
        if from_currency in exchange:
            # Получаем список доступных валют
            available_currencies = list(exchange[from_currency].keys())
            return_text = ""
            for to_currency in available_currencies:
                if to_currency != from_currency:
                    converted_amount = amount * exchange[from_currency][to_currency]
                    return_text += f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}\n"
            result.config(text=return_text)
        else:
            result.config(text='Некорректная валюта.')
    except ValueError:
        result.config(text='Некорректный ввод. Используйте "сумма валюта".')

# Кнопки для ввода валют
buttonRUB = tk.Button(root, text="Рубли", command=lambda: entryCurrency.insert(tk.END, "0 RUB "), width=8, height=2)
buttonEUR = tk.Button(root, text="Евро", command=lambda: entryCurrency.insert(tk.END, "0 EUR "), width=8, height=2)
buttonUSD = tk.Button(root, text="Доллар", command=lambda: entryCurrency.insert(tk.END, "0 USD "), width=8, height=2)
buttonConvert = tk.Button(root, text="Конвертировать", command=convert_currency, width=12, height=2)
buttonClear = tk.Button(root, text="Очистить", command=clear, width=8, height=2)

# Размещение элементов GUI
entryCurrency.grid(row=0, column=0, columnspan=3)
label1.grid(row=1, column=0, columnspan=3)
buttonRUB.grid(row=2, column=0)
buttonEUR.grid(row=2, column=1)
buttonUSD.grid(row=2, column=2)
label2.grid(row=3, column=0, columnspan=3)
buttonConvert.grid(row=4, column=0, columnspan=3)
label3.grid(row=5, column=0, columnspan=3)
result.grid(row=6, column=0, columnspan=3)
buttonClear.grid(row=7, column=0, columnspan=3)

root.mainloop()