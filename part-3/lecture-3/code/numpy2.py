import numpy as np

def svm_classify(w, b, x):
    return np.dot(w, x) - b > 0

w = [-1.3, 4.555, 7]
b = 9.0
points = [[8.11, 3.42, 11.2], [-4.9, 4.557, 7.08]]
labels = [svm_classify(w, b, p) for p in points]


