"""Spring 2019 COMSW 4995: Applied Machine Learning.

UNI: nl2643
Homework 1 Task 2.1

Replicates plot 'Number of people who drowned by falling into a pool correlates
with Films Nicholas Cage appears in' from
www.tylervigen.com/spurious-correlations

"""

import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from scipy.interpolate import spline


def getNicholasCageMovies():
    """Fetch number of movies Nicholas Cage appears in in each year."""
    # File was retrieved from https://www.imdb.com/name/nm0000115/
    # on Jan 30 2019
    file = 'task2/NicolasCageInfo.txt'

    with open(file, "r") as file:
        text = BeautifulSoup(file, "html.parser")
        films = text.find('div', class_='filmo-category-section')
        years = films.find_all('span', class_='year_column')

    movieno = {}
    for tag in years:
        yr = tag.contents[0][2:6]
        if yr == "\n":
            pass
        elif yr in movieno:
            movieno[yr] += 1
        else:
            movieno[yr] = 1

    return movieno


def getJoinedDataFrame():
    """Extract data and obtain DataFrame for plotting."""
    # initialize movie df
    moviedata = getNicholasCageMovies()
    moviedf = pd.DataFrame(moviedata.items(),
                           columns=['Year', 'Movie Count'])
    moviedf['Year'] = pd.to_numeric(moviedf['Year'])
    moviedf = moviedf.set_index('Year')

    # Initialize drowning df
    # Accessed at http://wonder.cdc.gov/cmf-icd10-archive2009.html
    # on Jan 30, 2019 5:19:09 PM"
    drowningdf = pd.read_csv('task2/PoolDrowning.txt', sep='\t')
    drowningdf = drowningdf[['Year', 'Deaths']]
    drowningdf = drowningdf.set_index('Year')

    # join both dataframes
    df = drowningdf.join(moviedf)
    return df


def main():
    """Define main function."""
    df = getJoinedDataFrame()

    xnew = np.linspace(1999, 2009, 200)
    splineDeaths = spline(df.index.values, df.Deaths.values, xnew)
    splineMovies = spline(df.index.values, df['Movie Count'].values, xnew)

    # generate plot
    plt.figure(figsize=(15, 4))

    plt.title('Number of people who drowned by falling into a pool\n'
              'correlates with\nFilms Nicolas Cage appeared in\n'
              'Correlation: 66.6% (r=0.666004)',
              fontsize=12)

    ax1 = plt.gca()
    ax1.plot(df.index.values, df['Deaths'], 'ro')
    line1, = ax1.plot(xnew, splineDeaths, 'r-')
    plt.xticks(np.arange(1999, 2010, 1))
    ax1.set_ylabel('Swimming pool drownings')
    ax1.set_ylim(80, 140)
    ax1.set_yticks(np.arange(80, 140, 20))
    ax1.yaxis.grid(True)

    tempax = ax1.twiny()  # tempx to obtain second x axis on top
    ax2 = ax1.twinx()  # actual axis on which to plot Movie count on

    ax2.plot(df.index.values, df['Movie Count'], 'ko')
    line2, = ax2.plot(xnew, splineMovies, 'k-')
    ax2.set_yticks(np.arange(0, 6, 2))
    ax2.set_ylim(0, 6)
    ax2.set_ylabel('Nicholas Cage', rotation=-90, labelpad=12)
    ax2.legend((line1, line2), ('Swimming pool drownings', 'Nicholas Cage'))

    tempax.set_xticks(ax1.get_xticks())
    tempax.set_xbound(ax1.get_xbound())

    plt.tight_layout()
    plt.savefig('task2/task21.png')
    plt.show()

    return


main()
