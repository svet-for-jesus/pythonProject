#17 Дан список с числами: [1, 2, 3, 4, 5]. Найдите сумму квадратов элементов этого списка.
chislo = [1, 2, 3, 4, 5]
i =0
result=0
while i < len(chislo):
    result=chislo[i]**2+result
    i+=1
print((result))

#18 Дана некоторая строка: 'abcdeabc'. Очистите ее от дублей символов: 'abcde'
a= 'abcdeabc'
b="abcde"
print(a.replace(b, ""))

#19  Даны два сета: st1 = {1, 2, 3, 4, 5} st2 = {4, 5, 6, 7, 8}. Получите сет их общих элементов: {4, 5}
st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}
result=st1.intersection(st2)
print(result)

#20 Дан текст со словами. Запишите в список все слова, начинающиеся на букву 'a'
text = (f"Текст (от лат. textus — ткань; сплетение, сочетание) — а чебурашки живут в африке. зафиксированная на каком-либо материальном носителе человеческая мысль; в общем плане связная и полная последовательность символов. Существуют две основные трактовки понятия «текст»: имманентная (расширенная, философски нагруженная) и репрезентативная (более частная). Имманентный подход подразумевает отношение к тексту как к автономной реальности, нацеленность на выявление его внутренней структуры. Репрезентативный — рассмотрение текста как особой формы представления информации о внешней тексту действительности. В лингвистике термин «текст» используется в широком значении, включая и образцы устной речи. Восприятие текста изучается в рамках лингвистики текста и психолингвистики. Так, например, И. Р. Гальперин определяет текст следующим образом: «Это письменное сообщение, объективированное в виде письменного документа, состоящее из ряда высказываний, объединённых разными типами лексической, грамматической и логической связи, имеющее определённый модальный характер, прагматическую установку и соответственно литературно обработанное». В смысловой цельности текста отражаются те связи и зависимости, которые имеются в самой действительности (общественные события, явления природы, человек, его внешний облик и внутренний мир, предметы неживой природы и т. д.). Единство предмета речи — это тема высказывания. Тема — это смысловое ядро текста, конденсированное и обобщённое содержание текста. Понятие «содержание высказывания» связано с категорией информативности речи и присуще только тексту. Оно сообщает читателю индивидуально-авторское понимание отношений между явлениями, их значимости во всех сферах придают ему смысловую цельность. большом тексте ведущая тема распадается на ряд составляющих подтем; подтемы членятся на более дробные, на абзацы (микротемы).")
text = text.lower().rsplit(sep=None, maxsplit=-1)
new_str=[]
for i in text:
    if i.startswith('а'):  # Проверяем, начинается ли слово с 'а'
        new_str.append(i)  # Добавляем слово в новый список
print(new_str)
