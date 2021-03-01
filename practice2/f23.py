
def f23(table):
    table = delEmptyRow(table)
    talbe = TransformTableData(table)
    table = FlipTable(table)

    table = delEmptyRow(table)
    #delEmptyRow(table)


    return table

def delEmptyRow(table):


    tableLen = len(table)

    for i in table:
        isEmpty = True
        for j in i:
            if (j != None):
                isEmpty = False
        if (isEmpty):
            table.remove(i)
    return table


def FlipTable(table):

    table =[*zip(*table)]
    table = [list(i) for i in table]
    return table


def TransformTableData(table):

    for i in table:
        i[1] = i[1].split(".")[2]
        i[2] = str(round(float(i[2]) * 100)) + "%"
        i[3] = i[3].split(" ")[2] + " " + i[3].split(" ")[0]
        i[4] = i[4][i[4].find("]")+1: ]
    return table



# print(f23([ [None, None, None, None, None],
#   [None, '09.11.2004', '0.28', 'Ростислав И. Фомли', 'rostislav41[at]mail.ru'],
#   [None, '24.11.2002', '0.24', 'Назар С. Целетко', 'zeletko31[at]gmail.com'],
#   [None, '10.01.1999', '0.56', 'Яромир Ч. Кевов', 'aromir34[at]rambler.ru'] ]
#  ))
#
# print(f23([[None, None, None, None, None],
#   [None, '12.02.1999', '0.40', 'Василий М. Фегянц', 'vasilij30[at]yahoo.com'],
#   [None, '15.05.2003', '0.44', 'Тамерлан Ц. Шанемяк', 'tamerlan52[at]yandex.ru'],
#   [None, '21.01.2004', '0.93', 'Арсен Л. Цабакич', 'zabakic89[at]yandex.ru']]))

# print(f23([ ["1","2","3"],
#             [],
#             [ "5", None, "7"] ]))
# print(f23([ ["1",None,"3"], ["2", None, "10"],[ "5", None, "7"] ]))