from mnist import MNIST
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from PIL import Image, ImageDraw

print("Loading dataset...")
mndata = MNIST("./data/")
images, labels = mndata.load_training()

clf = KNeighborsClassifier()

# Train on the first 10000 images:
train_x = images[:10000]
train_y = labels[:10000]

print("Train model")
clf.fit(train_x, train_y)

# Test on the next 100 images:
test_x = images[10000:10100]
expected = labels[10000:10100].tolist()

print("Compute predictions")
predicted = clf.predict(test_x)

for i, image in enumerate(test_x):
    output = Image.new("L", (28, 28))
    output.putdata(image)
    output.save("./output/output_%d.png" % predicted[i])

#print("Accuracy: ", accuracy_score(expected, predicted))
