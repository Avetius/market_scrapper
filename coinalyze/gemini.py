import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [38, 709, 700, 46, 712, 67, 708, 705, 709]

# Define window sizes
window_sizes = [9] # , 50, 100

# Create heatmap
fig, ax = plt.subplots()

for window_size in window_sizes:
    # Create frequency table for the window
    counts, bins = np.histogram(data, bins=np.arange(min(data), max(data) + 1, window_size))

    # Normalize counts for better visualization
    counts = counts / np.sum(counts)

    # Create heatmap for the window
    ax.imshow(
        counts[:, np.newaxis],
        extent=[bins[0], bins[-1], 0, 1],
        aspect="auto",
        cmap="hot",
        alpha=0.7,
        label=f"Window size: {window_size}",
    )

# Add labels and title
ax.set_xlabel("Number")
ax.set_ylabel("Frequency (normalized)")
ax.set_title("Heatmap of number frequencies (windowed)")
    
# Add legend
ax.legend()

# Show the plot
plt.show()