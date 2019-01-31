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
from bs4 import BeautifulSoup


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
    moviedf = pd.DataFrame(moviedata.items(), columns=['Year', 'Movie Count'])
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

    # generate plot
    df.index = pd.to_datetime(df.index, format='%Y')
    plt.figure()
    plt.suptitle('Number of people who drowned by falling into a pool',
                 fontsize=12)
    plt.title('correlates with Films Nicolas Cage appeared in', fontsize=10)
    ax1 = plt.gca()
    line1, = ax1.plot(df.index.values, df['Deaths'], 'ko-')
    ax1.xaxis.set_major_locator(dates.YearLocator(1))
    ax1.xaxis.set_minor_locator(dates.YearLocator(1, month=7, day=2))
    ax1.xaxis.set_major_formatter(dates.DateFormatter('%Y'))
    plt.tick_params(
        axis='x',
        which='major',
        bottom=False,
        labelbottom=True
    )
    ax1.set_ylabel('Swimming pool drownings')
    ax2 = ax1.twinx()
    line2, = ax2.plot(df.index.values, df['Movie Count'], '-ro')
    ax2.set_ylabel('NicholasCage')
    ax2.legend((line1, line2), ('Swimming pool drownings', 'Nicholas Cage'))
    plt.show()

    plt.savefig('task2/task21.png')

    return


main()
