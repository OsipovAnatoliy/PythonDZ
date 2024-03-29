# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два 
# соседних. Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому 
# ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система 
# состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один 
# заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух 
# соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном 
# списке урожайности грядки.


import random

kust = int(input("Введите количество кустов: "))
yagodi= []
for i in range(0,kust):
    yagodi.append(random.randint(0, 10))
result = 0
i = 0
sum = 0

print(yagodi)

while (i < kust):
    if i == kust-1:
       sum = yagodi[i] + yagodi[i - 1] + yagodi[0] 
    else:
       sum = yagodi[i] + yagodi[i - 1] + yagodi[i + 1]
    if sum > result:   
        result = sum
    i += 1

print(f"Максимальное число ягод за один заход {result}")