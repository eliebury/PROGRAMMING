#Посчитайте, сколько в каждом файле слов, запишите эту информацию в новый
#текстовый файл в формате "название файла<табуляция>количество слов", для
#каждого файла информация на новой строчке.

#Создайте csv-таблицу с полями "Название файла", "Автор", "Дата создания текста"
#, содержащую информацию о всех статьях. Пример таблицы ниже.
#Название файла	Автор	Дата создания текста
#file.xhtml	Батюшков Константин	2017.05.30

#Найдите в текстах все биграммы вида "прилагательное в род. пад.
#+ существительное в род. пад.". В новый текстовый файл запишите найденные
#биграммы; на каждой строке нужно записать биграмму и предложение, в котором она
#встретилась, разделив их табуляцией. Повторяющиеся биграммы убирать не надо.

import re
import csv
import os

## по первой: с помощью модуля os всё читается, открывается 

folder = 'news'
print(os.listdir(folder))
for f in os.listdir(folder):
    with open(os.path.join(folder, f)) as text:
        a = text.read()
        for str in a:
            b = str.count('<w>')
        print(f, b)

## по третьей: ищутся, предположим, прилагательные в р.п
## смотрится правый контекст на предмет существительных в р.п.
## 