import pickle

word_dict = dict()

with open('agykapocs_utf_clear_2_format.csv', 'r', encoding='utf-8',) as input, open('agykapocs_utf_clear_2_format_2.csv', 'w', encoding='utf-8') as output:
    i = 0
    word_num = 0
    for line in input:
        num1 = 0
        num2 = 0
        i += 1
        # print(i)
        words = line.split(';')
        if words[0] not in word_dict:
            word_num += 1
            word_dict[words[0]] = word_num
            num1 = word_num
        else:
            num1 = word_dict[words[0]]
        if words[1] not in word_dict:
            word_num += 1
            word_dict[words[1]] = word_num
            num2 = word_num
        else:
            num2 = word_dict[words[1]]
        output.write(str(num1) + ';' + str(num2) + ';' + words[2])
    print(f'number of different words: {word_num}')

with open('dict.txt', 'wb') as dict_output:
    # dict_output.write(str(word_dict).replace("\'", "\""))
    pickle.dump(word_dict, dict_output)