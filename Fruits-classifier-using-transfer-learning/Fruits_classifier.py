import tensorflow
from tensorflow import keras
from keras.models import Sequential
from keras.regularizers import l2
from keras.layers import Conv2D,Dense,MaxPooling2D,Flatten,BatchNormalization,Dropout
from keras import utils
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

from tensorflow import keras

base_model = keras.applications.VGG16(
    weights='imagenet',  # Load weights pre-trained on ImageNet.
    input_shape=(100, 100, 3),
    include_top=False)

base_model.trainable = False

inputs = keras.Input(shape=(100,100, 3))
# Separately from setting trainable on the model, we set training to False
x = base_model(inputs, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
# A Dense classifier with a single unit (binary classification)
outputs = keras.layers.Dense(36)(x)
model = keras.Model(inputs, outputs)

model.compile(loss=keras.losses.CategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

Train_Directory=r"D:\python\ece\train"
Category=["apple","banana","beetroot","bell_pepper","cabbage","capsicum","carrot","cauliflower","chilli_pepper","corn","cucumber","eggplant","garlic","ginger","grapes","jalepeno","kiwi","lemon","lettuce","mango","onion","orange","paprika","pear","peas","pineapple","pomegranate","potato","raddish","soy_beans","sweetcorn","tomato","turnip","watermelon"]

Test_Directory=r"D:\python\ece\test"


Train_data=[]
for category in Category:
    folder=os.path.join(Train_Directory,category)
    label=Category.index(category)
    for img in os.listdir(folder):
        img_path=os.path.join(folder,img)
        img_arr=cv2.imread(img_path)
        if img_arr is None:
            continue
        else:
            img_arr=cv2.resize(img_arr,(100,100))
            Train_data.append([img_arr,label])


Valid_data=[]
for category in Category:
    folder=os.path.join(Test_Directory,category)
    label=Category.index(category)
    for img in os.listdir(folder):
        img_path=os.path.join(folder,img)
        img_arr=cv2.imread(img_path)
        if img_arr is None:
            continue
        else:
            img_arr=cv2.resize(img_arr,(100,100))
            Valid_data.append([img_arr,label])

x_train=[]
y_train=[]
for features,labels in Train_data:
    x_train.append(features)
    y_train.append(labels)

x_test=[]
y_test=[]
for features,labels in Valid_data:
    x_test.append(features)
    y_test.append(labels)

x_train=np.array(x_train)
y_train=np.array(y_train)
x_test=np.array(x_test)
y_test=np.array(y_test)

x_train=x_train/255
x_test=x_test/255


num_classes=36
y_train=keras.utils.to_categorical(y_train,num_classes)
y_test=keras.utils.to_categorical(y_test,num_classes)


from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=10,  # randomly rotate images in the range (degrees, 0 to 180)
    zoom_range=0.1,  # Randomly zoom image
    width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
    height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
    horizontal_flip=True,  # randomly flip images horizontally
    vertical_flip=True, # Don't randomly flip images vertically
)

batch_size = 32
img_iter = datagen.flow(x_train, y_train, batch_size=batch_size)

datagen.fit(x_train)

model.compile(loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(img_iter,
          epochs=20,
          steps_per_epoch=int(len(x_train)/batch_size), # Run same number of steps we would if we were not using a generator.
          validation_data=(x_test, y_test))

# Unfreeze the base model
base_model.trainable = True

# It's important to recompile your model after you make any changes
# to the `trainable` attribute of any inner layer, so that your changes
# are taken into account
model.compile(optimizer=keras.optimizers.RMSprop(learning_rate = .001),  # Very low learning rate
              loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(img_iter,steps_per_epoch=92, validation_data=(x_test, y_test), epochs=32)

model.save("fruit_detector2.h5")
