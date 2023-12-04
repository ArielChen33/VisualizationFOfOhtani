import pandas as pd
import numpy as np
import imageio as iio
# from urllib.request import urlopen
from PIL import Image
# import cv2

from scipy import stats
import math
# import mplsoccer
from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt

df = pd.read_csv("percentile_rankings.csv")
df = df.dropna()

# read an image 
img = iio.imread("shohei4.png")
# URL = "https://i.postimg.cc/Wb7mqmwL/11.jpg"
# img = Image.open(urlopen(URL))
# img = cv2.imread("11.jpg", cv2.IMREAD_UNCHANGED)
# image = Image.open("shohei3.jpg")

# print(df.head())
print(df.shape)
params = list(df.columns)
params = params[3:]
player = df.loc[df["player_name"] == "Shohei Ohtani"].reset_index()
player = list(player.loc[0])
player = player[4:]
values = [int(x) for x in player]

# value = []
# for x in range(len(params)):
#     value.append(math.floor(stats.percentileofscore(df[params[x]], player[x])))
# print(len(params))

# color of the slices
slice_colors = ["#f75454"] * 11 + ["#1965fc"] * 2

# instantiate PyPizza class
baker = PyPizza(
    params=params,                  # list of parameters
    straight_line_color="white",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_lw=0,               # linewidth of last circle
    other_circle_lw=0,              # linewidth for other circles
    # other_circle_ls="-."            # linestyle for other circles
)

# plot pizza
fig, ax = baker.make_pizza(
    values,                     # list of values
    figsize=(10, 10),             # adjust figsize according to your need
    # color_blank_space=["#C5C5C5"]*len(params),   # use same color to fill blank space

    color_blank_space="same",        # use same color to fill blank space
    slice_colors=slice_colors,       # color for individual slices
    # value_colors=text_colors,        # color for the value-text
    value_bck_colors=slice_colors,   # color for the blank spaces

    blank_alpha=0.4,            # alpha for blank-space colors
    kwargs_slices=dict(
        # facecolor="#f75454", 
        edgecolor="white",
        zorder=2, linewidth=1
    ),                          # values to be used when plotting slices
    kwargs_params=dict(
        color="#000000", fontsize=12,
        va="center"
    ),                          # values to be used when adding parameter
    kwargs_values=dict(
        color="white", fontsize=12,
        zorder=3,
        bbox=dict(
            edgecolor="white", facecolor="red",
            boxstyle="round,pad=0.2", lw=1
        )
    )                           # values to be used when adding parameter-values
)
# add title
fig.text(
    0.515, 0.97, "Shohei Ohtani's batting performance in 2023", size=18,
    ha="center", color="#000000"
)

# add subtitle
fig.text(
    # 0.515, 0.942,
    0.515, 0.93,
    "Percentile Rankings in MLB all teams' players",
    color = "grey",
    size=15,
    ha="center"
)

# add text
fig.text(
    0.14, 0.9, 
    "Basic Stats         Statcast", size=14,
    color="#000000"
)

# add rectangles 
fig.patches.extend([
    plt.Rectangle(
        (0.11, 0.9), 0.025, 0.021, fill=True, color="#1965fc",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.262, 0.9), 0.025, 0.021, fill=True, color="#f75454",
        transform=fig.transFigure, figure=fig
    )
])

# add image
ax_image = add_image(
    img, fig, left=0.44, bottom=0.435, width=0.2, height=0.18
    # img, fig, left=0.4478, bottom=0.4315, width=0.13, height=0.127
)   # these values might differ when you are plotting 0.13 X 0.127


plt.show()