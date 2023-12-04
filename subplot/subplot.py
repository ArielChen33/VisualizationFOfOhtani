import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("yearChanges(sub).csv")
# print(df.ExitVelocity)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 5))

# Plot Exit Velocity
plt.subplot(2, 3, 1)
plt.plot(df.Year, df.ExitVelocity, linewidth=2, color="red", marker="o", markersize=6, label="Exit Velocity")
plt.title('Exit Velocity')

# Plot xBA
plt.subplot(2, 3, 2)
plt.plot(df.Year, df.xBA, linewidth=2, color="blue", marker="o", markersize=6, label="xBA")
plt.title('xBA')


# Plot BA
plt.subplot(2, 3, 3)
plt.plot(df.Year, df.BA, linewidth=2, color="skyblue", marker="o", markersize=6, label="xBA")
plt.title('BA')

# Plot xwOBA
plt.subplot(2, 3, 4)
plt.plot(df.Year, df.xwOBA, linewidth=2, color="green", marker="o", markersize=6, label="xBA")
plt.title('xwOBA')

# Plot wOBA
plt.subplot(2, 3, 5)
plt.plot(df.Year, df.wOBA, linewidth=2, color="lightgreen", marker="o", markersize=6, label="xBA")
plt.title('wOBA')

# Plot xSLG
plt.subplot(2, 3, 6)
plt.plot(df.Year, df.xSLG, linewidth=2, color="brown", marker="o", markersize=6, label="xBA")
plt.title('xSLG')

# # Plot SLG
# plt.subplot(3, 3, 7)
# plt.plot(df.Year, df.SLG, linewidth=2, color="grey", marker="o", markersize=6, label="xBA")
# plt.title('SLG')

# Adjust layout for better spacing
plt.tight_layout()

plt.title("Ohtani's batting performance in MLB career", fontsize=22, color="black", x=2.2, y=0,)
# plt.title("made in Python", loc='right', fontsize=10, color='grey', style='italic')

# Show the plots
plt.show()
