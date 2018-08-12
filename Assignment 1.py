import pandas as pd
import matplotlib as plt
import numpy as np
import array as arr
import dis
#extracting full data to numpy array
data=pd.read_csv('pre_primary_school_data.csv')
data_array=data.values
#extracting the needed columns into numpy array
male_teachers=data['Pre - Primary Schools Having LKG / UKG / Nursery Classes - Teachers - M'].values
female_teachers=data['Pre - Primary Schools Having LKG / UKG / Nursery Classes - Teachers - F'].values
schools=data['Pre - Primary Schools Having LKG / UKG / Nursery Classes - Number of Institutions'].values
total_teachers=male_teachers+female_teachers
#creating an array to store teachers per school
teachers_per_school=np.zeros((108,1),float)
i=0
while(i<108):
    if(schools[i]!=0):
        teachers_per_school[i]=total_teachers[i]/schools[i]
    else:
        teachers_per_school[i]=total_teachers[i]
    i+=1
#adding a column to data array which shows total number of teachers per pre-primary school
new_array=np.column_stack([data_array,teachers_per_school])
#creating array to store eachers_per_school in rural,urban,combined
teachers_per_school_rural=np.zeros((36,1),float)
teachers_per_school_urban=np.zeros((36,1),float)
teachers_per_school_combined=np.zeros((36,1),float)
j,r,u,t=0
while(j<108):
    if(j%3==0)
        teachers_per_school_rural[r]=teachers_per_school[j]
        r+=1
    if(j%3==1):
        teachers_per_school_urban[u]=teachers_per_school[j]
        u+=1
    if(j%3==2):
        teachers_per_school_combined[t]=teachers_per_school[j]
        t+=1
    j+=1
#hist for rural
plt.xlabel("number of teachers per rural school")
plt.ylabel("number of states")
plt.title("number of states with a number per pre-primary school")
plt.hist(teachers_per_school_rural,bins='auto',histtype='bar',rwidth=0.3)
plt.show()
#hist for urban
plt.xlabel("number of teachers per urban school")
plt.ylabel("number of states")
plt.title("number of states with a number per urban pre-primary school")
plt.hist(teachers_per_school_urban,bins='auto',histtype='bar',rwidth=0.3)
plt.show()
#hist for combined
plt.xlabel("number of teachers per combined school")
plt.ylabel("number of states")
plt.title("number of states with a number per combined pre-primary school")
plt.hist(teachers_per_school_combined,bins='auto',histtype='bar',rwidth=0.3)
plt.show()

