import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bxss.csv")

df = df.dropna(subset=['test_id']).reset_index(drop=True)

df['x_plot_continuous'] = range(1, len(df) + 1)

fig, ax = plt.subplots()

counts = {}

for i in range(1, 9):
    column_name = f'polyglot_{i}'
    polyglot_indices = df[df[column_name] == 1].index
    ax.scatter(df.loc[polyglot_indices, 'x_plot_continuous'], [i] * len(polyglot_indices), label=f'{column_name} ({df[column_name].sum()})')
    counts[column_name] = df[column_name].sum()

any_polyglot_indices = df[df[[f'polyglot_{i}' for i in range(1, 9)]].sum(axis=1) > 0].index
any_polyglot_count = len(any_polyglot_indices)
ax.scatter(df.loc[any_polyglot_indices, 'x_plot_continuous'], [0.5] * len(any_polyglot_indices), color='black', label=f'Any polyglot ({any_polyglot_count})')

plt.xlabel('Test IDs')
plt.title('Polyglot Analysis Plot')

plt.xticks(df['x_plot_continuous'], df['test_id'])

plt.yticks([0.5] + list(range(1, 9)), [f'Combined ({any_polyglot_count})'] + [f'polyglot_{i}' for i in range(1, 9)], fontsize=15)

plt.xticks(rotation=90)

plt.legend()

plt.show()
