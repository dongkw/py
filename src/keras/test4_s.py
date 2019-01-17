from keras.models import load_model
from keras.utils import to_categorical
from keras.datasets import mnist

model = load_model("model.mnist")
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
score = model.evaluate(test_images,test_labels,verbose=0)


print(score)
