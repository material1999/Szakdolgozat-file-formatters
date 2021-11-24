with open('agykapocs_utf_clear_2.csv', 'r', encoding='utf-8',) as input, open('agykapocs_utf_clear_2_format.csv', 'w', encoding='utf-8') as output:
    max_weight = 1.0
    max = 0
    for line in input:
        words = line.split(';')
        if int(words[2]) > max:
            max = int(words[2])
    # print(max)
    input.seek(0)
    i = 0
    for line in input:
        i += 1
        # print(i)
        words = line.split(';')
        output.write(words[0] + ';' + words[1] + ';' + str(int(words[2]) / float(max) * max_weight) + '\n')