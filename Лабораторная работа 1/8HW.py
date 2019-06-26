# Task
# Посчитайте среднюю цену за билет и медиану
# Решение
# импорт необходимых библиотек для работы
import pandas as pd

df = pd.read_csv('train.csv')
md = df['Fare'].median()
mn = df['Fare'].mean()
print(md, mn)
