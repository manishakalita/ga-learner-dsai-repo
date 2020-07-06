# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
data['Gender'].value_counts().plot.bar()
data.Alignment.value_counts().plot.bar()
data['Intelligence_rank']=data['Intelligence'].rank()
data['Strength_rank']=data['Strength'].rank()
data['Combat_rank']=data['Combat'].rank()
data['d1^2']=(data['Strength']-data['Combat'])**2
data['d2^2']=(data['Intelligence']-data['Combat'])**2
d1_square=data['d1^2'].sum()
d2_square=data['d2^2'].sum()
n=data.shape[0]
spearman_1=1- ((6*d1_square)/(n*(n**2-1)))
spearman_2=1- ((6*d2_square)/(n*(n**2-1)))
print(spearman_1)
print(spearman_2)
q1=data.Total.quantile(0.99)
print(q1)
data_1=data[data.Total>q1]
#data_1.head()
super_best_names =data_1.Name.unique()
print(super_best_names)
# Code starts here



