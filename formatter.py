for i in range(1,1081):
    input = "../szakdolgozat_results/grafok/communities/sim_com_" + (str)(i) + "_max10_50szazalek_4x.csv"
    output = "../szakdolgozat_results/grafok/communities_formatted/sim_com_" + (str)(i) + "_max10_50szazalek_4x_formatted.csv"
    with open(input, 'r') as input, open(output, 'w') as output:
        community = 0
        lines = input.readlines()
        for line in lines:
            line = line.strip()
            vertices = line.split(' ')
            for vertex in vertices:
                output.write((str)(vertex) + ';' + (str)(community) + "\n")
            community += 1