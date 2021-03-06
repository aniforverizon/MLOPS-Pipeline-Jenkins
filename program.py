from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.regularizers import l2
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.backend import clear_session

(x_train, y_train), (x_test, y_test)  = mnist.load_data()
x_train.shape

img = x_train[0].shape
print("size of image",img)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28,28 , 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
y_train =to_categorical(y_train,num_classes=None)
y_test =to_categorical(y_test,num_classes=None)

model = Sequential()

kernel = 8
filter = 3
pool = 2


model.add(Conv2D(kernel, (filter,filter), input_shape = (28, 28, 1), activation = 'relu'))
model.add(MaxPooling2D(pool_size =(pool,pool)))

model.add(Flatten())

model.add(Dense(10, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))
model.compile( optimizer= "Adam" , loss='categorical_crossentropy',  metrics=['accuracy'] )
print(model.summary())

batch_size = 128
epochs = 1

history = model.fit(x_train, y_train,
          batch_size=batch_size,verbose=1,
          epochs=epochs,
          validation_data=(x_test, y_test),
          shuffle=True)

model.save("mnist_LeNet.h5")

# Evaluate the performance of our trained model
scores = model.evaluate(x_test, y_test, verbose=False)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
accuracy = scores[1]

f= open("accuracy.txt","w+")
f.write(str(accuracy))
f.close()
print("Accuracy is : " , accuracy ,"%")
