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

polyglot_1_indices = df[df['polyglot_1'] == 1].index
ax.scatter(df.loc[polyglot_1_indices, 'x_plot_continuous'], [1] * len(polyglot_1_indices), label='polyglot_1')

polyglot_2_indices = df[df['polyglot_2'] == 1].index
ax.scatter(df.loc[polyglot_2_indices, 'x_plot_continuous'], [2] * len(polyglot_2_indices), label='polyglot_2')

polyglot_3_indices = df[df['polyglot_3'] == 1].index
ax.scatter(df.loc[polyglot_3_indices, 'x_plot_continuous'], [3] * len(polyglot_3_indices), label='polyglot_3')

polyglot_4_indices = df[df['polyglot_4'] == 1].index
ax.scatter(df.loc[polyglot_4_indices, 'x_plot_continuous'], [4] * len(polyglot_4_indices), label='polyglot_4')

polyglot_5_indices = df[df['polyglot_5'] == 1].index
ax.scatter(df.loc[polyglot_5_indices, 'x_plot_continuous'], [5] * len(polyglot_5_indices), label='polyglot_5')

polyglot_6_indices = df[df['polyglot_6'] == 1].index
ax.scatter(df.loc[polyglot_6_indices, 'x_plot_continuous'], [6] * len(polyglot_6_indices), label='polyglot_6')

polyglot_7_indices = df[df['polyglot_7'] == 1].index
ax.scatter(df.loc[polyglot_7_indices, 'x_plot_continuous'], [7] * len(polyglot_7_indices), label='polyglot_7')

polyglot_8_indices = df[df['polyglot_8'] == 1].index
ax.scatter(df.loc[polyglot_8_indices, 'x_plot_continuous'], [8] * len(polyglot_8_indices), label='polyglot_8')


# Add labels and title
plt.xlabel('Test IDs')
#plt.ylabel('Test Feature')
plt.title('Scatter Plot')

# Set x-axis ticks to continuous x_plot values and labels to test_id values
plt.xticks(df['x_plot_continuous'], df['test_id'])

# Set y-axis ticks and labels
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8], ['polyglot_1', 'polyglot_2', 'polyglot_3', 'polyglot_4', 'polyglot_5', 'polyglot_6', 'polyglot_7', 'polyglot_8'])

# Rotate x-axis labels vertically
plt.xticks(rotation=90)
# Add legend
plt.legend()

# Show the plot
plt.show()
