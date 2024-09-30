# Калькулятор: Создайте простой калькулятор с GUI, который может выполнять базовые арифметические операции
# (сложение, вычитание, умножение, деление).
import tkinter as tk


root = tk.Tk()
root.title("Калькулятор GUI")
label = tk.Label(root, text="Введите числа и действия")
entry=tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4)
label.grid(row=1, column=0, columnspan=4)

def on_button_click(value):
       entry.insert(tk.END, value)

def result():
 try:
    res = entry.get()
    entry.delete(0, 111)
    result=eval(res)
    entry.insert(0,result)
 except Exception as e:
    entry.delete(0, tk.END)
    entry.insert(0, "Ошибка")  # Если произошла ошибка, выводим сообщение
def clear(): entry.delete(0,tk.End)
# Кнопки
button0 = tk.Button(root, text="0", command=lambda: on_button_click("0"), width=4, height=2)
button1 = tk.Button(root, text="1", command=lambda: on_button_click("1"), width=4, height=2)
button2 = tk.Button(root, text="2", command=lambda: on_button_click("2"), width=4, height=2)
button3 = tk.Button(root, text="3", command=lambda: on_button_click("3"), width=4, height=2)
button4 = tk.Button(root, text="4", command=lambda: on_button_click("4"), width=4, height=2)
button5 = tk.Button(root, text="5", command=lambda: on_button_click("5"), width=4, height=2)
button6 = tk.Button(root, text="6", command=lambda: on_button_click("6"), width=4, height=2)
button7 = tk.Button(root, text="7", command=lambda: on_button_click("7"), width=4, height=2)
button8 = tk.Button(root, text="8", command=lambda: on_button_click("8"), width=4, height=2)
button9 = tk.Button(root, text="9", command=lambda: on_button_click("9"), width=4, height=2)
buttonAdd = tk.Button(root, text="+", command=lambda: on_button_click("+"), width=4, height=2)
buttonSubtrack = tk.Button(root, text="-", command=lambda: on_button_click("-"), width=4, height=2)
buttonMultiply = tk.Button(root, text="*", command=lambda: on_button_click("*"), width=4, height=2)
buttonDivide = tk.Button(root, text="/", command=lambda: on_button_click("/"), width=4, height=2)
buttonResult = tk.Button(root, text="=", command=result, width=4, height=2)
buttonClear = tk.Button(root, text="CLS", command=clear, width=4, height=2)

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
buttonAdd.grid(row=2, column=3)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonSubtrack.grid(row=3, column=3)
button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
buttonMultiply.grid(row=4, column=3)
button0.grid(row=5, column=0)
buttonClear.grid(row=5, column=1)
buttonDivide.grid(row=5, column=2)
buttonResult.grid(row=5, column=3)
root.mainloop()



