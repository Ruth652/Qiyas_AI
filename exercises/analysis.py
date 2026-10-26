import pandas as pd
from collections import Counter

df = pd.read_csv("ethiopian_news.csv")

print("Total headlines:", len(df))

longest = max(df["title"], key=len)
print("Longest headline:")
print(longest)

shortest = min(df["title"], key=len)
print("Shortest headline:")
print(shortest)

average_length = df["title"].str.len().mean()
print("Average headline length:", average_length)

words = []

for title in df["title"]:
    words.extend(title.lower().split())

common_words = Counter(words)

print("\nTop 10 Common Words")

for word, count in common_words.most_common(10):
    print(word, count)

