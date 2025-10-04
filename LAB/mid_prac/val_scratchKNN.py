#knn

from collections import Counter
import numpy as np

def knn(X_train,y_train,X_test,k=3):
  preds=[]
  for x in X_test:
    dist = np.sqrt(np.sum((X_train-x)**2,axis=1))
    k_idx = np.argsort(dist)[:k]
    k_labels = y_train[k_idx]
    preds.append(Counter(k_labels).most_common(1)[0][0])
  return np.array(preds)

#LOO
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score

loo = LeaveOneOut()
acc_scores = []

for train_idx,test_idx in loo.split(X):
  X_train,X_test = X[train_idx],X[test_idx]
  y_train,y_test = y[train_idx],y[test_idx]
  y_pred = knn(X_train,y_train,X_test,k=3)
  acc = accuracy_score(y_test,y_pred)
  acc_scores.append(acc)

print("avg loo" , np.mean(acc_scores))

#k-fold
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score

kf = KFold(n_splits=3,shuffle=True,random_state=42)
scores = []

for train_idx,test_idx in kf.split(X):
  X_train,X_test = X[train_idx],X[test_idx]
  y_train,y_test = Y[train_idx],y[test_idx]
  pred = knn(X_train,y_train,X_test,k=3)
  accs = accuracy_score(y_test,pred)
  scores.append(accs)

print("fold", scores)
print("avg" ,np.mean(scores))


