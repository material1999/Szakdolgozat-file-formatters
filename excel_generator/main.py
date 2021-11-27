import openpyxl as xl

##### Full info #####

'''
workbook = xl.Workbook()
sheet = workbook.active
sheet.title = "Greedy_Infections"
sheet["a1"] = "file number"
sheet["b1"] = "greedy_full"
sheet["c1"] = "greedy_max10_25szazalek_5x"
sheet["d1"] = "greedy_max10_25szazalek_6x"
sheet["e1"] = "greedy_max10_50szazalek_4x"
sheet["f1"] = "greedy_max10_50szazalek_5x"
sheet["g1"] = "greedy_max10_100szazalek_3x"
sheet["h1"] = "greedy_max10_100szazalek_4x"


graph_count = 1080
for i in range(1, graph_count + 1):

    print("file: " + str(i))

    filenames = ["../../szakdolgozat_results/grafok/greedy/greedy_" + str(i) + "_full.csv",
                 "../../szakdolgozat_results/grafok/greedy/greedy_" + str(i) + "_max10_25szazalek_5x.csv",
                 "../../szakdolgozat_results/grafok/greedy/greedy_" + str(i) + "_max10_25szazalek_6x.csv",
                 "../../szakdolgozat_results/grafok/greedy/greedy_" + str(i) + "_max10_50szazalek_4x.csv",
                 "../../szakdolgozat_results/grafok/greedy/greedy_" + str(i) + "_max10_50szazalek_5x.csv",
                 "../../szakdolgozat_results/grafok/greedy/greedy_" + str(i) + "_max10_100szazalek_3x.csv",
                 "../../szakdolgozat_results/grafok/greedy/greedy_" + str(i) + "_max10_100szazalek_4x.csv"]

    current_col = "a"
    cell_to_write = current_col + str(i + 1)
    sheet[cell_to_write] = i

    for filename in filenames:
        with open(filename, 'r') as file:
            for line in file:
                pass
            infection = line.split(":")[1].strip()
            # print(infection)
            current_col = chr(ord(current_col) + 1)
            cell_to_write = current_col + str(i + 1)
            sheet[cell_to_write] = float(infection)

workbook.save('greedy_infections.xlsx')
'''



##### Aggregated info #####

workbook = xl.Workbook()
sheet = workbook.active
sheet.title = "Aggregated_Infections"
sheet["a1"] = "file numbers"
sheet["b1"] = "greedy_full"
sheet["c1"] = "greedy_max10_25szazalek_5x"
sheet["d1"] = "greedy_max10_25szazalek_6x"
sheet["e1"] = "greedy_max10_50szazalek_4x"
sheet["f1"] = "greedy_max10_50szazalek_5x"
sheet["g1"] = "greedy_max10_100szazalek_3x"
sheet["h1"] = "greedy_max10_100szazalek_4x"


graph_count = 1080
for i in range(0, graph_count // 10):

    print("files: " + str(i * 10 + 1) + "-" + str((i + 1) * 10))

    current_col = "a"
    cell_to_write = current_col + str(i + 2)
    sheet[cell_to_write] = str(i * 10 + 1) + "-" + str((i + 1) * 10)

    filenames = ["_full.csv",
                 "_max10_25szazalek_5x.csv",
                 "_max10_25szazalek_6x.csv",
                 "_max10_50szazalek_4x.csv",
                 "_max10_50szazalek_5x.csv",
                 "_max10_100szazalek_3x.csv",
                 "_max10_100szazalek_4x.csv"]

    for filename in filenames:
        infection_sum = 0
        for j in range(1, 11):
            current_filename = "../../szakdolgozat_results/grafok/greedy/greedy_" + str(i * 10 + j) + filename
            with open(current_filename, 'r') as file:
                for line in file:
                    pass
                infection = line.split(":")[1].strip()
                # print(infection)
                infection_sum += float(infection)
        infection_mean = infection_sum / 10
        current_col = chr(ord(current_col) + 1)
        cell_to_write = current_col + str(i + 2)
        sheet[cell_to_write] = float(infection_mean)

workbook.save('greedy_aggregated.xlsx')

