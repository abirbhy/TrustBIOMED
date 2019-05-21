import pickle
import re
import nltk
from nltk.corpus import stopwords
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import Sequential,Model
from keras.layers import LSTM,Input, Dense, RepeatVector, TimeDistributed,PReLU,Dropout
from keras.utils import plot_model
from matplotlib import pyplot
from keras.initializers import glorot_normal
from keras import optimizers,initializers
from scipy.spatial import distance
import scipy.spatial.distance
infile = open(r'C:/Users/asus/pcd2019/.spyproject/FastText.p','rb')
new_dict = pickle.load(infile,encoding='latin1')
infile.close()
print(len(new_dict))
f = open(r"C:/Users/asus/pcd2019/.spyproject/FastText_pcd.txt","w")
corpus = str(new_dict)
f.write(corpus)
f.close()
file_errors_location = r'C:/Users/asus/pcd2019/.spyproject/important/requete.xlsx'
df1 = pd.read_excel(file_errors_location)
def tokenize(string):
    string.strip()
    string=re.sub('(\\d|\\W)+',' ',string)
    return string
symtoms=[]
for x in df1:
    print(x)
    symtoms.append(x)
print(symtoms[0])
x=[]
for i in range(1,137):
    x.append( symtoms[i].split())
    print((x))
list_vect=[]
for j in (x):
   
    #print((j))

    l=[]
    for word in j:
            #print(word)
        if word in new_dict.keys():
                l.append(new_dict.get(word))
            #print(l[2])
        list_vect.append(l)
print(list_vect[4]) 
t=[0 for i in range(0,200)]
mat=[[0 for x in range(0,51)] for y in range (0,136)]
for i in range(0,136):
    for j in range(0,51): 
        if (j<len(list_vect[i])):
            mat[i][j]=list_vect[i][j]
        else:
            mat[i][j]=t
print((mat[97]))
      
sequence = np.array(mat)
print(sequence[1])
x_train2, x_test2 = train_test_split(sequence, test_size=0.2)
print(x_train2.shape)
print(x_test2.shape)

model = Sequential()
k =initializers.constant(value=0.02)
model.add(LSTM(160, activation='tanh',recurrent_initializer=k, input_shape=(51,200)))
#model.add(Dropout(0.5))
model.add(RepeatVector(51))
model.add(LSTM(160, activation='tanh',recurrent_initializer=k, return_sequences= True ))
model.add(TimeDistributed(Dense(200,activation='sigmoid')))
adam =optimizers.Adam(lr=0.0001)
#model.compile(loss='mean_squared_error', optimizer=sgd)
model.compile(optimizer='adam', loss='mse',metrics=['accuracy'])

history=model.fit(x_train2,x_train2, epochs=20, verbose=2,shuffle = False,validation_data=(x_test2, x_test2))
#score = model.evaluate(x_test, x_test, batch_size=28)
#print(score)

intermediate_layer_model= Model(inputs=model.layers[0].input,
                                 outputs=model.layers[0].output)
intermediate_output_Q = intermediate_layer_model.predict(x_train2)
print(intermediate_output_Q[2])
for i in range(108):
    print('*********')
    print(intermediate_output_Q[i])
    print('*********')
model.predict(x_test2)

model.save("req_model.h5")

pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'test'], loc='upper right')
pyplot.show()




"""def requete_bar():
    distan= []
    for i in range(1,403):
        print (vect[i])
        dist= []
        for j in range(1,403):
            if j != i :
                dist = scipy.spatial.distance.euclidean(list_vect[i], list_vect[j])
        distan.append(dist)       

requete_bar()"""

"""a={}
#print(l1)
listt=(list(enumerate(l1, start=1)))
print(listt[477])
for x in listt:
    for i in range(478):
        a[x[1]] = x[0]"""
    


