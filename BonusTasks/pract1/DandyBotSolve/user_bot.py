import random
import random_bot


def script(check, x, y):

    if check("level") == 1:
        # По умолчанию идем всегда направо, если вдруг встречается стена, то идем вниз
        if check("gold", x, y):
            return "take"
        elif check("wall", x+2, y):
            return "down"
        return "right"
    elif check("level") == 2:
        # По умолчанию идем вверх
        # Для постановки игрока на первоначальную линию, где находится золото
        # используется условие проверки стены на 2 блока справа
        # Затем просто проверяется, где находится золото и туда делается шаг.
        if check("gold", x, y):
            return "take"

        if check("gold", x + 1, y):
            return  "right"
        elif check("gold", x - 1, y):
            return  "left"
        if check("gold", x, y - 1):
            return  "up"
        elif check("gold", x, y + 1):
            return  "down"

        if not check("wall",x+2,y):
            return "right"
        return "up"
    elif check("level") == 3:
        #Проверятся все блоки вокруг игрока и, в зависимости от этого, делается шаг
        # Таким образом происходит обход локации против часовой стрелки
        if check("gold", x, y):
            return "take"

        u = check("wall", x, y - 1)
        d = check("wall", x, y + 1)
        r = check("wall", x + 1, y)
        l = check("wall", x - 1, y)
        ur = check("wall", x + 1, y - 1)
        dr = check("wall", x + 1, y + 1)
        dl = check("wall", x - 1, y + 1)
        ul = check("wall", x - 1, y - 1)
        if l and d:
            return "right"
        if r and d:
            return "up"
        if u and r:
            return "left"
        if l and u:
            return "down"
        if d:
            return "right"
        if r:
            return "up"
        if u:
            return "left"
        if l:
            return "down"
        if ur:
            return "up"
        if dr:
            return "right"
        if dl:
            return "down"
        if ul:
            return "left"
    elif check("level") == 4:
        # Сохраняется логика из 3го уровня и добавляется "прыжок" на противоположную платформу
        # Прыжок происходит при условии, что сверху есть 3 блока подряд и сниху есть один блок
        # Прыжок происходит в двух направлениях: вниз и вверх
        if check("gold", x, y):
            return "take"
        if check("wall", x, y - 2) & check("wall", x + 1, y - 2) & check("wall", x + 2, y - 2) & check("wall", x, y + 1):
            return "up"
        if check("wall", x, y + 2) & check("wall", x - 1, y + 2) & check("wall", x - 2, y + 2) & check("wall", x, y - 1):
            return "down"
        u = check("wall", x, y - 1)
        d = check("wall", x, y + 1)
        r = check("wall", x + 1, y)
        l = check("wall", x - 1, y)
        ur = check("wall", x + 1, y - 1)
        dr = check("wall", x + 1, y + 1)
        dl = check("wall", x - 1, y + 1)
        ul = check("wall", x - 1, y - 1)
        if l and d:
            return "right"
        if r and d:
            return "up"
        if u and r:
            return "left"
        if l and u:
            return "down"
        if d:
            return "right"
        if r:
            return "up"
        if u:
            return "left"
        if l:
            return "down"
        if ur:
            return "up"
        if dr:
            return "right"
        if dl:
            return "down"
        if ul:
            return "left"
    return "pass"
