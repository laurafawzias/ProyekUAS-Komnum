#Laura Fawzia Sambowo - 2306260145
#Proyek UAS Komnum - Adaptive Noise Cancellation Using Least-Squares Regression

import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("output_signal.txt", sep="\t", skiprows=1, names=["index", "desired", "output", "error"])

# caption
caption = "*caption: desired = target signal, output = LMS output, error = desired - output"

# style setup
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.linestyle'] = '-'
plt.rcParams['grid.linewidth'] = 0.5
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['axes.facecolor'] = 'white'

# plot 1: desired vs output
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(df["index"], df["desired"], label="Desired", color="royalblue", linewidth=1)
ax.plot(df["index"], df["output"], label="Output", color="forestgreen", linewidth=1)
ax.set_xlabel("Sample Index", fontsize=11)
ax.set_ylabel("Signal Value", fontsize=11)
ax.set_title("Desired vs Output Signal", fontsize=13, pad=8)
ax.legend(loc="upper right", fontsize=9, frameon=True)
ax.grid(True, linestyle='-', linewidth=0.8, alpha=0.4, color='gray')
ax.set_axisbelow(True)
plt.tight_layout(rect=[0, 0.05, 1, 0.93])
plt.figtext(0.5, 0.05, caption, wrap=True, ha='center', fontsize=8, color='dimgray', style='italic')
plt.savefig("../Figures/desired_output.png", dpi=400, bbox_inches='tight')
plt.close()

# plot 2: output zoomed
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(df["index"], df["output"], label="Output Signal (Scaled View)", color="forestgreen", linewidth=1)
ax.set_xlabel("Sample Index", fontsize=11)
ax.set_ylabel("Output Signal Value", fontsize=11)
ax.set_title("Output Signal (Zoomed In)", fontsize=13, pad=8)
ax.set_ylim(-0.25, 0.45)
ax.legend(loc="lower left", fontsize=9, frameon=True)
ax.grid(True, linestyle='-', linewidth=0.8, alpha=0.4, color='gray')
ax.set_axisbelow(True)
plt.tight_layout(rect=[0, 0.05, 1, 0.93])
plt.figtext(0.5, 0.05, caption, wrap=True, ha='center', fontsize=8, color='dimgray', style='italic')
plt.savefig("../Figures/output_zoom.png", dpi=400, bbox_inches='tight')
plt.close()

# plot 3: error
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(df["index"], df["error"], label="Error Signal", color="crimson", linewidth=1)
ax.set_xlabel("Sample Index", fontsize=11)
ax.set_ylabel("Error Value", fontsize=11)
ax.set_title("Error Signal", fontsize=13, pad=8)
ax.legend(loc="upper right", fontsize=9, frameon=True)
ax.grid(True, linestyle='-', linewidth=0.8, alpha=0.4, color='gray')
ax.set_axisbelow(True)
plt.tight_layout(rect=[0, 0.05, 1, 0.93])
plt.figtext(0.5, 0.05, caption, wrap=True, ha='center', fontsize=8, color='dimgray', style='italic')
plt.savefig("../Figures/error.png", dpi=400, bbox_inches='tight')
plt.close()