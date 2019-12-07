
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import os
from shutil import copy
import numpy as np
import pandas as pd

def import_train_images(path,p1,p2):
    image_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = image_datagen.flow_from_directory(
        directory=path,
        target_size=(p1, p2),
        color_mode="rgb",
        batch_size=32,
        class_mode="categorical",
        shuffle=True,
        seed=42
    )
    return train_generator

def import_test_images(path,p1,p2):
    image_datagen = ImageDataGenerator(rescale=1./255)
    valid_generator = image_datagen.flow_from_directory(
        directory=path,
        target_size=(p1, p2),
        color_mode="rgb",
        batch_size=32,
        class_mode="categorical",
        shuffle=True,
        seed=42
    )
    return valid_generator


def model_initialization(p1,p2):
    cnn_model = Sequential()  # this is Keras's way of specifying a model that is a single sequence of layers
    cnn_model.add(Conv2D(32, (3, 3), input_shape = (p1,p2,3), activation = 'relu'))
    cnn_model.add(MaxPooling2D(pool_size = (2, 2)))
    cnn_model.add(Conv2D(32, (3, 3), activation = 'relu'))
    cnn_model.add(MaxPooling2D(pool_size = (2, 2)))
    # cnn_model.add(Conv2D(32, (3, 3), activation = 'relu'))
    # cnn_model.add(MaxPooling2D(pool_size = (2, 2)))
    cnn_model.add(Flatten())
    cnn_model.add(Dense(units = 128, activation = 'relu'))
    cnn_model.add(Dense(units = 5, activation = 'sigmoid'))
    cnn_model.compile(optimizer='adam',
                               loss='categorical_crossentropy',
                               metrics=['accuracy'])
    return cnn_model

def fit_model(cnn_model,train_generator,valid_generator):
    cnn_model.fit_generator(train_generator,
                                 steps_per_epoch = 10,
                                 epochs = 10,
                                 validation_data=valid_generator,
                                 validation_steps = 5)
    
    
def model_accuracy(cnn_model,test_generator):
    test_loss, test_acc = cnn_model.evaluate(test_generator)
    print('Test accuracy:', test_acc)
    

p1 = 128
p2 = 128
train_generator = import_train_images(r"./Data/Model Data/Train",p1,p2)
valid_generator = import_test_images(r"./Data/Model Data/Valid",p1,p2)
cnn_model = model_initialization(p1,p2)
#cnn_model.summary()
fit_model(cnn_model,train_generator,valid_generator)


test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
    directory=r"./Data/Model Data/Test",
    target_size=(128, 128),
    color_mode="rgb",
    batch_size=1,
    class_mode=None,
    shuffle=False,
    seed=42
)


STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
test_generator.reset()
pred=cnn_model.predict_generator(test_generator,
steps=STEP_SIZE_TEST,
verbose=1)


predicted_class_indices=np.argmax(pred,axis=1)


labels = (train_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]


filenames=test_generator.filenames

results=pd.DataFrame({"Filename":filenames,
                      "Predictions":predictions})
results.to_csv("results.csv",index=False)

for category in list(set(predictions)):
    path = './Predict/'+category
    os.mkdir(path)
    
for i in range(len(filenames)):
    copy('.\\Data\\Model Data\\Test\\'+filenames[i], '.\\Predict\\'+predictions[i])
    
    