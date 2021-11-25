import pickle

with open('dict.txt', 'rb') as dict_input, open('communities.csv', 'r') as input, open('communities_formatted.csv', 'w') as output:
    data = dict_input.read()
    word_dict = pickle.loads(data)
    # print(str(word_dict))
    # print(word_dict["mobil"])
    line_num = 0
    for line in input:
        line_num += 1
        print(line_num)
        numbers = line.split(" ")
        com_size = len(numbers)
        i = 0
        for number in numbers:
            i += 1
            output.write(list(word_dict.keys())[list(word_dict.values()).index(int(number))])
            if i != com_size:
                output.write(" --- ")
        output.write("\n")