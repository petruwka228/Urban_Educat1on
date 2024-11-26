def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    i = 1
    for string in strings:
        byte_position = file.tell()
        file.write(string + '\n')
        strings_positions[(i, byte_position)] = string
        i += 1
    file.close()
    return strings_positions

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)
