# Task
# Какие доли составляли пассажиры первого, второго, третьего класса?
# Решение
# импорт необходимых библиотек для работы
import pandas as pd

# функция для расчета доли пассажиров первого, второго и третьего классов
def perc (x):
    a=0
    for summ in x:
        a = a + summ
    for cnt in x:
        print ("%.2f" % (cnt/a), end = ' ')

# создаём DataFrame
df = pd.read_csv('train.csv')

# группируем людей по классам кают и считаем их отдельно для каждого класса

cnt = list((df.groupby(['Pclass'])['PassengerId'].count()))
perc (cnt)
