# since deep learning is on really big datasets
# usually kfold not run because it is so large

# during model.fit step, can use model.fit(predictors, fit, validation_split=0.3)
# can use 'early stopping'

from keras.callbacks import EarlyStopping
early_stopping_monitor = EarlyStopping(patience=2)

# patience, how many epochs model can go without stopping without improving -- model might im[prove still
# in practice maybe 3 epochs at most

model.fit(predictors, fit, validation_split=0.3, epochs=20, callbacks = [early_stopping_monitor])

# want to switch to pytorch
