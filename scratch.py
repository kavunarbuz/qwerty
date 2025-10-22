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

if __name__ == "__main__":
    main()
else: print("вы ввели не верное число")
       

