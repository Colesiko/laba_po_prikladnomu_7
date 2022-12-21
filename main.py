import logging
logging.basicConfig(filename="ex.log", level=logging.INFO)
while True:
    try:
        logging.info("User started program")
#x1, y1, x2, y2
        k = input("Введите x координату первого поля: ")

        bukv = k.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                k = input("Введите число от 1 до 8(цифрами): ")
                bukv = str.isnumeric(k)
        k = int(k)
        if k <= 0 or k > 8:
            print("Вы ввели некорректное значение")
            logging.error("Incorrect number.")
            continue
        logging.info(f"Users input {k}")

        l = input("Введите y координату первого поля: ")

        bukv = l.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                l = input("Введите число от 1 до 8(цифрами): ")
                bukv = str.isnumeric(l)
        l = int(l)
        if l <= 0 or l > 8:
            print("Вы ввели некорректное значение")
            logging.error("Incorrect number.")
            continue
        logging.info(f"Users input {l}")

        m = input("Введите x координату второго поля: ")

        bukv = m.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                m = input("Введите число от 1 до 8(цифрами): ")
                bukv = str.isnumeric(m)
        m = int(m)
        if m <= 0 or m > 8:
            print("Вы ввели некорректное значение")
            logging.error("Incorrect number.")
            continue
        logging.info(f"Users input {m}")

        n = input("Введите y координату второго поля: ")

        bukv = n.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                n = input("Введите число от 1 до 8(цифрами): ")
                bukv = str.isnumeric(n)
        n = int(n)
        if n <= 0 or n > 8:
            print("Вы ввели некорректное значение")
            logging.error("Incorrect number.")
            continue
        logging.info(f"Users input {n}")

        print("Выберите вашу фигуру: 1 - Конь, 2 - Слон, 3 - Ладья, 4 - Ферзь")
        fig = input("Ваша фигура: ")

        bukv = fig.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                fig = input("Введите число от 1 до 4(цифрами): ")
                bukv = str.isnumeric(fig)
        fig = int(fig)
#1 - конь, 2 - слон, 3 - ладья, 4 - ферзь
        if fig <= 0 or fig > 4:
            print("Вы ввели некорректное значение")
            logging.error("Incorrect number.")
            continue
    except ValueError:
        print("Вы ввели некорректное значение")
        logging.info("ValueError.")
        logging.info(f"Users entered figure: {fig}")

#1-1 8-8; 1-3 6-8 - белые с чётной суммой
#1-2 7-8; 1-4 7-8 - чёрные с нечётной
    sum1 = (k + l) % 2
    sum2 = (m + n) % 2
    if sum1 == sum2:
        print("Они обе", end=" ")
        logging.info("Program printed to user.")
        if sum1 == 1:
            print("чёрного ", end="")
        else:
            print("белого ", end="")
        print("цвета")
        logging.info("Program printed to user.")
    else:
        print("Они разных цветов")
        logging.info("Program printed to user.")

    distx = abs(k-m)
    disty = abs(l-n)
    if fig == 1:
        if distx == 2 and disty == 1 or distx == 1 and disty == 2:
            print(f"Конь бъёт поле ({m};{n}) за один ход.")
            logging.info("Program printed to user.")
        else:
            print("Не угрожает")
            logging.info("Program printed to user.")
    elif fig == 2:
        if distx == disty:
            print(f"Слон угрожает полю({m};{n})")
            logging.info("Program printed to user.")
        else:
            print("Слон не угрожает заданному полю")
            logging.info("Program printed to user.")
#Надо отнимать от диагонали фигуры числа до тех пор, пока число не будет равно числу диагонали слона
    elif fig == 3:
        if k == m or l == n:
            print(f"Ладья угрожает полю ({m};{n})")
            logging.info("Program printed to user.")
        else:
            print("Ладья не угрожает данному полю")
            print(f"Для нападения переставьте фигуру на поле ({k};{n})")
            logging.info("Program printed to user.")
    else:
        if distx == disty or k == m or l == n:
            print(f"Ферзь угрожает полю ({m};{n})")
            logging.info("Program printed to user.")
        else:
            print("Ферзь не угрожает данному полю")
            print(f"Для нападения передвиньте ферзя на поле ({m};{l})")
            logging.info("Program printed to user.")
    logging.info("Programm ended")
    i = input("Если вы хотите выйти из программы введите 0, если вы хотите продолжить введите 1: ")
    bukv = i.isdigit()
    if bukv == False:  # проверка на буквы
        while bukv == False:
            i = input("Введите 0 если хотите выйти из программы или 1, если вы хотите прододжить(цифрами): ")
            bukv = str.isnumeric(i)
    i = int(i)
    if i == 0:
        break
