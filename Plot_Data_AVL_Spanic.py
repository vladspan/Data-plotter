import matplotlib.pyplot as plt
import numpy as np


class PlotData():

    def plot_3500(x_a: list, y_a: list):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(x_a, y_a, linewidth=1, color='red', label='flow: total_mass(g)')
        plt.xticks(np.arange(0, 1281, 85.25))
        plt.yticks(np.arange(0.1355, 0.1440, 0.0005))
        plt.title('Total Mass @3500 rpm', fontweight="bold")
        plt.text(0.141, 700, ':flow:total_mass(g)')
        plt.ylabel('Total Mass (g)')
        plt.xlabel('Crank Angle (deg)')
        plt.grid(visible=True, which='major', axis='both', linestyle='dashed')
        plt.legend(loc='upper left')
        plt.xlim([0, 1279])
        plt.ylim([0.1355, 0.143])
        plt.show()

    def plot_3750(x_b: list, y_b: list):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(x_b, y_b, linewidth=1, color='green', label='flow: total_mass(g)')
        plt.xticks(np.arange(0, 1281, 85.25))
        plt.yticks(np.arange(0.1355, 0.1440, 0.0005))
        plt.title('Total Mass @3750 rpm', fontweight="bold")
        plt.text(0.141, 700, ':flow:total_mass(g)')
        plt.ylabel('Total Mass (g)')
        plt.xlabel('Crank Angle (deg)')
        plt.grid(visible=True, which='major', axis='both', linestyle='dashed')
        plt.legend(loc='upper left')
        plt.xlim([0, 1279])
        plt.ylim([0.1355, 0.143])
        plt.show()

    def average(x_c: list, y_c: list):

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(x_c, y_c, linewidth=1, color='blue', label='Average :flow: total_mass(g)')
        plt.xticks(np.arange(0, 1281, 85.25))
        plt.yticks(np.arange(0.1355, 0.1440, 0.0005))
        plt.title('Average Total Mass', fontweight="bold")
        plt.text(0.155, 700, 'Average :flow:total_mass(g)')
        plt.ylabel('Total Mass (g)')
        plt.xlabel('Crank Angle (deg)')
        plt.grid(visible=True, which='major', axis='both', linestyle='dashed')
        plt.legend(loc='upper left')
        plt.xlim([0, 1279])
        plt.ylim([0.1355, 0.143])
        plt.show()




