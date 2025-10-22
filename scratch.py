import math

def main():
    while True:
        print("Введите номер программы ")
        select_program = input()

        if select_program == "1.1":
            print(31,18,79)

        elif select_program == "1.2":
            print(47,52,150,sep= '  ')

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
            num=input("Введите число:")
            print("Вы вывели число",num)

        elif select_program == "1.9":
            num =input ("число:")
            print(num,"вот такое число Вы ввели")

        elif select_program == "1.10":
            num=input("введите имя")
            print(num)

        elif select_program == "1.11":
            num = input("введите название команды")
            print("команда", num,"чемпион!")

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
        elif select_program == "2.22.2":
            import random
            from math import sqrt
            a = random.randint(2, 10)
            y = ((a ** 2 + 10) / (sqrt(a ** 2 + 1)))
            print(y)
if __name__ == "__main__":
    main()
else: print("вы ввели не верное число")

       


       

