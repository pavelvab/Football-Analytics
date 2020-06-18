import matplotlib.pyplot as plt

# Team colors from https://teamcolorcodes.com/nfl-team-color-codes/
# I chose the most pleasant color as primary, not necessarily the actual primary color
team_colors_primary = {"TB": "#D50A0A", "DET": "#0076b6", "TEN": "#0C2340", "BAL": "#241773",
                       "GB": "#FFB612", "MIA": "#FC4C02", "DAL": "#041E42", "BUF": "#00338D",
                       "CLE": "#311D00", "HOU": "#03202f", "WAS": "#FFB612", "LAC": "#0080C6",
                       "CHI": "#c83803", "KC": "#E31837", "NYJ": "#125740", "PHI": "#004C54",
                       "NYG": "#0B2265", "IND": "#002C5F", "ATL": "#000000", "MIN": "#4F2683",
                       "CAR": "#0085CA", "CIN": "#fb4f14", "LA": "#866D4B", "ARI": "#000000",
                       "NE": "#B0B7BC", "SF": "#B3995D", "OAK": "#A5ACAF", "JAX": "#006778",
                       "PIT": "#FFB612", "NO": "#D3BC8D", "DEN": "#FB4F14", "SEA": "#69BE28",
                       }
team_colors_secondary = {"TB": "#FF7900", "DET": "#B0B7BC", "TEN": "#4B92DB", "BAL": "#000000",
                         "GB": "#203731", "MIA": "#008E97", "DAL": "#869397", "BUF": "#C60C30",
                         "CLE": "#ff3c00", "HOU": "#A71930", "WAS": "#773141", "LAC": "#FFC20E",
                         "CHI": "#0B162A", "KC": "#FFB81C", "NYJ": "#000000", "PHI": "#000000",
                         "NYG": "#a71930", "IND": "#A2AAAD", "ATL": "#a71930", "MIN": "#FFC62F",
                         "CAR": "#BFC0BF", "CIN": "#000000", "LA": "#002244", "ARI": "#97233F",
                         "NE": "#002244", "SF": "#AA0000", "OAK": "#000000", "JAX": "#9F792C",
                         "PIT": "#101820", "NO": "#101820", "DEN": "#002244", "SEA": "#002244",
                         }


# Create some dummy data
Superbowl_wins = {"NYG": 4, "DAL": 5, "WAS": 3, "PHI": 3}
Superbowl_appearances = {"NYG": 5, "DAL": 8, "WAS": 5, "PHI": 1}
NFL_wins_fake = {"NYG": 700, "DAL": 500, "WAS": 300, "PHI": 100}

# Plot the data.  Each point is plotted individually in a loop
mean_sb_wins = 0
mean_sb_appearances = 0
count = 0
for team in Superbowl_wins:

    # Set the colors
    color1 = team_colors_primary[team]
    color2 = team_colors_secondary[team]

    # Assign data to shorter variables
    A = Superbowl_appearances[team]
    B = Superbowl_wins[team]
    S = NFL_wins_fake[team]

    # s sets the bubble size
    # alpha sets the bubble transparency
    plt.scatter(A, B, s=S, alpha=0.8, color=color1, edgecolors=color2)

    # Annotate each bubble
    plt.annotate(team,  # this is the text
                 (A, B),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 15),  # distance from text to points (x,y)
                 ha='center',
                 fontsize=7)  # horizontal alignment can be left, right or center

    # Keep track of data to compute means later
    mean_sb_wins += Superbowl_wins[team]
    mean_sb_appearances += Superbowl_appearances[team]
    count += 1

# Plot lines to show means
mean_sb_wins /= count
mean_sb_appearances /= count
plt.axvline(mean_sb_wins, color='r', linestyle='--', linewidth=1, alpha=0.8, zorder=0)
plt.axhline(mean_sb_appearances, color='r', linestyle='--', linewidth=1, alpha=0.8, zorder=0)

# Create a grid
plt.grid(color='k', linestyle='--', linewidth=1, alpha=0.15)

# Set x and y limits (optional)
xstart = 0
xstop = 10
ystart = 0
ystop = 6
plt.xlim(xstart, xstop)
plt.ylim(ystart, ystop)

# Set titles and axis labels
plt.suptitle('NFCE Superbowl appearances and wins by team', fontsize=20)
plt.title('Bubble size is irrelevant in this case', fontsize=16)
plt.ylabel('Superbowl wins', fontsize=14)
plt.xlabel('Superbowl appearances', fontsize=14)

# Add an image to the background
img = plt.imread("./Emanning.jpeg")
ext = [xstart, xstop, ystart, ystop]
plt.imshow(img, zorder=0, extent=ext, alpha=0.3)
aspect=img.shape[0]/float(img.shape[1])*((ext[1]-ext[0])/(ext[3]-ext[2]))
plt.gca().set_aspect(aspect)

# Show the plot
plt.show()
