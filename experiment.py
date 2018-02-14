# test

from sklearn import tree # Import the library
# feaatures = characteristics,
features = [[140, 1],[130, 1],[150, 0],[170, 0]]
#features = input
#labels = output
labels = [0, 0, 1, 1]
#crerate classifier
clf = tree.DecisionTreeClassifier()
# training Algorithm is included in the classifier object , called fit
clf = clf.fit(features, labels)

print clf.predict([[150, 0]])


# https://www.youtube.com/watch?v=cKxRvEZd3Mw
