with open('agykapocs_utf.csv', 'r', encoding='utf-8',) as input, open('agykapocs_utf_clear.csv', 'w', encoding='utf-8') as output:
    i = 0
    for line in input:
        i += 1
        # print(i)
        words = line.split(';')
        if words[3].strip() == 'hu' and words[2].strip() != 'no_idea' and words[1].strip() != 'no_idea' and words[1].strip().lower() != words[2].strip().lower():
            output.write(words[0].strip().lower() + ';' + words[1].strip().lower() + ';' + words[2].strip().lower() + ';' + words[3].strip().lower() + ';' + words[4].strip().lower() + '\n')