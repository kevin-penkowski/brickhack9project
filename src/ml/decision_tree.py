import numpy as np
from sklearn.tree import DecisionTreeClassifier

def run(x_train, y_train, x_test, y_test, clf):
    clf.fit(x_train, y_train) #this is the training step
    print(" predictions: ", clf.predict(x_test)) #this tries out the model on the held out dataset
    print(" actual labels: ", y_test) #this vector is our actual label
    print("score = %0.4f" % clf.score(x_test, y_test)) #this compares the predicted to actual classifier and calculates accuracy. Score = (num of test samples correct)/(num of test correct + num of test wrong)
    print()

features = np.load("mushroom_features.npy")
labels = np.load("mushroom_labels.npy")

N = 300

features_train = features[:N]; features_test = features[N:]
labels_train = labels[:N]; labels_test = labels[N:]

print("Running Decision Tree...")
run(features_train, labels_train, features_test, labels_test, DecisionTreeClassifier())