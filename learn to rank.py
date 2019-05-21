import pickle
import numpy as np
from keras.models import Sequential,Model
from keras.layers import Dense,Dropout
import pandas as pd
from keras.models import load_model
from req_model import *
from pcd_doc_model import *
model1=load_model('pcd_doc_model.h5')
model2=load_model('req_model.h5')  

file_errors_location = r'C:/Users/asus/pcd2019/.spyproject/important/requete.xlsx'
df =pd.read_excel(file_errors_location)

y=[]
z=[]
intermediate_layer_model2= Model(inputs=model2.layers[0].input,
                                 outputs=model2.layers[0].output)
intermediate_layer_model1= Model(inputs=model1.layers[0].input,
                                 outputs=model1.layers[0].output)
w=intermediate_layer_model2.predict(x_train2)
v=intermediate_layer_model1.predict(x_train1)



df.describe()
print(df.Disease)
for x in df :
    for j in range(137):
        print(df[x][j])
        if (df[x][j]) == 1:
            z.append(v[x]*w[df.Disease[j]])
            y.append(1)
        else:
            z.append(v[x]* w(df.sample()))
            y.append(0)
x_train= np.array(z) 
y_train= np.array(y) 

model = Sequential()
model.add(Dense(512, input_shape=(max_words,)))
 
           

            

print(df.sample())

"""list1=[]<
for i in range(137):
    list1.append(intermediate_output_doc)
list2=[]
for j in range(404):
    list2.append(intermediate_output_Q)
x_train=[list1,list2]    
		
		
		
		#print(queryVec)
results = [[self.dotProduct(vectors[result], queryVec), result] for result in resultDocs]
		#print(results)
results.sort(key=lambda x: x[0])
		#print(results)
results = [x[1] for x in results]"""
   