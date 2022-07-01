def helloXO():
    print("Привет, это игра крестики-нолики!")


def show_field():
    print(f"  0 | 1 | 2")
    for i in range(3):
        row_info = " | ".join(field[i])
        print(f"{i} {row_info}")


def ask():
    while True:
        x, y = map(int, input("Введите координаты клетки через пробел: ").split())

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X! Поздравляем!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0! Поздравляем!")
            return True
    return False

helloXO()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1
    show_field()

    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print("Игра закончена!")
        break
