print("----------   Игра Крестики-Нолики   ----------")
field_ = [
    [" ", "1", "2", "3"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"],
    ["3", "-", "-", "-"]
]


# функция игрового поля
def field_func(field_in):
    for i in field_in:
        for j in i:
            print(j, end=" ")
        print()


# функция проверки условий ввода
def check_input():
    global player
    while True:
        coord_ = input(f"Введите координаты {player} - номер строки и столбца через пробел: ").split()

        if len(coord_) != 2:
            print("Координат должно быть две")
            continue

        i, j = coord_

        if not(i.isdigit()) or not(j.isdigit()):
            print("Введите числа!")
            continue

        i, j = map(int, coord_)

        if i < 1 or i > 3 or j < 1 or j > 3:
            print("Неверные координаты, повторите ввод")
            continue

        if field_[i][j] != "-":
            print("Позиция занята, введите другие координаты")
            continue

        return i, j


# функция проверки выйгрыша
def winning_():
    win_variants = [([1, 1], [1, 2], [1, 3]), ([2, 1], [2, 2], [2, 3]), ([3, 1], [2, 2], [3, 3]),
                    ([1, 1], [2, 1], [3, 1]), ([1, 2], [2, 2], [3, 2]), ([1, 3], [2, 3], [3, 3]),
                    ([1, 1], [2, 2], [3, 3]), ([1, 3], [2, 2], [3, 1])]
    for x in win_variants:
        insert = []
        for y in x:
            insert.append(field_[y[0]][y[1]])
        if insert == ["x", "x", "x"]:
            print("Выиграл x !")
            return True
        if insert == ["o", "o", "o"]:
            print("Выиграл o !")
            return True
    return False


# основная функция
def gaming_func(gamer):
    global player
    global count
    if count == 9:
        return count
    if winning_():
        return print("Победа!")
    if gamer == "x":
        player = "x"
        i, j = check_input()
        field_[i][j] = "x"
        print(field_func(field_))
        count += 1
        return gaming_func("o")
    elif gamer == "o":
        player = "o"
        i, j = check_input()
        field_[i][j] = "o"
        print(field_func(field_))
        count += 1
        return gaming_func("x")


print()
field_func(field_)
print()
player = input("Выберете 'x' или 'o' для начала игры (eng. раскладка): ")
print()
count = 0

while True:
    if player == "x":
        gaming_func("x")
    elif player == "o":
        gaming_func("o")
    else:
        print("* * *")
        print("Символ не соответствует условию, игра перезапущена")
        print()
        field_func(field_)
        print()
        player = input("Начало игры, выберите с какого символа хотите начать(x/o?): ")

    if winning_():
        break

    if count == 9:
        print(" Ничья!")
        break
