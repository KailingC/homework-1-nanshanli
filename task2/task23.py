"""Spring 2019 COMSW 4995: Applied Machine Learning.

UNI: nl2643
Homework 1 Task 2.3

Reproduce 4 plots from https://serialmentor.com/dataviz/overlapping-points.html

"""

import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


def obtainDataFromCSV(path):
    """Read csv and obtain data in format for plotting."""
    data = []
    with open('task2/mpg.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            data.append(row)
    datadict = {}
    for key in data[0]:
        datadict[key] = []
    for i in range(1, len(data)):
        for ix, key in enumerate(data[0]):
            datadict[key].append(data[i][ix])
    return datadict


def main():
    """Define main function."""
    data = obtainDataFromCSV('task2/mpg.csv')
    fig, ax = plt.subplots(2, 2)

    drv_short = ['f', 'r', '4']
    drv_long = ['FWD', 'RWD', '4WD']
    cdict = {0: 'orange', 1: 'skyblue', 2: 'black'}

    drv = np.array(data['drv'])
    cty = pd.to_numeric(np.array(data['cty']))
    displ = pd.to_numeric(np.array(data['displ']))

    # Plot  1
    for index, type in enumerate(drv_short):
        ix = np.where(drv == type)
        ax[0, 0].scatter(displ[ix[0]], cty[ix[0]],
                         c=cdict[index], label=drv_long[index], s=5)
    ax[0, 0].legend(title="drive train")
    ax[0, 0].set_ylabel('fuel economy (mpg)')
    ax[0, 0].set_xlabel('displacement (l)')
    ax[0, 0].set_xticks(np.arange(2, 7, 1))
    ax[0, 0].spines['right'].set_color('white')
    ax[0, 0].spines['top'].set_color('white')
    ax[0, 0].set_title('Figure 18.1')
    plt.setp(ax[0, 0].get_legend().get_texts(), fontsize='8')

    # Plot 2
    for index, type in enumerate(drv_short):
        ix = np.where(drv == type)
        ax[0, 1].scatter(displ[ix[0]], cty[ix[0]],
                         c=cdict[index], label=drv_long[index], s=5, alpha=0.2)
    ax[0, 1].legend(title="drive train")
    ax[0, 1].set_ylabel('fuel economy (mpg)')
    ax[0, 1].set_xlabel('displacement (l)')
    ax[0, 1].set_xticks(np.arange(2, 7, 1))
    ax[0, 1].spines['right'].set_color('white')
    ax[0, 1].spines['top'].set_color('white')
    ax[0, 1].set_title('Figure 18.2')
    plt.setp(ax[0, 1].get_legend().get_texts(), fontsize='8')

    # Plot 3
    displ_jitter = displ + np.random.randn(len(displ)) * 0.01 * (displ.max()
                                                                 - displ.min())
    cty_jitter = cty + np.random.randn(len(cty)) * 0.01 * (cty.max()
                                                           - cty.min())
    for index, type in enumerate(drv_short):
        ix = np.where(drv == type)
        ax[1, 0].scatter(displ_jitter[ix[0]], cty_jitter[ix[0]],
                         c=cdict[index], label=drv_long[index], s=5, alpha=0.2)
    ax[1, 0].legend(title="drive train")
    ax[1, 0].set_ylabel('fuel economy (mpg)')
    ax[1, 0].set_xlabel('displacement (l)')
    ax[1, 0].set_xticks(np.arange(2, 7, 1))
    ax[1, 0].spines['right'].set_color('white')
    ax[1, 0].spines['top'].set_color('white')
    ax[1, 0].set_title('Figure 18.3')
    plt.setp(ax[1, 0].get_legend().get_texts(), fontsize='8')

    # Plot 4
    displ_xjitter = displ + np.random.randn(len(displ)) * (displ.max()
                                                           - displ.min()) * .1
    cty_xjitter = cty + np.random.randn(len(cty)) * (cty.max()
                                                     - cty.min()) * .1
    for index, type in enumerate(drv_short):
        ix = np.where(drv == type)
        ax[1, 1].scatter(displ_xjitter[ix[0]], cty_xjitter[ix[0]],
                         c=cdict[index], label=drv_long[index], s=5, alpha=0.2)
    ax[1, 1].legend(title="drive train")
    ax[1, 1].set_ylabel('fuel economy (mpg)')
    ax[1, 1].set_xlabel('displacement (l)')
    ax[1, 1].set_xticks(np.arange(2, 7, 1))
    ax[1, 1].spines['right'].set_color('white')
    ax[1, 1].spines['top'].set_color('white')
    ax[1, 1].set_title('Figure 18.4')
    plt.setp(ax[1, 1].get_legend().get_texts(), fontsize='8')

    plt.tight_layout()
    plt.savefig('task2/task23.png')
    plt.show()


if __name__ == "__main__":
    main()
