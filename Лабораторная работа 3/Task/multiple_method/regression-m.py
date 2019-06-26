# Задача
# Реализовать метод линейной регрессии с несколькими переменными

# Решение

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import csv


def sq_error(_x, _y, f_x=None):
    squared_error = []
    for i in range(len(_x)):
        squared_error.append((f_x(_x[i]) - _y[i])**2)
    return sum(squared_error)

X, Y = [], []

with open("data_file/traffic.tsv") as tsvfile:
    tsv_reader = csv.reader(tsvfile, delimiter="\t")
    for line in tsv_reader:
        if line[1] != 'nan':
          X.append(float(line[0]))
          Y.append(float(line[1]))


x1 = [1, 743]

np_x = np.array(X)
np_y = np.array(Y)

x2 = list(range(743))

th1_1, th0_1 = sp.polyfit(np_x, np_y, 1)
th2_2, th1_2, th0_2 = np.polyfit(np_x, np_y, 2)
th3_3, th2_3, th1_3, th0_3 = np.polyfit(np_x, np_y, 3)
th4_4, th3_4, th2_4, th1_4, th0_4 = np.polyfit(np_x, np_y, 4)
th5_5, th4_5, th3_5, th2_5, th1_5, th0_5 = np.polyfit(np_x, np_y, 5)

plt.scatter(X, Y, label = u'Исходные данные', color='b')

f1 = sp.poly1d(np.polyfit(np_x, np_y, 1))
plt.plot(x1, f1(x1), linewidth = 3, label = u'полином 1-ой степени', color='black')

f2 = sp.poly1d(np.polyfit(np_x, np_y, 2))
plt.plot(x2, f2(x2), linewidth = 3, label = u'полином 2-ой степени', color='red')

f3 = sp.poly1d(np.polyfit(np_x, np_y, 3))
plt.plot(x2, f3(x2), linewidth = 3, label = u'полином 3-ей степени', color='yellow')

f4 = sp.poly1d(np.polyfit(np_x, np_y, 4))
plt.plot(x2, f4(x2), linewidth = 3, label = u'полином 4-ой степени', color='orange')

f5 = sp.poly1d(np.polyfit(np_x, np_y, 5))
plt.plot(x2, f5(x2), linewidth = 3, label = u'полином 5-ой степени', color='green')


fun1 = lambda x: th1_1*x + th0_1
fun2 = lambda x: th2_2*x**2 + th1_2*x + th0_2
fun3 = lambda x: th3_3*x**3 + th2_3*x**2 + th1_3*x + th0_3
fun4 = lambda x: th4_4*x**4 + th3_4*x**3 + th2_4*x**2 + th1_4*x + th0_4
fun5 = lambda x: th5_5*x**5 + th4_5*x**4 + th3_5*x**3 + th2_5*x**2 + th1_5*x + th0_5

res1 = sq_error(X, Y, fun1)
res2 = sq_error(X, Y, fun2)
res3 = sq_error(X, Y, fun3)
res4 = sq_error(X, Y, fun4)
res5 = sq_error(X, Y, fun5)

print()
print(f"Ср. кв. ошибка 1 составляет = {res1:.3f}")
print(f"Ср. кв. ошибка 2 составляет = {res2:.3f} на {100 - 100*res2/res1:.2f}% лучше ")
print(f"Ср. кв. ошибка 3 составляет = {res3:.3f} на {100 - 100*res3/res1:.2f}% лучше ")
print(f"Ср. кв. ошибка 4 составляет = {res4:.3f} на {100 - 100*res4/res1:.2f}% лучше ")
print(f"Ср. кв. ошибка 5 составляет = {res5:.3f} на {100 - 100*res5/res1:.2f}% лучше ")
print()

#Task 10 - предсказание
from sklearn.linear_model import LinearRegression

model = LinearRegression()
np_x = np_x.reshape(-1, 1)
np_y = np_y.reshape(-1, 1)
model.fit(np_x, np_y)

x_predict = np.array(list(range(744, 751)))
new_x_predict = x_predict.reshape(-1, 1)
y_predict = model.predict(new_x_predict)
y_predict = y_predict.flatten()


print("Предсказание значения целевого параметра для x = list(range(744, 751))")
print()

new_th1_1, new_th0_1 = sp.polyfit(x_predict, y_predict, 1)
print(f"Полином 1-ой степени: {new_th0_1:.3f}x + {new_th1_1:.3f}")


new_th5_2, new_th4_2, new_th3_2, new_th2_2, new_th1_2, new_th0_2 = np.polyfit(x_predict, y_predict, 5)
print(f"Полином 5-ой степени: {new_th5_2}x^5 + {new_th4_2}x^4 + {new_th3_2:.6f}x^3 + {new_th2_2:.6f}x^2 + {new_th1_2:.6f}x + {new_th0_2:.6f}")


plt.title('C несколькими переменными')
plt.legend()
plt.ylabel('y')
plt.xlabel('x')
plt.show()
plt.savefig('result.png')
