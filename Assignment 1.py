import pandas as pd
import matplotlib as plt
import numpy as np
import array as arr
import dis
data=pd.read_csv('pre_primary_school_data.csv')
male_teachers=data['Pre - Primary Schools Having LKG / UKG / Nursery Classes - Teachers - M'].values
female_teachers=data['Pre - Primary Schools Having LKG / UKG / Nursery Classes - Teachers - F'].values
schools=data['
