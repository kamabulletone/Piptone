from struct import unpack

#from source import Source

'''
Реализовать разбор двоичного формата данных (в духе формата WAD игры Doom или
графического формата PNG). Данные начинаются с сигнатуры 0x22 0x44 0x5a 0x4c 0x4e, за которой
следует структура A. Порядок байт: от младшего к старшему. Адреса указаны в виде смещений
от начала данных. В решении разрешено использовать модуль struct..
'''


def f31(binary_data):
    start_from = [int(i) for i in [0x22, 0x44, 0x5a, 0x4c, 0x4e]]
    # Получение id, с которого необходимо начать обработку
    idx = [
        (i, i + len(start_from)) for i in range(len(binary_data))
        if [int(i) for i in binary_data[i:i + len(start_from)]] == start_from
    ][0][1]

    def struct_a(index):
        response = {}

        # Адрес (uint32) структуры B
        [a1] = unpack('<i', binary_data[index:index + 4])
        index += 4
        response['A1'], b = struct_b(a1)

        # uint64
        [a2] = unpack('<Q', binary_data[index:index + 8])
        index += 8
        response['A2'] = a2

        # uint16
        [a3] = unpack('<H', binary_data[index:index + 2])
        index += 2
        response['A3'] = a3

        # uint64
        a4,a5,a6 = unpack('<QQQ', binary_data[index:index + 8 + 8 + 8])
        index += 8 + 8 + 8
        response['A4'] = a4
        response['A5'] = a5
        response['A6'] = a6

        # double

        [a7] = unpack('<d', binary_data[index:index + 8])
        index += 8
        response['A7'] = a7



        # Структура C
        response['A8'], index = struct_c(index)

        return response

    def struct_b(index):
        response = {}

       # Массив char, размер4
        b1 = ''.join([chr(i) for i in binary_data[index:index + 4]])
        index += 4
        response['B1'] = b1

        #uint32 []
        [b2] = unpack('<I', binary_data[index:index + 4])
        index += 4
        response['B2'] = b2


        return response, index

    def struct_c(index):
        response = {}

        # Массив адресов (uint32) структур D, размер 4
        d_size = 4
        c1_tmp = list(unpack('<4I', binary_data[index:index + 16]) ) #[index + i * 4 for i in range(d_size)]

        response['C1'] = [struct_d(i) for i in c1_tmp]
        #index = [i[1] for i in c1_tmp][d_size - 1]
        index += 4 * 4

        # int16
        [c2]= unpack('<h', binary_data[index:index + 2])
        index += 2
        response['C2'] = c2

        # массив int32, размер 3
        int32_size = 3
        c3 = list(unpack('<{}i'.format(int32_size),
                         binary_data[index:index + 4 * int32_size]))
        index += 4 * 3
        response['C3'] = c3



        return response, index

    def struct_d(index):
        response = {}

        # Размер (uint32) и адрес (uint16) массива int8
        size, address = unpack('<IH', binary_data[index:index + 6])
        d1 = list(unpack('<{}b'.format(size),
                         binary_data[address:address + 1 * size]))
        index += 6
        response['D1'] = d1

        # uint16
        d2, d3 = unpack('<HH', binary_data[index:index + 4])
        index += 4
        response['D2'] = d2
        response['D3'] = d3

        # массив uint8, размер 8
        uint8_size = 8
        d4 = list(unpack('<{}B'.format(uint8_size),
                         binary_data[index:index + 1 * uint8_size]))
        index += 1 * 8
        response['D4'] = d4

        return response

    

    return struct_a(idx)




