#%%
import matplotlib.pyplot as plt
import numpy as np
import csv

FILE_NAME = "NMTR1.csv"
B = 0
D = 2
F = 4

#################### SETUP FUNCTIONS (PARSE CSV) ####################
def conv(pt):
    """ Converts each datapoint from str to 2-decimal float 
    Returns: 
        float: number in data, or 0 if pt is "n/a"
    """
    return round(float('0' if pt == "n/a" else pt), 2)

def readCSV():
    """ Reads raw CSV data 
    Returns:
        list[str]: list of strings representing each row of CSV
    """
    with open(FILE_NAME, 'r') as f:
        return list(csv.reader(f))

def processCSV():
    """  For each CSV row, store B-F column corresponding to name in dictionary
    Returns:
        people (dictionary{str:float}): list of columns B-F correspoding to name
    """
    people = {}
    data = readCSV()
    for row in data[1:]:
        people[row[0]] = [conv(i) for i in row[1:6]]
    return people

def parseCSV():
    """ Parses CSV data
    Returns:
        dataPts (List[list[float]]): list containing list of B, D, F columns in order
        names (list[str]): list of names in order
    """
    dataPts = []
    people = processCSV()
    names = list(people.keys()) # list of all names (column A)

    # For each name, store column B, D, & F in "dataPts" 
    for name in names:
        dat = people.get(name)
        dataPts.append([dat[B], dat[D], dat[F]])
    
    return dataPts, names

def setup():
    """
    PROGRAM FLOW ON SETUP:
        1) Calling parseCSV() -> calls processCSV() -> calls readCSV().
            Once the raw CSV is read in readCSV(), it sends the raw 
            data to processCSV() which grabs & stores columns B-F 
            sorted by name, then sends that data to parseCSV, which 
            grabs only columns B, D, & F, & returns a list of those 
            data points, & the list of names to be used in plotting.
        2) Line 2 below is setting each variable to the correct column. 
            - before = col B, during = col D, after = col F
    Returns:
        before (list[float]): data points from column B
        during (list[float]): data points from column D
        after (list[float]): data points from column F
        names (list[str]): list of names in CSV file
    """
    dataPts, names = parseCSV() # 1
    before, during, after = map(list, zip(*dataPts)) # 2
    return before, during, after, names
    
#################### SETUP ####################

# Calls all necessary functions to read & parse CSV for plotting
before, during, after, names = setup()

#################### PLOTTING ####################

""" Adjust Plot Parameters Here """
FIG_WIDTH = 20 # Width of Diagram
FIG_HEIGHT = 10 # Height of Diagram
BAR_WIDTH = 0.30
LEGEND_SIZE = 20 
LEGEND_LOC = 2 # Location of legend (2 is upper left)
XLABEL = "People"
YLABEL = "Seconds"
TITLE = "10M Walk Test Normal"
FONT_SIZE = 15 # Font Size of X/Y-Label, Title, LEGEND, & X-ticks

# Plotting
plt.figure(figsize=(FIG_WIDTH, FIG_HEIGHT))

bar1 = np.arange(len(names))
bar2 = [i+BAR_WIDTH for i in bar1]
bar3 = [i+BAR_WIDTH for i in bar2]

plt.bar(bar1, before, BAR_WIDTH, label="Before")
plt.bar(bar2, during, BAR_WIDTH, label="During")
plt.bar(bar3, after, BAR_WIDTH, label="after")

plt.xlabel(XLABEL, fontsize=FONT_SIZE)
plt.ylabel(YLABEL, fontsize=FONT_SIZE)
plt.xticks(bar2, names, fontsize=FONT_SIZE)

plt.title(TITLE, fontsize=FONT_SIZE)
plt.legend(loc=LEGEND_LOC, prop={"size":LEGEND_SIZE})

plt.show()

# %%
