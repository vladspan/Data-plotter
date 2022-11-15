import numpy as np
from Index_AVL_Spanic import ChannelIndex
from Plot_Data_AVL_Spanic import PlotData


class GraphPlotter():



    global user_input

    user_input = str(input("Hi user :). Please press a, b, c for the type of diagram you want: a) Flow mass @3500 RPM, b) Flow mass @3750 RPM, c) Average Flow mass: "))

    def input_and_plot(name: str):

        if user_input.lower() == "a":
            with open("003_B1_SN2c2_FL_3500rpm_fl2.txt") as file:
                lines_a = [line.rstrip() for line in file]

        elif user_input.lower() == "b":
            with open("004_B1_SN1c7_FL_3750rpm_fl2.txt") as file:
                lines_b = [line.rstrip() for line in file]

        elif user_input.lower() == "c":
            with open("003_B1_SN2c2_FL_3500rpm_fl2.txt") as file:
                lines_a = [line.rstrip() for line in file]

            with open("004_B1_SN1c7_FL_3750rpm_fl2.txt") as file:
                lines_b = [line.rstrip() for line in file]

        if user_input.lower() == 'a':

            index = lines_a.index("END")
            meta_data = lines_a[:index]
            matrix_data_a = lines_a[index+1:]

            values_x_a = []
            values_y_a = []

            for line in matrix_data_a:
                current_line = line.split("\t")

                values_x_a.append(current_line[main.Index_AVL_Spanic.crank_angle_index])
                values_y_a.append(current_line[main.Index_AVL_Spanic.flow_mass_index])

            values_y_a_ = list(np.float_(values_y_a))
            values_y__a = np.array(1000, dtype=np.float64)
            values_y_gram_a = values_y__a*values_y_a_

            x_plot_a = values_x_a
            y_plot_a = values_y_gram_a

            PlotData.plot_3500(x_plot_a, y_plot_a)

        if user_input.lower() == 'b':

            index = lines_b.index("END")
            meta_data = lines_b[:index]
            matrix_data_b = lines_b[index + 1:]

            values_x_b = []
            values_y_b = []

            for line in matrix_data_b:
                current_line = line.split("\t")

                values_x_b.append(current_line[ChannelIndex.crank_angle_index])
                values_y_b.append(current_line[ChannelIndex.flow_mass_index])

            values_y_b_ = list(np.float_(values_y_b))
            values_y__b = np.array(1000, dtype=np.float64)
            values_y_gram_b = values_y__b * values_y_b_

            x_plot_b = values_x_b
            y_plot_b = values_y_gram_b

            PlotData.plot_3750(x_plot_b, y_plot_b)

        if user_input.lower() == 'c':

            index_a = lines_a.index("END")
            meta_data = lines_a[:index_a]
            matrix_data_a = lines_a[index_a + 1:]

            index_b = lines_b.index("END")
            meta_data = lines_b[:index_b]
            matrix_data_b = lines_b[index_b + 1:]

            values_x_a = []
            values_y_a = []

            for line in matrix_data_a:
                current_line = line.split("\t")

                values_x_a.append(current_line[ch.crank_angle_index])
                values_y_a.append(current_line[ch.flow_mass_index])

            values_x_b = []
            values_y_b = []

            for line in matrix_data_b:
                current_line = line.split("\t")

                values_x_b.append(current_line[ch.crank_angle_index])
                values_y_b.append(current_line[ch.flow_mass_index])

            values_y_b_ = list(np.float_(values_y_b))
            values_y__b = np.array(1000, dtype=np.float64)
            values_y_gram_b = values_y__b * values_y_b_

            values_y_a_ = list(np.float_(values_y_a))
            values_y__a = np.array(1000, dtype=np.float64)
            values_y_gram_a = values_y__a * values_y_a_

            x_plot_c = values_x_a

            list_a_b = [values_y_gram_b, values_y_gram_a]
            values_a_b = [np.array(x) for x in list_a_b]
            y_plot_c = [np.mean(k) for k in zip(*values_a_b)]

            PlotData.average(x_plot_c, y_plot_c)

    input_and_plot(user_input)






