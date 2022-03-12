import numpy as np
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

# Load Model
(train_X , train_y), (test_X , test_y) = mnist.load_data("mymnist.data")
# Reshape data and change type
test_X = test_X.reshape(-1 , 28, 28, 1)
train_X = train_X.reshape(-1 ,  28, 28, 1)
test_X = test_X.astype("float32")
train_X = train_X.astype("float32")
# One hot encoding
test_y = to_categorical(test_y,num_classes=None)
train_y = to_categorical(train_y,num_classes=None)

accuracy= open("accuracy.txt","r")
accuracy = float(accuracy.read())
accuracy = accuracy *100
#Initials
neurons = 10
epochs = 1
test = 1
flag = 0
kernel = 8
batch_size = 128
#filter = 3


while int(accuracy)<90:
    if flag == 1 :
        model = keras.backend.clear_session()
        neurons = neurons+10
        epochs = epochs+1
        test = test + 1
        kernel = kernel * 2
        test = test + 1
    print("* * * TRIAL : ",test ,"-----------------")
    model=Sequential()
    model.add(Conv2D(kernel, (3,3), input_shape = (28, 28, 1), activation = 'relu'))
    model.add(MaxPooling2D(pool_size =(2,2)))
    model.add(Flatten())
    model.add(Dense(neurons, activation = 'relu'))
    model.add(Dense(10, activation = 'softmax'))
    model.compile( optimizer= "Adam" , loss='categorical_crossentropy',  metrics=['accuracy'] )
    train_X.shape
    model_predict= model.fit(train_X, train_y,batch_size=batch_size,verbose=1,epochs=epochs,validation_data=(test_X, test_y),shuffle=True)
    scores = model.evaluate(test_X, test_y, verbose=False)
    print('Test loss :', scores[0]*100)
    print('-------Accuracy of the model :', scores[1]*100)
    accuracy = scores[1]*100
    print("_______________________________________________________")
    print()
    print()
    flag = 1

print("Total numbers of epochs :" , epochs)
print("Total number of filters :", kernel)
print("Total number of neurons :", neurons)
print("Final Accuracy : ", accuracy)

## After the Hyperparameter Tuning again mail will be sent ##

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "limbachiyajeet42@gmail.com"  # Enter your address
receiver_email = "acanubhav@gmail.com"  # Enter receiver address
password = "123456789@987654321"
message = """\
Subject: Hi there

This message is sent from jenkins regarding your accuracy!!! """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
