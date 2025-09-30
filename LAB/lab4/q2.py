import pandas as pd
import numpy as np
from math import log2

df = pd.read_csv("/content/task2.csv")
target = "CLASS (Yes or No)" 

def entropy(series):
    probs = series.value_counts(normalize=True)
    return -sum(p * log2(p) for p in probs if p > 0)

total_entropy = entropy(df[target])
print(f"Total Entropy: {total_entropy:.3f}\n")

def information_gain(df, attribute, target):
    total_entropy = entropy(df[target])
    values = df[attribute].unique()  

    weighted_entropy = 0
    for val in values:
        subset = df[df[attribute] == val]
        weight = len(subset) / len(df)
        subset_entropy = entropy(subset[target])
        weighted_entropy += weight * subset_entropy  

    ig = total_entropy - weighted_entropy
    return ig


attributes = [col for col in df.columns if col not in [target,"ID"]]
ig_results = {}

print("Information Gain for each attribute:\n")
for attr in attributes:
    ig = information_gain(df, attr, target)
    ig_results[attr] = ig
    print(f"{attr}: {ig:.3f}")

best_attr = max(ig_results, key=ig_results.get)
print("\n✅ Best root node (highest IG):", best_attr)

