import collections
from pathlib import Path

for i in range(1,1081):

    input = "../szakdolgozat_results/grafok/communities_formatted/sim_com_" + (str)(i) + "_max10_50szazalek_4x_formatted.csv"
    output = "../szakdolgozat_results/grafok/communities_sorted/sim_com_" + (str)(i) + "_max10_50szazalek_4x_sorted.csv"
    
    with open(input, 'r') as input, open(output, 'w') as output:
        dictionary = dict()
        lines = input.readlines()     
        for line in lines:
            vertex, community = line.strip().split(';')
            if vertex in dictionary:
                dictionary[vertex] += 1
            else:
                dictionary[vertex] = 1
        
        dictionary = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
        dictionary = collections.OrderedDict(dictionary)

        for kulcs, ertek in dictionary.items():
            output.write((str)(kulcs) + ':' + (str)(ertek) + "\n")
        