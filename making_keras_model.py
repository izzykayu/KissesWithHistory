# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
import numpy as np


# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]

# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))

# Add the second layer
model.add(Dense(32, activation='relu'))

# Add the output layer
model.add(Dense(1))

# adding the compiler
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(predictors, target)
# basically is similar to sci kit learn, 

# output layer which is workers values

target = np.array([ 5.1 ,  4.95,  6.67,  4.  ,  7.5 , 13.07,  4.45, 19.47, 13.28,
        8.75, 11.35, 11.5 ,  6.5 ,  6.25, 19.98,  7.3 ,  8.  , 22.2 ,
        3.65, 20.55,  5.71,  7.  ,  3.75,  4.5 ,  9.56,  5.75,  9.36,
        6.5 ,  3.35,  4.75,  8.9 ,  4.  ,  4.7 ,  5.  ,  9.25, 10.67,
        7.61, 10.  ,  7.5 , 12.2 ,  3.35, 11.  , 12.  ,  4.85,  4.3 ,
        6.  , 15.  ,  4.85,  9.  ,  6.36,  9.15, 11.  ,  4.5 ,  4.8 ,
        4.  ,  5.5 ,  8.4 ,  6.75, 10.  ,  5.  ,  6.5 , 10.75,  7.  ,
       11.43,  4.  ,  9.  , 13.  , 12.22,  6.28,  6.75,  3.35, 16.  ,
        5.25,  3.5 ,  4.22,  3.  ,  4.  , 10.  ,  5.  , 16.  , 13.98,
       13.26,  6.1 ,  3.75,  9.  ,  9.45,  5.5 ,  8.93,  6.25,  9.75,
        6.73,  7.78,  2.85,  3.35, 19.98,  8.5 ,  9.75, 15.  ,  8.  ,
       11.25, 14.  , 10.  ,  6.5 ,  9.83, 18.5 , 12.5 , 26.  , 14.  ,
       10.5 , 11.  , 12.47, 12.5 , 15.  ,  6.  ,  9.5 ,  5.  ,  3.75,
       12.57,  6.88,  5.5 ,  7.  ,  4.5 ,  6.5 , 12.  ,  5.  ,  6.5 ,
        6.8 ,  8.75,  3.75,  4.5 ,  6.  ,  5.5 , 13.  ,  5.65,  4.8 ,
        7.  ,  5.25,  3.35,  8.5 ,  6.  ,  6.75,  8.89, 14.21, 10.78,
        8.9 ,  7.5 ,  4.5 , 11.25, 13.45,  6.  ,  4.62, 10.58,  5.  ,
        8.2 ,  6.25,  8.5 , 24.98, 16.65,  6.25,  4.55, 11.25, 21.25,
       12.65,  7.5 , 10.25,  3.35, 13.45,  4.84, 26.29,  6.58, 44.5 ,
       15.  , 11.25,  7.  , 10.  , 14.53, 20.  , 22.5 ,  3.64, 10.62,
       24.98,  6.  , 19.  , 13.2 , 22.5 , 15.  ,  6.88, 11.84, 16.14,
       13.95, 13.16,  5.3 ,  4.5 , 10.  , 10.  , 10.  ,  9.37,  5.8 ,
       17.86,  1.  ,  8.8 ,  9.  , 18.16,  7.81, 10.62,  4.5 , 17.25,
       10.5 ,  9.22, 15.  , 22.5 ,  4.55,  9.  , 13.33, 15.  ,  7.5 ,
        4.25, 12.5 ,  5.13,  3.35, 11.11,  3.84,  6.4 ,  5.56, 10.  ,
        5.65, 11.5 ,  3.5 ,  3.35,  4.75, 19.98,  3.5 ,  4.  ,  7.  ,
        6.25,  4.5 , 14.29,  5.  , 13.75, 13.71,  7.5 ,  3.8 ,  5.  ,
        9.42,  5.5 ,  3.75,  3.5 ,  5.8 , 12.  ,  5.  ,  8.75, 10.  ,
        8.5 ,  8.63,  9.  ,  5.5 , 11.11, 10.  ,  5.2 ,  8.  ,  3.56,
        5.2 , 11.67, 11.32,  7.5 ,  5.5 ,  5.  ,  7.75,  5.25,  9.  ,
        9.65,  5.21,  7.  , 12.16,  5.25, 10.32,  3.35,  7.7 ,  9.17,
        8.43,  4.  ,  4.13,  3.  ,  4.25,  7.53, 10.53,  5.  , 15.03,
       11.25,  6.25,  3.5 ,  6.85, 12.5 , 12.  ,  6.  ,  9.5 ,  4.1 ,
       10.43,  5.  ,  7.69,  5.5 ,  6.4 , 12.5 ,  6.25,  8.  ,  9.6 ,
        9.1 ,  7.5 ,  5.  ,  7.  ,  3.55,  8.5 ,  4.5 ,  7.88,  5.25,
        5.  ,  9.33, 10.5 ,  7.5 ,  9.5 ,  9.6 ,  5.87, 11.02,  5.  ,
        5.62, 12.5 , 10.81,  5.4 ,  7.  ,  4.59,  6.  , 11.71,  5.62,
        5.5 ,  4.85,  6.75,  4.25,  5.75,  3.5 ,  3.35, 10.62,  8.  ,
        4.75,  8.5 ,  8.85,  8.  ,  6.  ,  7.14,  3.4 ,  6.  ,  3.75,
        8.89,  4.35, 13.1 ,  4.35,  3.5 ,  3.8 ,  5.26,  3.35, 16.26,
        4.25,  4.5 ,  8.  ,  4.  ,  7.96,  4.  ,  4.15,  5.95,  3.6 ,
        8.75,  3.4 ,  4.28,  5.35,  5.  ,  7.65,  6.94,  7.5 ,  3.6 ,
        1.75,  3.45,  9.63,  8.49,  8.99,  3.65,  3.5 ,  3.43,  5.5 ,
        6.93,  3.51,  3.75,  4.17,  9.57, 14.67, 12.5 ,  5.5 ,  5.15,
        8.  ,  5.83,  3.35,  7.  , 10.  ,  8.  ,  6.88,  5.55,  7.5 ,
        8.93,  9.  ,  3.5 ,  5.77, 25.  ,  6.85,  6.5 ,  3.75,  3.5 ,
        4.5 ,  2.01,  4.17, 13.  ,  3.98,  7.5 , 13.12,  4.  ,  3.95,
       13.  ,  9.  ,  4.55,  9.5 ,  4.5 ,  8.75, 10.  , 18.  , 24.98,
       12.05, 22.  ,  8.75, 22.2 , 17.25,  6.  ,  8.06,  9.24, 12.  ,
       10.61,  5.71, 10.  , 17.5 , 15.  ,  7.78,  7.8 , 10.  , 24.98,
       10.28, 15.  , 12.  , 10.58,  5.85, 11.22,  8.56, 13.89,  5.71,
       15.79,  7.5 , 11.25,  6.15, 13.45,  6.25,  6.5 , 12.  ,  8.5 ,
        8.  ,  5.75, 15.73,  9.86, 13.51,  5.4 ,  6.25,  5.5 ,  5.  ,
        6.25,  5.75, 20.5 ,  5.  ,  7.  , 18.  , 12.  , 20.4 , 22.2 ,
       16.42,  8.63, 19.38, 14.  , 10.  , 15.95, 20.  , 10.  , 24.98,
       11.25, 22.83, 10.2 , 10.  , 14.  , 12.5 ,  5.79, 24.98,  4.35,
       11.25,  6.67,  8.  , 18.16, 12.  ,  8.89,  9.5 , 13.65, 12.  ,
       15.  , 12.67,  7.38, 15.56,  7.45,  6.25,  6.25,  9.37, 22.5 ,
        7.5 ,  7.  ,  5.75,  7.67, 12.5 , 16.  , 11.79, 11.36,  6.1 ,
       23.25, 19.88, 15.38])
