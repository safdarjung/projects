import pandas as pd 
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json


df=pd.read_csv("D:\CV_Projects\pima-indians-diabetes.csv")
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

# print(df.shape)
# print(x.head())
# print()
# print(y.head())
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=150, batch_size=10)

_,accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

model_json = model.to_json()
with open('DIABETES_model.json', 'w') as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("DIABETES_weights.h5")
print("Saved model to disk")