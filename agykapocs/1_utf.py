with open('agykapocs.csv', 'r', encoding='windows-1252', errors='ignore') as input, open('agykapocs_utf.csv', 'w', encoding='utf-8') as output:
    i = 0
    for line in input:
        i += 1
        # print(i)
        output.write(line)