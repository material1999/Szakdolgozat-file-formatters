with open('agykapocs_utf_clear.csv', 'r', encoding='utf-8',) as input, open('agykapocs_utf_clear_2.csv', 'w', encoding='utf-8') as output:
    line_dict = dict()
    i = 0
    for line in input:
        i += 1
        # print(i)
        words = line.split(';')
        temp_string = words[1] + ';' + words[2] if words[1] < words[2] else words[2] + ';' + words[1]
        if temp_string not in line_dict:
            line_dict[temp_string] = int(words[4])
        else:
            line_dict[temp_string] += int(words[4])
    for key, value in line_dict.items():
        output.write(str(key) + ';' + str(value) + '\n')