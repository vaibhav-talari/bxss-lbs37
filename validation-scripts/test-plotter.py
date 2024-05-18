import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("bxss.csv")

# Filter out rows where test_id is None
df = df.dropna(subset=['test_id']).reset_index(drop=True)

# Create a new continuous x_plot array after filtering
df['x_plot_continuous'] = range(1, len(df) + 1)

# Initialize a figure and axis with a specified size
fig, ax = plt.subplots()

# Define a dictionary to store counts
counts = {}

# Scatter plots for each polyglot
for i in range(1, 9):
    column_name = f'polyglot_{i}'
    polyglot_indices = df[df[column_name] == 1].index
    ax.scatter(df.loc[polyglot_indices, 'x_plot_continuous'], [i] * len(polyglot_indices), label=f'{column_name} ({df[column_name].sum()})')
    # Count the number of points plotted for each polyglot_x
    counts[column_name] = df[column_name].sum()

# Create an additional line at y=0.5 if any polyglot_x is 1 for a given x_plot_continuous
any_polyglot_indices = df[df[[f'polyglot_{i}' for i in range(1, 9)]].sum(axis=1) > 0].index
any_polyglot_count = len(any_polyglot_indices)
ax.scatter(df.loc[any_polyglot_indices, 'x_plot_continuous'], [0.5] * len(any_polyglot_indices), color='black', label=f'Any polyglot ({any_polyglot_count})')

# Add labels and title
plt.xlabel('Test IDs')
plt.title('Polyglot Analysis Plot')

# Set x-axis ticks to continuous x_plot values and labels to test_id values
plt.xticks(df['x_plot_continuous'], df['test_id'])

# Set y-axis ticks and labels, including the new 'Any polyglot' line
plt.yticks([0.5] + list(range(1, 9)), [f'Ultimate Polyglot ({any_polyglot_count})'] + [f'polyglot_{i}' for i in range(1, 9)], fontsize=15)

# Rotate x-axis labels vertically
plt.xticks(rotation=90)

# Add legend
plt.legend()

# Show the plot
plt.show()
