#%%
import matplotlib.pyplot as plt
import numpy as np
import csv

FILE_NAME = "NMTR1.csv"

#################### HELPER FUNCTION ####################
def processData(pt):
    """ Converts each datapoint from str to 2-decimal float """
    return round(float('0' if pt == "n/a" else pt), 2)

#################### READING/PROCESSING THE CSV ####################

with open(FILE_NAME, 'r') as f:
    """ Reads raw CSV data """
    data = list(csv.reader(f))

# Stores CSV data in dictionary called "people" 
#   - EXAMPLE: {"name":[0.0,2.1,...], "name2":[1.2,1.2,...]}
# data[1:] ignores header line; only parses relevant data
# person[0] is each person's name
# [dat(i) for i in person[1:]] is each person's excel data (B-N)
people = {}
for person in data[1:]:
    people[person[0]] = [processData(i) for i in person[1:]]
    
#################### PARSING THE CSV ####################
names = list(people.keys()) # All names from Column A
before = []
during = []
after = []
B = 0
D = 2
F = 4

# Parses CSV data from columns B, D, & F to seperate list
for name in names:
    person_data = people.get(name)
    before.append(person_data[B])
    during.append(person_data[D])
    after.append(person_data[F])

#################### PLOTTING ####################

# Adjust Plot Parameters Here
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
