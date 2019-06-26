# Task
# Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
#       * возрастом и параметром survival;
#       * полом человека и параметром survival;
#       * классом, в котором пассажир ехал, и параметром survival.

# Решение
# импорт необходимых библиотек для работы

import pandas as pd

df = pd.read_csv('train.csv')
sex = list(df['Sex'])
ln = len(sex)

# Замещаем male и female на 1 и 0 соответственно
for i in range(ln):
    if sex[i] == 'male':
        sex[i] = 1
    else:
        sex[i] = 0

sx = pd.DataFrame({'Sex':sex})

print(df['Age'].corr(df['Survived']))
print(sx['Sex'].corr(df['Survived']))
print(df['Pclass'].corr(df['Survived']))
