# Annalise Sean, CST205

import matplotlib.pyplot as plt
from collections import Counter
from a205_lab14 import filtered_words # farewell neat naming scheme

# count word frequencies
word_counts = Counter(filtered_words)

# get top 5 most common words
top_words = word_counts.most_common(5)
labels, counts = zip(*top_words)

# plot the results
plt.figure(figsize=(8, 5))
plt.bar(labels, counts, color='goldenrod')
plt.title("Top 5 Most Frequent Words in Bee Movie Script")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()