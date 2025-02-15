import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

data = {
    'Subject': ['Math', 'Physics', 'Chemistry', 'Biology', 'Computer Science'],
    'Score': [random.randint(50, 100) for _ in range(5)]
}

df = pd.DataFrame(data)
print(df)

sns.set(style="whitegrid")

# different colors for each bar
colors = sns.color_palette('husl', len(df))
bar_plot = sns.barplot(x='Subject', y='Score', data=df, palette=colors)

# Add annotations on top of each bar
for i in range(len(df)):
    bar_plot.text(i, df['Score'][i] + 1, df['Score'][i], ha='center', va='bottom')

# Add title, axis labels, and grid
plt.title('Random Scores of Five Subjects')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.grid(True)

plt.show()
