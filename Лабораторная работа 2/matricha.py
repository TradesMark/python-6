# Task
# Реализуйте перемножение квадратных матриц произвольной размерности,
# используя библиотеку numpy (для создания матриц) и библиотеку
# threading (поточное вычисление).

# Решение
import numpy as np
import threading


class shet(threading.Thread):
    def __init__(self, num, a, b, m_m):
        threading.Thread.__init__(self)
        self.tnum = num
        self.A = a
        self.B = b
        self.m_m = m_m

    def run(self):
        if self.tnum is 0:
            self.m_m.append([])
            for i in range(3):
                self.m_m[0].append(sum(self.A[0]*self.B[:,i]))
        if self.tnum is 1:
            self.m_m.append([])
            for i in range(3):
                self.m_m[1].append(sum(self.A[1]*self.B[:,i]))
        if self.tnum is 2:
            self.m_m.append([])
            for i in range(3):
                self.m_m[2].append(sum(self.A[2]*self.B[:,i]))
            с = np.array(self.m_m)
            out_put(с)

def output(arr):
    print(f'Массив A:\n{A}')
    print(f'Массив B:\n{B}')
    print(f'Массив А*B:\n{arr}')

A = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
B = np.array([(9, 8, 7), (6, 5, 4), (3, 2, 1)])
mult_matr = []

if __name__ == '__main__':
    for i in range(3):
        thread = shet(i, A, B, mult_matr)
        thread.setName(i)
        thread.start()
        
        
