#########################
# Week 1: Lab, Plotting #
#########################

##########
# Plot 1 #
##########
import matplotlib.pyplot as plt
import numpy as np
plt.figure()

# creating lists of data
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# creating cuts spacing bars on axis
pos = np.arange(len(languages))

# height of bars data in a list
popularity = [56, 39, 34, 34, 29]

# plotting
plt.bar(pos, popularity, align='center')
# positioning
plt.xticks(pos, languages)

# labels
plt.ylabel('% Popularity')
plt.title('Top 5 Languages for Math & Data \nby % Popularity on Stack Overflow')
plt.show()

##########
# Plot 2 #
##########
# refining plot 1
import matplotlib.pyplot as plt
import numpy as np
plt.figure()

# creating lists of data
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# creating cuts spacing bars on axis
pos = np.arange(len(languages))

# height of bars data in a list
popularity = [56, 39, 34, 34, 29]

# plotting: altering bar color
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')
# setting one contrasting color
bars[0].set_color('#1F77B4')
# positioning, softening labels
plt.xticks(pos, languages, alpha=0.8)
# removing ylabels since bars are directly labeled
# plt.ylabel('% Popularity', alpha=0.8)
plt.title('Top 5 Languages for Math & Data \nby % Popularity on Stack Overflow', alpha=0.8)

# removing all ticks
plt.tick_params(top='off', bottom='off', left='off', right='off',
                labelleft='off', labelbottom='on')

# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# direct label each bar with Y axis values
for bar in bars:
    height = bar.get_height()
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(height)) + '%',
    ha='center', color='w', fontsize=11)

plt.show()




















# plt.show() to display plots
