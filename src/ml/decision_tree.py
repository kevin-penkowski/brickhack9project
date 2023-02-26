import numpy as np
from sklearn.tree import DecisionTreeClassifier

def run(x_train, y_train, x_test, y_test, clf):
    train(x_train, y_train, clf) #this is the training step
    print(" predictions: ", predict(x_test, clf)) #this tries out the model on the held out dataset
    print(" actual labels: ", y_test) #this vector is our actual labels
    print(len(y_test))
    print("score = %0.4f" % clf.score(x_test, y_test)) #this compares the predicted to actual classifier and calculates accuracy. Score = (num of test samples correct)/(num of test correct + num of test wrong)
    print()


def train(x_train, y_train, clf):
    #this is the training step
    clf.fit(x_train, y_train)

def predict(test, clf):
    return clf.predict(test)


def create_clf():
    return DecisionTreeClassifier()

def get_training_set():
    features = np.load("./src/ml/mushroom_features.npy")
    labels = np.load("./src/ml/mushroom_labels.npy")
    N = 300
    features_train = features[:N]; features_test = features[N:]
    labels_train = labels[:N]; labels_test = labels[N:]
    return features_train, labels_train

if __name__ == "__main__":
    features = np.load("./src/ml/mushroom_features.npy")
    labels = np.load("./src/ml/mushroom_labels.npy")
    
    # N = 300
    N = 400

    #All experiments have resulted in a score of 1.00 (experiments: 300 train samples with 20 test samples and then 200 test samples; 400 train samples with 100 test samples)

    features_train = features[:N]; features_test = features[N:]
    labels_train = labels[:N]; labels_test = labels[N:]

    print("Running Decision Tree...")
    run(features_train, labels_train, features_test, labels_test, create_clf())