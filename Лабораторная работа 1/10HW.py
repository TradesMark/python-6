# Task
# Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?

# Решение
# импорт необходимых библиотек для работы

import pandas as pd

df = pd.read_csv('train.csv')
data = pd.read_csv('train.csv', usecols=['Name', 'Age'])

na = df[df.Age > 15][['Sex', 'Name', 'Age']]
fe = na[na.Sex == 'female'][['Name', 'Age']]

ma = na[na.Sex == 'male'][['Name', 'Age']]
ma = pd.DataFrame(ma.Name.str.split(' ', 1).tolist())

fe = pd.DataFrame(fe.Name.str.split(' ',1).tolist())

# fe[0] - исследуем столбик с именем, index[0] - выводит первый элемент

print(fe[0].value_counts().index[0], ma[0].value_counts().index[0])
