import math


def main():
    while True:
        print("Введите номер программы ")
        select_program = input()

        if select_program == "1.1":
            print(31, 18, 79)

        elif select_program == "1.2":
            print(47, 52, 150, sep='  ')

        elif select_program == "1.3":
            print(50)
            print(10)

        elif select_program == "1.4":
            print(5)
            print(10)
            print(21)

        elif select_program == "1.5":
            print(1)
            print(2)

        elif select_program == "1.6":
            print(f"{math.pi:.3f}")

        elif select_program == "1.7":
            print(f"{math.e:.1f}")

        elif select_program == "1.8":
            num = input("Введите число:")
            print("Вы вывели число", num)

        elif select_program == "1.9":
            num = input("число:")
            print(num, "вот такое число Вы ввели")

        elif select_program == "1.10":
            num = input("введите имя")
            print(num)

        elif select_program == "1.11":
            num = input("введите название команды")
            print("команда", num, "чемпион!")

        elif select_program == "1.12":
            num = input("введите имя")
            print(f"привет,{num}!")
        elif select_program == "1.13":
            n = 15
            b = n + 1
            c = n - 1
            print(n, b, c)
        elif select_program == "1.14":
            n = 2
            b = 44
            print(n, b, sep="  ")
        elif select_program == "1.15":
            n = 2
            b = 44
            c = b - 23
            print(n, b, c, sep=" ")
        elif select_program == "1.16":
            a = 5
            b = 7 + 3
            c = "7 см"
            print(a, b)
            print(c)
        elif select_program == "1.16a":
            a = 5
            b = 7 + 3
            c = "7 см"
            print(a, b)
            print(c)
        elif select_program == "1.16b":
            for t in range(1, 3):
                for v in range(1, 2):
                    print(100, t)
                    print(1949, v)
        elif select_program == "1.16c":
            for x in range(1, 3):
                for y in range(1, 2):
                    print(x, 25)
                    print(x, y)
        elif select_program == "1.17a":
            print(2, "кг")
            print(13, 14 + 3)
        elif select_program == "1.17b":
            for a in range(1, 5):
                for b in range(1):
                    print(a, 1)
                    print(19, b)
        elif select_program == "1.17c":
            for x in range(1, 2):
                for y in range(3):
                    print(x, y)
                    print(2 + 3, y)
        elif select_program == "2.1a":
            for x in range(1, 10):
                y = 17 * x ** 2 - 6 * x + 13
                print(y)
        elif select_program == "2.1b":
            import random
            a = random.randint(2, 10)
            y = 3 * a ** 2 + 5 * a - 21
            print(y)
        elif select_program == "2.2":
            import random
            from math import sqrt
            a = random.randint(2, 10)
            y = ((a ** 2 + 10) / (sqrt(a ** 2 + 1)))
            print(y)
        elif select_program == "2.3a":
            import math
            import random
            from math import sqrt
            a = random.randint(-2, 10)
            y = sqrt((2 * a + math.sin(3 * abs(a)) / 3.56))
            print(y)
        elif select_program == "2.3b":
            import math
            import random
            from math import sqrt
            x = random.randint(1, 10)
            y = math.sin((3.2 + (sqrt(1 + x)) / abs(5 * x)))
            print(y)
        elif select_program == "2.4":
            import random
            a = random.randint(1, 10)
            P = 4 * a
            print(P)
        elif select_program == "2.5":
            import random
            a = random.randint(1, 15)
            diam = a * 2
            print(diam)
        elif select_program == "2.6":
            import math
            R = 6350
            h = 15
            горизонт = (2 * R * h + h ** 2)
            линия = (math.sqrt(горизонт))
            print(линия)
        elif select_program == "2.7":
            a = 14
            V = a ** 3
            Sбок = 4 * (a ** 2)
            print(V, Sбок)
        elif select_program == "2.8":
            import math
            R = 7
            l = 2 * (math.pi) * R
            S = (math.pi) * (R ** 2)
            print(l, S)
        elif select_program == "2.9a":
            import random
            x = random.randint(1, 5)
            y = random.randint(11, 16)
            z = 2 * x ** 3 - 3, 44 * x * y + 2, 3 * x ** 2 - 7, 1 * y + 2
            print(z)
        elif select_program == "2.9b":
            for a in range(1, 2):
                for b in range(2, 3):
                    x = 3, 14 * ((a + b) ** 3) + 2, 75 * b ** 2 - 12, 7 * a - 4, 1
                    print(x)
        elif select_program == "2.10":
            from math import sqrt
            a = 21
            b = 42
            ариф = (a + b) / 2
            геом = sqrt(a * b)
            print(ариф, геом, sep="       ")
        elif select_program == "2.11":
            v = 2314
            m = 32412
            p = (m / v)
            print(p)
        elif select_program == "2.12":
            кол = 287519
            s = 32932
            p = (кол / s)
            print(round(p), "житель на 1м^2")
        elif select_program == "2.13":
            import random
            a = random.randint(-10, 10)
            b = random.randint(-5, 5)
            for x in range(1, 10):
                С = a * x + b
                if a != 0:
                    print("a*x+b = 0", С, sep=";")
        elif select_program == "2.14":
            from math import sqrt
            k = 22
            k2 = 41
            c = k ** 2 + k2 ** 2
            w = sqrt(c)
            print(round(w))
        elif select_program == "2.15":
            import math
            S = math.pi * (25 ** 2 - 17 ** 2)
            print(S)
        elif select_program == "2.16":
            from math import sqrt
            k = 6
            k2 = 8
            г = sqrt(k ** 2 + k2 ** 2)
            P = k + k2 + г
            print(P)
        elif select_program == "2.17":
            from math import sqrt
            a1 = 7
            a2 = 3
            h = 4
            абок = sqrt(((a1 - a2) / 2) ** 2 + h ** 2)
            P = абок * 2 + a1 + a2
            print(P)
        elif select_program == "2.18":
            import math
            from math import sqrt
            for x in range(1, 2):
                for y in range(-1, 5):
                    a = ((x + 2 + y) / (x ** 2))
                    b = (y) + (1 / (sqrt(x ** 2 + 10)))
                    z = (a / b)
                    q = (7, 25 * math.sin(x) - abs(y))
                    print(z, q, sep=",   ")
        elif select_program == "2.19":
            import math
            from math import sqrt
            for a in range(1, 10):
                for b in range(1, 2):
                    x = (((2 / (a ** 2 + 25)) + b) / (sqrt(b) + ((a + b) / 2)))
                    c = (abs(a) + 2 * math.sin(b))
                    w = (5.5 * a)
                    y = (c / w)
                    print(x, y, sep=" ,                    ")
        elif select_program == "2.20":
            import math
            import random
            from math import sqrt
            from random import randint
            for e in range(1, 10):
                for f in range(1, 2):
                    for g in range(3, 5):
                        for h in range(6, 10):
                            a = (sqrt(abs(e - (3 / f) ** 3) + g))
                            b = (math.sin(e) + (math.pow(math.cos(h), 2)))
                            c = ((33 * g) / (e * f - 3))
                            print(a, b, c, sep=(" ,           "))
        elif select_program == "2.21":
            import math
            import random
            from math import sqrt
            from random import randint
            for e in range(1, 10):
                for f in range(1, 2):
                    for g in range(3, 5):
                        for h in range(6, 10):
                            a = ((e + (f / 2) / 3))
                            b = (abs(h ** 2 - g))
                            c = (sqrt(((g - h) ** 2) - 3 * math.sin(e)))
                            print(a, b, c, sep=" ,            ")
        elif select_program == "2.22":
            from math import sqrt
            a = 32
            b = 54
            ar = abs(a + b) / 2
            geo = sqrt(abs(a * b))
            print(ar, geo, sep=",      ")
        elif select_program == "2.23":
            from math import sqrt
            a = 32
            b = 12
            p = (32 + 12) * 2
            d = sqrt((a ** 2 + b ** 2))
            print(p, d)
        elif select_program == "2.24":
            from math import sqrt
            a = 112
            b = 82
            c = a + b
            r = a - b
            s = a * b
            o = a // b
            print(c, r, s, o, sep=",    ")
        elif select_program == "2.25":
            from math import sqrt
            a = 11
            b = 5
            c = 3
            v = a * b * c
            s = 2 * (a + b) * c
            print(v, s)
        elif select_program == "2.26":
            from math import sqrt
            x1 = 2
            y1 = 3
            x2 = 6
            y2 = 7
            d = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            print(d)
        elif select_program == "2.27":
            from math import sqrt
            a = 7
            b = 5
            h = 4
            c = sqrt((((a - b) / 2) ** 2) + (h ** 2))
            p = c * 2 + a + b
            print(p)
        elif select_program == "2.28":
            import math
            from math import sqrt
            a = 7
            b = 5
            y = (60)
            ak = (7 - 5) / 2
            h = (ak * math.tan(60))
            s = ((a + b) / 2) * h
            print(s)
        elif select_program == "2.29":
           from math import sqrt
           x1 = 6
           y1 = 4
           x2 = 3
           y2 = 1
           x3 = -7
           y3 = -1
           a = sqrt((x1 - x2) ** 2 + (y1 + y2) ** 2)
           b = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
           c = sqrt((x1 - x3) ** 2 + (y1 + y3) ** 2)
           P = (a + b + c)
           p = (a + b + c) / 2
           S = sqrt(p * (p - a) * (p - b) * (p - c))
           print(P, S)
        elif select_program == "2.30":
          import math
          from math import sqrt
          x1 = 9
          y1 = 7
          x2 = 2
          y2 = 3
          x3 = 4
          y3 = 0
          x4 = 3
          y4 = 6
          a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
          b = sqrt(((x3 - x2) ** 2 + (y3 - y2) ** 2))
          c = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
          d = sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
          s = 1 / 4 * abs(a ** 2 + c ** 2 - b ** 2 - d ** 2) * math.tan(90)
          print(abs(s))
        elif select_program == "2.31":
            import math
            import random
            к = 142
            п = 97
            я = 86
            x = random.randrange(1, 10)
            y = random.randrange(1, 10)
            z = random.randrange(1, 10)
            print(x * к + п * y + я * z)
        elif select_program == "2.32":
            import math
            import random
            m = 23414
            s = 14323
            k = 1700
            d = 2340
            n = random.randint(1, 100)
            print(3 * (m + s + k + d))
            print(n * (m + s + k + d))
        elif select_program == "2.33":
            import math
            import random
            t = random.randint(1, 16)
            m = random.randint(1, 16)
            s = ((t + m) / 2)
            print(s)
            print(s - t)
            print(s - m)
        elif select_program == "2.34":
            import random
            from random import randint
            v1 = random.randint(40, 100)
            v2 = random.randint(50, 110)
            s = random.randint(10000, 15000)
            print(s / (v1 + v2))
        elif select_program == "2.35":
            import random
            from random import randint
            v1 = random.randint(80, 100)
            v2 = random.randint(50, 79)
            t = 30
            s = (t * (v1 * v2))
            print(s, "м")
        elif select_program == "2.36":
            import random
            from random import randint
            t = random.randrange(36, 41)
            f = ((t * 1.8) + 32)
            k = (t - 273.15)
            print(f, k)
        elif select_program == "2.37":
            import random
            f = 450
            c = ((450 / 1.8) - 32)
            print(c)
        elif select_program == "2.38":
            import random
            a = random.randint(3, 8)
            b = random.randint(5, 10)
            e = (a + b)
            w = (a - b)
            q = (a * b)
            s = (a / b)
            d = (a + b) / 2
            print(e, w, q, s, d, sep=",    ")
        elif select_program == "2.39":
if __name__ == "__main__":
    main()
else:
    print("вы ввели не верное число")




