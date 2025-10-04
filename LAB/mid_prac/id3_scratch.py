from math import log2

target = df['target']
def entropy(series):
  probs = series.value_counts(normalize=True)
  return -sum(p * log2(p) for p in probs if p > 0)

def infor_gain(df,attribute,target):
  total_entropy = entropy(df[target])
  values = df[attribute].unique()
  for val in values:
    subset = df[df[attribute]==val]
    weight = len(subset)/len(df)
    subset_ent = entropy(subset[target])
    weighted_ent += weight*subset_ent

attribute = [col for col in df.columns if col not in ['target']]
ig_results={}

print("info gain:")
for attr in attribute:
  ig = infor_gain(df,attribute,target)
  ig_results[attr] = ig
  print(f"{attr}: {ig:.3f}")

best_attr = max(ig_results,key=ig_results.get)
print(best_attr)

def id3(df, target, attributes, parent_class=None):
    # Base cases
    
    # 1️⃣ If all samples have the same class → return that class
    if len(df[target].unique()) == 1:
        return df[target].iloc[0]
    
    # 2️⃣ If dataset is empty → return the parent node's majority class
    elif len(df) == 0:
        return parent_class
    
    # 3️⃣ If no attributes left → return majority class of current node
    elif len(attributes) == 0:
        return df[target].mode()[0]
    
    # 4️⃣ Otherwise, pick the best attribute
    else:
        parent_class = df[target].mode()[0]
        ig_values = {attr: infor_gain(df, attr, target) for attr in attributes}
        best_attr = max(ig_values, key=ig_values.get)
        
        # Initialize the tree with this attribute
        tree = {best_attr: {}}
        
        # For each value in the best attribute, grow a branch
        for val in df[best_attr].unique():
            subset = df[df[best_attr] == val]
            
            # Remove the used attribute for the next recursion
            new_attributes = [a for a in attributes if a != best_attr]
            
            subtree = id3(subset, target, new_attributes, parent_class)
            
            # Connect the branch
            tree[best_attr][val] = subtree
        
        return tree
