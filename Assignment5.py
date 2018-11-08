import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import dis
import math
import scipy.integrate as integrate
from scipy.integrate import quad
data = pd.read_csv('recoilenergydata_EP219.csv')
data_array = data.values

# Taking values of datasheet columns in arrays
number_of_events = data[' Number of events'].values
E_rvalues = data['#E_R (KeV)'].values

# writing the function of background data
def integrand(x):
    return 1000 * np.exp(-x / 10)

nmean_background = np.zeros((40, 1), int)

# Calculating mean by integrating
i = 0
while(i < 40):
    nmean_background[i], err = quad(integrand, i, i + 1)
    i += 1
#finding the test schematic for the given data
k=0
ts=0
while (k<40):
	ts_sum=(number_of_events[k]-nmean_background[k])*(number_of_events[k]-nmean_background[k])/nmean_background[k]
	ts=ts+ts_sum
	k+=1

#finding p value of the given data
p=integrate.quad(lambda x:(x**18.5)*(math.e**(-x/2))/(math.gamma(19.5)*(2**19.5)), 0, ts)
p=1-p[0]
print(p)
