import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("yearChanges(rate).csv")
# print(df.head)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize = (12, 4))
ax.plot(df.Year, df.HardHit, linewidth = 2, color = "red", marker = "*", markersize = 6, label = "Exit Velocity")
ax.plot(df.Year, df.SweetSpot, linewidth = 2, color = "orange", marker = "d", markersize = 6, label = "Exit Velocity")
ax.plot(df.Year, df.K, linewidth = 2, color = "yellow", marker = "s", markersize = 6, label = "Exit Velocity")
ax.plot(df.Year, df.BB, linewidth = 2, color = "green", marker = "p", markersize = 6, label = "Exit Velocity")
ax.plot(df.Year, df.Swing, linewidth = 2, color = "skyblue", marker = "P", markersize = 6, label = "Exit Velocity")
ax.plot(df.Year, df.Whiff, linewidth = 2, color = "darkblue", marker = "h", markersize = 6, label = "Exit Velocity")
# ax.plot(df.Year, df.InZone, linewidth = 2, color = "purple", marker = "o", markersize = 6, label = "Exit Velocity")
# ax.plot(df.Year, df.OutofZone, linewidth = 2, color = "black", marker = "o", markersize = 6, label = "Exit Velocity")
# ax.plot(df.Year, df.OutofZoneSwing, linewidth = 2, color = "brown", marker = "o", markersize = 6, label = "Exit Velocity")
# ax.plot(df.Year, df.FirstPitchSwing, linewidth = 2, color = "grey", marker = "o", markersize = 6, label = "Exit Velocity")
# ax.plot(df.Year, df.FirstPitchStrike, linewidth = 2, color = "pink", marker = "o", markersize = 6, label = "Exit Velocity")

plt.title("Ohtani's batting performance in MLB career", fontsize=22, color="black", loc="left")
plt.title("made in Python", loc='right', fontsize=10, color='grey', style='italic')
plt.xlabel("year")
plt.ylabel("rate(%)")
plt.legend(["HardHit%", "SweetSpot%", "K%", "BB%", "Swing%", "Whiff%"], loc = "lower left")
										
plt.show()
