import os
import numpy as np
import matplotlib.pyplot as plt

class ChannelIndex:
    @staticmethod
    def extract_indices(file_path):
        try:
            with open(file_path) as file:
                lines = [line.rstrip() for line in file]
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")

        text = ' '.join(lines)
        text = text.replace(",", " ").replace("&", ",").replace("\n", "").replace("[", "").replace("]", "")

        input_text = text.split("UNIT")[0]
        channel_ = input_text.split("=")[1]
        channel_list = channel_.split(",")

        flow_mass_index = None
        crank_angle_index = None

        for i, channel in enumerate(channel_list):
            if channel == " 'Crank Angle' ":
                crank_angle_index = i
            elif channel == "  ':flow:total_mass' ":
                flow_mass_index = i

        if crank_angle_index is None or flow_mass_index is None:
            raise ValueError("Required indices not found in file.")

        return crank_angle_index, flow_mass_index

class PlotData:
    @staticmethod
    def plot_data(x, y, rpm, color):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(x, y, linewidth=1, color=color, label=f'Flow Mass @ {rpm} RPM')
        plt.xticks(np.arange(0, 1281, 85.25))
        plt.yticks(np.arange(0.1355, 0.1440, 0.0005))
        plt.title(f'Total Mass @ {rpm} rpm', fontweight="bold")
        plt.text(0.141, 700, ':flow:total_mass(g)')
        plt.ylabel('Total Mass (g)')
        plt.xlabel('Crank Angle (deg)')
        plt.grid(visible=True, which='major', axis='both', linestyle='dashed')
        plt.legend(loc='upper left')
        plt.xlim([0, 1279])
        plt.ylim([0.1355, 0.143])
        plt.show()

    @staticmethod
    def plot_average(x, y_a, y_b, y_average):
        fig, ax = plt.subplots(figsize=(12, 6))
        #ax.plot(x, y_a, linewidth=1, color='red', label='Flow Mass @ 3500 RPM')
        #ax.plot(x, y_b, linewidth=1, color='green', label='Flow Mass @ 3750 RPM')
        ax.plot(x, y_average, linewidth=1, color='blue', label='Average Flow Mass')
        plt.xticks(np.arange(0, 1281, 85.25))
        plt.yticks(np.arange(0.1355, 0.1440, 0.0005))
        plt.title(f'Average Total Mass', fontweight="bold")
        plt.text(0.141, 700, ':flow:total_mass(g)')
        plt.ylabel('Total Mass (g)')
        plt.xlabel('Crank Angle (deg)')
        plt.grid(visible=True, which='major', axis='both', linestyle='dashed')
        plt.legend(loc='upper left')
        plt.xlim([0, 1279])
        plt.ylim([0.1355, 0.143])
        plt.show()

class GraphPlotter:
    def __init__(self):
        self.user_input = None
        self.crank_angle = False

    def set_working_directory(self):
        # Set the working directory to the location of your data files
        working_directory = "/Users/vladimirspanic/Documents/AVL/AVL_solution"
        os.chdir(working_directory)
        print(f"Working directory set to: {os.getcwd()}")

    def get_user_input(self):
        self.set_working_directory()

        while True:
            channel_choose = input("For choosing channel 'Crank angle' press '+': ")
            if channel_choose == "+":
                self.crank_angle = True
                break
            else:
                print("Invalid input. Please enter +")

        while True:
            user_input = input("Hi user :). Please press a, b, c for the type of diagram you want: a) Flow mass @3500 RPM, b) Flow mass @3750 RPM, c) Average Flow mass: ")
            if user_input.lower() in ['a', 'b', 'c']:
                break
            else:
                print("Invalid input. Please enter a, b, or c.")

        self.user_input = user_input

    def input_and_plot(self):
        self.get_user_input()

        if self.user_input.lower() in ['a', 'b', 'c'] and self.crank_angle:
            file_paths = {"a": "003_B1_SN2c2_FL_3500rpm_fl2.txt", "b": "004_B1_SN1c7_FL_3750rpm_fl2.txt", "c": None}
            file_path = file_paths[self.user_input.lower()]

            if self.user_input.lower() == 'a' or self.user_input.lower() == 'b':
                crank_angle_index, flow_mass_index = ChannelIndex.extract_indices(file_path)

                with open(file_path) as file:
                    lines = [line.rstrip() for line in file]

                index = lines.index("END")
                matrix_data = lines[index + 1:]

                values_x = []
                values_y = []

                for line in matrix_data:
                    current_line = line.split("\t")
                    values_x.append(current_line[crank_angle_index])
                    values_y.append(current_line[flow_mass_index])

                values_y_gram = np.array(values_y, dtype=np.float64) * 1000

                x_plot = values_x
                y_plot = values_y_gram

                if self.user_input.lower() == 'a':
                    PlotData.plot_data(x_plot, y_plot, 3500, 'red')
                elif self.user_input.lower() == 'b':
                    PlotData.plot_data(x_plot, y_plot, 3750, 'green')
            else:
                if self.user_input.lower() == 'c':
                    file_path_a = "003_B1_SN2c2_FL_3500rpm_fl2.txt"
                    file_path_b = "004_B1_SN1c7_FL_3750rpm_fl2.txt"

                    crank_angle_index_a, flow_mass_index_a = ChannelIndex.extract_indices(file_path_a)
                    crank_angle_index_b, flow_mass_index_b = ChannelIndex.extract_indices(file_path_b)

                    with open(file_path_a) as file_a:
                        lines_a = [line.rstrip() for line in file_a]

                    with open(file_path_b) as file_b:
                        lines_b = [line.rstrip() for line in file_b]

                    index_a = lines_a.index("END")
                    matrix_data_a = lines_a[index_a + 1:]

                    index_b = lines_b.index("END")
                    matrix_data_b = lines_b[index_b + 1:]

                    values_x_a = []
                    values_y_a = []

                    for line in matrix_data_a:
                        current_line = line.split("\t")
                        values_x_a.append(current_line[crank_angle_index_a])
                        values_y_a.append(current_line[flow_mass_index_a])

                    values_y_gram_a = np.array(values_y_a, dtype=np.float64) * 1000

                    values_x_b = []
                    values_y_b = []

                    for line in matrix_data_b:
                        current_line = line.split("\t")
                        values_x_b.append(current_line[crank_angle_index_b])
                        values_y_b.append(current_line[flow_mass_index_b])

                    values_y_gram_b = np.array(values_y_b, dtype=np.float64) * 1000

                    x_plot_c = values_x_a
                    y_plot_a = values_y_gram_a
                    y_plot_b = values_y_gram_b
                    y_average = np.mean([y_plot_a, y_plot_b], axis=0)

                    PlotData.plot_average(x_plot_c, y_plot_a, y_plot_b, y_average)
        else:
            print("Invalid input. Please choose a, b, or c.")

# Create an instance of GraphPlotter and call input_and_plot method
graph_plotter = GraphPlotter()
graph_plotter.input_and_plot()
