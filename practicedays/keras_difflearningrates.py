# with keras
from keras.optimizers import SGD

def get_new_model(input_shape = input_shape):
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape = input_shape))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    return model

lr_to_test = [0.000001, 0.01, 1]   # low, medium and high learning rate

for lr in lr_to_test:
    print('\n\nTesting model with learning rate: %f\n'%lr )
    model = get_new_model()
    izzys_optimizer = SGD(lr=lr)
    model.compile(optimizer=izzys_optimizer, loss = 'categorical_crossentropy')
    model.fit(predictors, target)

# dying neuron problem thus any node with negative will get zero, and those weights dont get updated
# may continue only getting negative inputs
