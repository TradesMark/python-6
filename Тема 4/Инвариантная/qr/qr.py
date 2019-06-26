import pyqrcode
import png
import random


def qr1(data, name, scale = 8):
    qr = pyqrcode.create(data)
    qr.png(name, scale = scale)

def qr2(data, name, scale = 8):
    c1 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    c2 = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    qr = pyqrcode.create(data)
    qr.png(name, scale = scale, module_color = c1, background = c2)


if __name__ == '__main__':
    text = 'https://vk.com/feed'
    qr1(text, '1.png')
    qr2(text, '2.png')
