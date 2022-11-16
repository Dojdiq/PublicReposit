roster = "3 2 8 5 4 11 13 15 21 18 19 "
at = [int(x) for x in roster.split()]
try:
    user = int(input("Введите число от 1 до 21: "))
    if user % 1 == 0:
        at.append(user)
        print("Список до сортировки: ", at)
        at.sort()
        print("Список после сортировки по возрастанию: ", at)
    else:
        print("Введите корректное число")
except ValueError:
    print("Некорректные данные.")

def binary_search(at, user, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if at[middle] == user:
            return middle
        elif user < at[middle]:
            return binary_search(at, user, left, middle - 1)
        else:
            return binary_search(at, user, middle + 1, right)
    except IndexError:
        return "Число выходит за диапазон списка, введите меньшее число."

print("Индекс введенного числа в списке: ", binary_search(at, user, 0, len(at) - 1))
