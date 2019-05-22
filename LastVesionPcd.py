from __future__ import absolute_import
import recurrentshop
from recurrentshop.cells import ExtendedRNNCell
from keras.models import Model,Sequential
from keras.layers import Input, Dense, Lambda, Activation
from keras.layers import add, multiply, concatenate
from keras import backend as K


from recurrentshop import LSTMCell, RecurrentSequential, GRUCell
from keras.layers import  Dropout, TimeDistributed

from keras import initializers
from keras import constraints
from keras import regularizers
import tensorflow as tf
import pickle
import re
import io
import nltk
from nltk.corpus import stopwords
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import load_model
from keras.utils import plot_model
from matplotlib import pyplot
from keras.initializers import glorot_normal
import keras
from sklearn import metrics
from keras.optimizers import Adam
import scipy
#from attention_decoder import AttentionDecoderx
from sklearn.model_selection import cross_val_score

class LSTMDecoderCell(ExtendedRNNCell):
    def __init__(self, hidden_dim=None, **kwargs):
        if hidden_dim:
            self.hidden_dim = hidden_dim
        else:
            self.hidden_dim = self.output_dim
        super(LSTMDecoderCell, self).__init__(**kwargs)
    def _slice(self, x, dim, index):
        return x[:, index * dim: dim * (index + 1)]
        
    def get_slices(self,x, n):
        dim = int(K.int_shape(x)[1] / n)
        return [Lambda(self._slice, arguments={'dim': dim, 'index': i}, output_shape=lambda s: (s[0], dim))(x) for i in range(n)]
    def build_model(self, input_shape):
        hidden_dim = self.hidden_dim
        output_dim = self.output_dim
        x = Input(batch_shape=input_shape)
        h_tm1 = Input(batch_shape=(input_shape[0], hidden_dim))
        c_tm1 = Input(batch_shape=(input_shape[0], hidden_dim))
        W1 = Dense(hidden_dim * 4,
                   kernel_initializer=self.kernel_initializer,
                   kernel_regularizer=self.kernel_regularizer,
                   use_bias=False)
        W2 = Dense(output_dim,
                   kernel_initializer=self.kernel_initializer,
                   kernel_regularizer=self.kernel_regularizer,)
        U = Dense(hidden_dim * 4,
                  kernel_initializer=self.kernel_initializer,
                  kernel_regularizer=self.kernel_regularizer,)
        z = add([W1(x), U(h_tm1)])
        z0, z1, z2, z3 =self.get_slices(z, 4)
        i = Activation(self.recurrent_activation)(z0)
        f = Activation(self.recurrent_activation)(z1)
        c = add([multiply([f, c_tm1]), multiply([i, Activation(self.activation)(z2)])])
        o = Activation(self.recurrent_activation)(z3)
        h = multiply([o, Activation(self.activation)(c)])
        y = Activation(self.activation)(W2(h))
        return Model([x, h_tm1, c_tm1], [y, h, c])


def Seq2Seq(output_dim, output_length, batch_input_shape=None,
            batch_size=None, input_dim=None, input_length=None,
            hidden_dim=None, broadcast_state=True, unroll=False,
            stateful=False, inner_broadcast_state=True, teacher_force=False,
            peek=False, dropout=0.):
    input_shape = (output_length, output_dim)
    if batch_input_shape:
        shape = batch_input_shape
    elif input_shape:
        shape = (batch_size,) + input_shape
    elif input_dim:
        if input_length:
            shape = (batch_size,) + (input_length,) + (input_dim,)
        else:
            shape = (batch_size,) + (None,) + (input_dim,)
    else:
        raise TypeError
    if hidden_dim is None:
        hidden_dim = output_dim
    encoder = RecurrentSequential(readout=True, state_sync=inner_broadcast_state,
                                  unroll=unroll, stateful=stateful,
                                  return_states=broadcast_state)
    #changer par GRUCell
    encoder.add(LSTMCell(hidden_dim, batch_input_shape=(shape[0], hidden_dim)))
    encoder.add(Dropout(dropout))
    dense1 = TimeDistributed(Dense(hidden_dim))
    dense1.supports_masking = True
    dense2 = Dense(output_dim)
    decoder = RecurrentSequential(readout='add' if peek else 'readout_only',
                                  state_sync=inner_broadcast_state, decode=True,
                                  output_length=output_length, unroll=unroll,
                                  stateful=stateful, teacher_force=teacher_force)
    decoder.add(Dropout(dropout, batch_input_shape=(shape[0], output_dim)))
    decoder.add(LSTMDecoderCell(output_dim=output_dim, hidden_dim=hidden_dim,
                                    batch_input_shape=(shape[0], output_dim)))
    _input = Input(batch_shape=shape)
    _input._keras_history[0].supports_masking = True
    encoded_seq = dense1(_input)
    encoded_seq = encoder(encoded_seq)
    if broadcast_state:
        assert type(encoded_seq) is list
        states = encoded_seq[-2:]
        encoded_seq1 = encoded_seq[0]
    else:
        states = None
    encoded_seq = dense2(encoded_seq1)
    inputs = [_input]
    if teacher_force:
        truth_tensor = Input(batch_shape=(shape[0], output_length, output_dim))
        truth_tensor._keras_history[0].supports_masking = True
        inputs += [truth_tensor]
    decoded_seq = decoder(encoded_seq,
                          ground_truth=inputs[1] if teacher_force else None,
                          initial_readout=encoded_seq, initial_state=states)
    model = Model(inputs, decoded_seq)
    model2 = Model(inputs, encoded_seq1)
    model.encoder = encoder
    model.decoder = decoder
    return model, model2

#prepare doc input
    
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

for i in range(137):
    if l1[i]==most:
        print(i)
        
df["key_words"]= [ " ".join(j) for j in df.filtered_sentence]
print((df.key_words[0]))

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

t=[0 for i in range(0,200)]
mat=[[0 for x in range(0,483)] for y in range (0,137)]
for i in range(0,137):
    for j in range(0,483): 
        if (j<len(list_vect[i])):
            mat[i][j]=list_vect[i][j]
        else:
            mat[i][j]=t
print((mat[97]))
sequence = np.array(mat)

model, model2 = Seq2Seq(output_dim=200, hidden_dim=400, output_length=483,dropout=0.25)
model.compile(loss='mse', optimizer='adam')
y=model.fit(sequence,sequence,epochs=250)

#cross validation
scores = cross_val_score(model,sequence, y , cv=5, scoring='brier_score_loss')
scores.mean()


#model.predict(x)[0]
#model2.predict(x)[0]

#prepare query input 


file_errors_location = r'C:/Users/asus/pcd2019/.spyproject/important/requete.xlsx'
df1 = pd.read_excel(file_errors_location)

symtoms=[]
for x in df1:
    print(x)
    symtoms.append(x)
print(symtoms[1])
x=[]
for i in range(1,137):
    x.append( symtoms[i].split())
    print((x))
list_vect1=[]
for j in (x):
   
    #print((j))

    l1=[]
    for word in j:
            #print(word)
        if word in new_dict.keys():
                l1.append(new_dict.get(word))
            #print(l[2])
        list_vect1.append(l1)
print(list_vect1[4]) 
t1=[0 for i in range(0,200)]
mat1=[[0 for x in range(0,51)] for y in range (0,136)]
for i in range(0,136):
    for j in range(0,51): 
        if (j<len(list_vect1[i])):
            mat1[i][j]=list_vect1[i][j]
        else:
            mat1[i][j]=t1
print((mat1[97]))
      
sequence1 = np.array(mat1)

model3, model4 = Seq2Seq(output_dim=200, hidden_dim=400, output_length=51,dropout=0.25)
model3.compile(loss='mse', optimizer='adam')
model3.fit(sequence1,sequence1,epochs=200)



