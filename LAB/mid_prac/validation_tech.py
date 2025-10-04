# train-test-split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# k-fold
from sklearn.model_selection import KFold,cross_val_score
from sklearn.neighbors import KNeighborsClassifier

kf = KFold(n_splits=5,shuffle=True,random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn,X,y,cv=kf)

# leave one out
from sklearn.model_selection import LeaveOneOut
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

loo = LeaveOneOut()
model = KNeighborsClassifier(n_neighbors=5)
scores = []

for train_idx,test_idx in loo.split(X):
  X_train,X_test = X[train_idx],X[test_idx]
  y_train,ytest = y[train_idx],y[test_idx]
  model.fit(X_train,y_train)
  y_pred = model.predict(X_test)
  scores.append(accuracy_score(y_test,y_pred))
