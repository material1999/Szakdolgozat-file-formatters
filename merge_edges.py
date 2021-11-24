for i in range(1, 1081):
    input_filename = './networks/' + str(i) + '/edgeweighted.csv'
    output_filename = './networks/' + str(i) + '/edgeweighted_edit.csv'
    with open(input_filename, 'r', encoding='utf-8',) as input, open(output_filename, 'w', encoding='utf-8') as output:
        output.write('\"V1\";\"V2\";\"edgeweight\"\n')
        print(i)
        next(input)
        line_dict = dict()
        for line in input:
            # print(line)
            words = line.split(';')
            temp_string = words[0] + ';' + words[1] if words[0] < words[1] else words[1] + ';' + words[0]
            if temp_string not in line_dict:
                line_dict[temp_string] = float(words[2].strip())
            else:
                line_dict[temp_string] = 1 - (1 - float(line_dict[temp_string])) * (1 - float(words[2].strip()))
        for key, value in line_dict.items():
            output.write(str(key) + ';' + str(value) + '\n')