import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kmodes.kprototypes import KPrototypes
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.datasets import make_blobs
from kneed import KneeLocator

df = pd.read_csv("./customer_data.csv")
customer = df
for i in customer.columns:
    print(i)
    print(customer[i].value_counts())
    print("\n--------------------------------------\n")

ind = []
l = customer.dtypes
for i in range(len(l)):
    if (str(l[i])=='object'):
        ind.append(i)
c_data = [customer.columns[i] for i in ind]
print("Columns with categorical data")
print(c_data)


d={}
k=0
for i in customer.columns:
    d[i]=k
    k=k+1

customer.rename(columns=d,inplace=True)

c_list=[]
cluster_dict={}
for i in range(1,11):
    kproto = KPrototypes(n_clusters=i, init='Cao', verbose=2)
    clusters = kproto.fit_predict(customer, categorical=ind)
    cluster_dict[i]=clusters
    c_list.append(kproto.cost_)
    print("------------------------------------------------------")

sns.lineplot(y=c_list,x=range(0,len(c_list)))


y=c_list
x = range(1, len(y)+1)
kn = KneeLocator(x, y, curve='convex', direction='decreasing')
print("Number of clusters : ",kn.knee)

final_cluster = cluster_dict[kn.knee]
cd={}
for i in range(kn.knee):
    cd[i]=[]
    
for i in range(0,len(final_cluster)):
    cd[final_cluster[i]].append(list(customer.iloc[i]))

column = list(df.columns)
for i in range(len(cd)):
    cd[i]=pd.DataFrame(cd[i],columns=column)



