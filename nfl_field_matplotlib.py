import matplotlib.pyplot as plt
import pylab as pl

# Create figure
fig, ax = pl.subplots()

# Set field dimensions
plt.xlim(0, 120)  # Field length including endzones
plt.ylim(0, 53.3)  # field width

# Set field color green
ax.set_facecolor('#79af75')
ax.set_alpha(0.5)

# Print lines
for i in range(0, 120, 10):
    plt.axvline(i, color='white', linewidth=3, alpha=0.4, zorder=1)
    if i == 10 or i == 110:  # Make endzone lines
        plt.axvline(i, color='white', linewidth=5, alpha=0.4, zorder=1)

# Paint numbers
yds_from_sideline = 12
for i in range(10, 50, 10):
    plt.text(i+10, 53.3-yds_from_sideline, str(i), color='white', fontsize=20, verticalalignment='bottom', horizontalalignment='center', rotation=180)
    plt.text(110-i, 53.3-yds_from_sideline,  str(i), color='white', fontsize=20, verticalalignment='bottom', horizontalalignment='center', rotation=180)

    plt.text(i+10, yds_from_sideline, str(i), color='white', fontsize=20, verticalalignment='bottom', horizontalalignment='center')
    plt.text(110-i, yds_from_sideline, str(i), color='white', fontsize=20, verticalalignment='bottom', horizontalalignment='center')

# Paint 50 yard line numbers
plt.text(60, 53.3-yds_from_sideline, str(50), color='white', fontsize=20, verticalalignment='bottom', horizontalalignment='center', rotation=180)
plt.text(60, yds_from_sideline, str(50), color='white', fontsize=20, verticalalignment='bottom', horizontalalignment='center')

# Print something in the endzones
GiantsColor = "#0B2265"
CowboysColor = "#041E42"
plt.text(5, 26.5, 'GIANTS', color=GiantsColor, fontsize=30, verticalalignment='center', horizontalalignment='center', rotation=90)
plt.text(115, 26.5, 'COWBOYS', color=CowboysColor, fontsize=30, verticalalignment='center', horizontalalignment='center', rotation=270)

# Just showing how to set titles and labels
plt.suptitle('NFL football field', fontsize=20)
plt.title('The gridiron', fontsize=14)
plt.ylabel('Field width', fontsize=12)
plt.xlabel('Field length', fontsize=12)

# Fix the aspect ratio (optional)
plt.gca().set_aspect(1)

# Display the figure
plt.show()
