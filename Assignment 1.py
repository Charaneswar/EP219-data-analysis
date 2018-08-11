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
teachers_per_school=np.zeros((108,1),float)
i=0
while(i<108)

