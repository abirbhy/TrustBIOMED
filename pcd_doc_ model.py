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
import keras
from keras.optimizers import Adam
#from attention_decoder import AttentionDecoder
from sklearn.model_selection import cross_val_score
#import pydot
import os

infile = open(r'C:/Users/asus/pcd2019/.spyproject/FastText.p','rb')
new_dict = pickle.load(infile,encoding='latin1')
infile.close()
print(len(new_dict))
f = open(r"C:/Users/asus/pcd2019/.spyproject/FastText_pcd.txt","w")
corpus = str(new_dict)
print(new_dict.get("keeping"))
f.write(corpus)
f.close()
file_errors_location = r'C:/Users/asus/pcd2019/.spyproject/important/doc.xlsx'
df = pd.read_excel(file_errors_location)


def tokenize(string):
    string.strip()
    string=re.sub('(\\d|\\W)+',' ',string)
    return string

def elimineredondance(l1):
    E = []
    for elem in l1:
        if isinstance(elem, list):
            E1 = []
            for elem2 in elem:
                if elem2 not in E1:
                    E1.append(elem2)
            E.append(E1)
        else:
            E.append(elem)
    return E
#other tokenize
#def tokenize(string):
    #string = re.sub(r"""[\[\](),\.\";:!?&\^\/\*\'\#]""",'',string)
   # string = re.sub(r'  +',' ',string)
  #  string = re.sub(r' [^a-zA-Z]+ ',' ',string)
 #   string = re.sub(r'\n',' ',string)
#    return string
df["text_preprocessing"]=[ tokenize(text) for text in df.Symptômes]
print(df.text_preprocessing[0])
m=[]
for text in df.text_preprocessing:
    m1=[]
    for word in(text.lower()).split():
        if not word in stopwords.words("english"):
            m1.append(word)
    m.append(m1)
df["filtered_sentence"]=(elimineredondance(m))
print((df.filtered_sentence[0]))

l1=[]
for j in (df.filtered_sentence):
    l1.append(len(j))
most=max(l1)    
print(most)
#print(l1)    

#l2=[]
#for i in range(137):
#    l2.append(len(l1[i]))
#m=max(l2)
#print(m)
for i in range(137):
    if l1[i]==most:
        print(i)
        
df["key_words"]= [ " ".join(j) for j in df.filtered_sentence]
print((df.key_words[0]))
#print(new_dict)

#"name-however" in [tokenize(word) for word in df.text_preprocessing[1].split()]
list_vect=[]
for text in (df.key_words):
    l=[]    
    for word in text.split():
        if word in new_dict.keys():
            l.append(new_dict.get(word))
    list_vect.append(l)
l2=[]
for j in range(137):
    l2.append(len(list_vect[j]))  
mor=max(l2)
print(mor)
         
df["vect"]= list_vect
print((df.vect))
print (len(df.vect[0]))

#sequence = sequence.reshape((1, 137, 1))
#print(sequence)

#mat contient les vecteurs des mots de chaque document
t=[0 for i in range(0,200)]
mat=[[0 for x in range(0,483)] for y in range (0,137)]
for i in range(0,137):
    for j in range(0,483): 
        if (j<len(list_vect[i])):
            mat[i][j]=list_vect[i][j]
        else:
            mat[i][j]=t

sequence = np.array(mat)

print(sequence[37])

x_train1, x_test1 = train_test_split(sequence, test_size=0.2)
print(x_train1.shape)
print(x_test1.shape)
print(x_train1[37])
print (x_test1[1])
#prelu = PReLU(alpha_initializer='zeros', alpha_regularizer=None, alpha_constraint=None, shared_axes=None)

# define model
k=keras.initializers.constant(value=0.01)
model = Sequential()
model.add(LSTM(160, activation='tanh',recurrent_initializer=k,input_shape=(483,200)))
#model.add(Dropout(0.5))
model.add(RepeatVector(483))
model.add(LSTM(160, activation='tanh',recurrent_initializer=k, return_sequences= True ))
model.add(TimeDistributed(Dense(200,activation='sigmoid')))
adam =keras.optimizers.Adam(lr=0.0001)
model.compile(optimizer='adam', loss='mse',metrics=['accuracy'])

model.summary()

history=model.fit(x_train1,x_train1, epochs=10, verbose=2,shuffle = False ,validation_data=(x_test1, x_test1))
             
intermediate_layer_model = Model(inputs=model.layers[0].input,
                    outputs=model.layers[0].output)
intermediate_output_doc = intermediate_layer_model.predict(x_test1)

print(len(intermediate_output_doc[2]))
for i in range(28):
    print('*********')
    print(intermediate_output_doc[i])
    print('*********')



bou =model.predict(x_train1)

model.save("pcd_doc_model.h5")
print(bou)
pyplot.plot(history.history['loss'])
pyplot.plot(history.history['val_loss'])
pyplot.title('model loss')
pyplot.ylabel('loss')
pyplot.xlabel('epoch')
pyplot.legend(['train', 'test'], loc='upper right')
pyplot.show()


#cross validation
scores = cross_val_score(model, x_train,intermediate_output_doc, cv=5,scoring="loss")
scores.mean()



#define model with attention
"""model = Sequential()
model.add(LSTM(30, input_shape=(483, 200), return_sequences=True))
model.add(AttentionDecoder(30,200))
model.compile(loss='mse', optimizer='adam', metrics=['acc'])"""

#other model
"""learning_rate = 0.1
inputs = Input(shape=(510, 200))
encoded = LSTM(50,keras.initializers.glorot_normal(seed=None)(inputs))

decoded = RepeatVector(510,keras.initializers.glorot_normal(seed=None))(encoded)
decoded = LSTM(200, return_sequences=True,keras.initializers.glorot_normal(seed=None))(decoded)

sequence_autoencoder = Model(inputs, decoded)
encoder = Model(inputs, encoded)
sequence_autoencoder.summary()

sequence_autoencoder.compile(optimizer='adam', loss='mse')
history = sequence_autoencoder.fit(x_train, x_train,
                epochs=10,
                batch_size=137,
                shuffle=True,
                validation_data=(x_test, x_test))

sequence_autoencoder.predict(x_test)

#other model
inputs= Input(batch_shape=(109,483, 200))

encoder = LSTM(50,kernel_initializer=glorot_normal(seed=None),activation='relu')(inputs)

decoder = RepeatVector(483)(encoder)
decoder = LSTM(50,kernel_initializer=glorot_normal(seed=None),activation='relu', return_sequences=True)(decoder)
autoencoder = Model(input=inputs, output=decoder)
adam =optimizers.Adam(lr=0.001)
autoencoder.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
history=autoencoder.fit(x_train,x_train, epochs=10, verbose=2,shuffle = True,validation_data=(x_test, x_test))

autoencoder.predict(x_test)"""
