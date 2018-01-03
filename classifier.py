import numpy as np
import pandas as pd
import pickle 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

a=open("mixed_images.pickle","rb")
img_df=pickle.load(a)
a.close()

shape=img_df.shape
new_index=list(range(0,shape[0]))
img_df.index=new_index
#print(img_df.head)

b=open("mixed_names.pickle","rb")
name_list=pickle.load(b)
b.close()
#print(name_list)



X_train, X_test, y_train, y_test = train_test_split(img_df, name_list, test_size=0.20, random_state=42)


 
 
clf = GaussianNB()
clf.fit(X_train, y_train) 
score__=clf.score(X_test,y_test)
print(score__,"score")

handle=open("Calssifier.pickle","wb")
pickle.dump(clf,handle,protocol=pickle.HIGHEST_PROTOCOL)
handle.close()