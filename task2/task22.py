"""Spring 2019 COMSW 4995: Applied Machine Learning.

UNI: nl2643
Homework 1 Task 2.2

Create pair-plot of iris dataset using only numpy and matplotlib.

"""

from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt


def transposeArray(data):
    """Tranpose array for plotting."""
    arr = [[] for i in range(0, len(data[0]))]
    for row in data:
        for i in range(0, len(data[0])):
            arr[i].append(row[i])
    return np.array(arr)


def generatePairPlots(data, col, columns):
    """Generate pair plot from an array."""
    numvars, numpoints = data.shape
    fig, ax = plt.subplots(numvars, numvars, figsize=(5, 5))
    classes = ['Setosa', 'Versicolour', 'Virginica']
    cdict = {0: 'red', 1: 'blue', 2: 'green'}
    for i in range(0, numvars):
        for j in range(0, numvars):
            if i != j:
                for index, type in enumerate(classes):
                    ix = np.where(col == index)
                    ax[j, i].scatter(data[i][ix], data[j][ix],
                                     c=cdict[index], label=type, s=5)
            else:
                ax[j, i].hist(data[i], bins=15,
                              edgecolor='black', linewidth=.8)
            if i == 0:
                ax[j, i].set_ylabel(columns[j], {'size': 8})
                ax[j, i].tick_params(axis='y', labelsize=8)
            else:
                ax[j, i].set_yticklabels([])
                ax[j, i].set_yticks([])
            if j == (numvars - 1):
                ax[j, i].set_xlabel(columns[i], {'size': 8})
                ax[j, i].tick_params(axis='x', labelsize=8)
            else:
                ax[j, i].set_xticklabels([])
                ax[j, i].set_xticks([])
    plt.subplots_adjust(wspace=0, hspace=0)
    fig.suptitle('Pair plot of iris dataset', x=0.55)
    handles, labels = ax[1, 2].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.2, 0.85))
    plt.savefig('task2/task22.png')
    plt.show()


def main():
    """Define main function."""
    # load iris dataset
    irisdata = load_iris()
    columns = ['sepal length (cm)', 'sepal width (cm)',
               'petal length (cm)', 'petal width (cm)']
    irisdata_t = transposeArray(irisdata['data'])
    irisdata_class = irisdata['target']
    generatePairPlots(irisdata_t, irisdata_class, columns)


main()
