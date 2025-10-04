import numpy as np
from collections import Counter

def knn(X_train,y_train,X_test,k=3):
  preds=[]
  for x in X_test:
    dist = np.sqrt(np.sum((X_train-x)**2,axis=1))
    k_idx = np.argsort(dist)[:k]
    k_labels = y_train[k_idx]
    preds.append(Counter(k_labels).most_common(1)[0][0])
  return np.array(preds)

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X = df.drop('target',axis=1)
y = df['target']


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

y_pred = knn(X_train,y_train,X_test,k=5)
print(f"acc: {accuracy_score(y_test,y_pred)}")
