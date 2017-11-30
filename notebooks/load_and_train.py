
# coding: utf-8

# In[1]:


from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import MaxPooling2D
from keras.layers import Conv2D
from keras.models import load_model
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from skimage.transform import resize
from sklearn.model_selection import train_test_split
import csv
import h5py
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
#get_ipython().magic('matplotlib inline')


# In[2]:


# set global variables and hyper-parameters
DATA_LOCATION = '../data/'
TRAIN_IMAGES_LOCATION = '../data/train_images/'
IMAGE_SIZE = 64
N_CLASSES = 121
BATCH_SIZE = 128
N_EPOCHS = 20

X = np.empty([len(filenames),IMAGE_SIZE,IMAGE_SIZE,1])
Y = np.empty([len(filenames),N_CLASSES])
print('Shapes:\nX:{}\nY:{}'.format(X.shape, Y.shape))


# In[4]:


def get_padding(i):
    """
    Helper function for getting right padding sizes
    input:
        - i: positive integer gotten from substracting height and width of an image
    output:
        - Tuple representing the correct padding
    """
    if i%2 == 0:
        return (int(i/2),int(i/2))
    else:
        return (int(i/2-.5), int(i/2+.5))

def pad_image(img):
    """
    Add padding to image to make it square
    input:
        - img: numpy array (2D) representing image
    output:
        - padded array of shape (N,N)
    """
    H, W = img.shape
    if H == W:
        return img
    elif H > W:
        return np.pad(img, ((0,0), get_padding(H-W)), 'constant')
    else:
        return np.pad(img, (get_padding(W-H), (0,0)), 'constant')

def resize_image(img):
    """
    Resize image to new square shape
    input:
        - img: numpy array (2D) representing image
        - size: final shape of image in pixels (integer)
    """
    return resize(img, (IMAGE_SIZE,IMAGE_SIZE), mode='reflect')


# For image in filenames:
# - load file
# - rotate [0,90,180,270] (how-to???: ImageDataGenerator?)
# - look up label in .csv
# - add 4 images to X
# - add 4 labels to Y

# In[ ]:


filenames = [i for i in os.listdir('../data/train_images') if i.endswith('.jpg')]
with open(DATA_LOCATION + 'train_onelabel.csv', mode='r') as infile:
    reader = csv.reader(infile)
    file_to_class = {rows[0]:rows[1] for rows in reader}


# In[5]:


for i in range(len(filenames)):
    # read and transform image to usable format
    img = mpimg.imread(TRAIN_IMAGES_LOCATION + filenames[i])
    img = np.absolute(np.divide(img.astype(float), 255) - 1.0)
    img = resize_image(pad_image(img))
    # create a grayscale channel 
    img = img.reshape(64,64,1)
    
    X[i] = img
    # set the one-hot-label
    Y[i][int(file_to_class[filenames[i]])] = 1.0


# In[6]:


# select a random train/test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)


# In[7]:


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=X[0].shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(N_CLASSES, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

model.fit(X_train, 
          y_train, 
          validation_data=(X_test,y_test), 
          batch_size=BATCH_SIZE, 
          epochs=N_EPOCHS, 
          verbose=1)

model.save('../data/output/models/model1.h5')


# In[ ]:




