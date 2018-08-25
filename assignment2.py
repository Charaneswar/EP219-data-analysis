import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import dis
import math
#extracting data to a numpy array 
data=pd.read_excel('swachhbharat.xlsx')
data_array=data.values
i=0
#defining an array of fraction of ODF villages
odf_frac_UP=[]
#assigning values to the array
while(i<6871):
	if(data_array[i,0]=='Uttar Pradesh'):
		odf_frac_UP.append((data_array[i,5])/(data_array[i,4]))
	i+=1
j=odf_frac_UP.__len__()
#function to find the mean
def mean_val(ar):
	s=0
	for i in range(0,j-1):
		s=s+ar[i]
	mn=s/j
	return mn
mn=mean_val(odf_frac_UP)
#function to find the standard deviation
def std_dev(ar):
	s=0
	for i in range(0,j-1):
		s = s + pow((ar[i]-mn),2)
	sd=math.sqrt(s/(j-1))
	return sd
sd=std_dev(odf_frac_UP)
#restricting the mean and standard deviation to 2 decimal places
mn=mn-(mn%0.01)
sd=sd-(sd%0.01)
#ploting the histogram
f1=plt.figure(1)
tx1=f1.add_subplot(111)
f1.subplots_adjust(top=0.85)
tx1.text(0.5,100,r'Mean(Red)=%s'%(mn),fontsize=8)
tx1.text(0.5,95,r'Standard Deviation(Green)=%s'%(sd),fontsize=8)
tx1.text(0.5,90,r'Mean-Standard Deviation(Magenta)',fontsize=8)
tx1.text(0.5,85,r'Mean+Standard Deviation(Cyan)',fontsize=8)
plt.xlabel("Fraction of ODF Villages")
plt.ylabel("Number of Districts")
plt.title("Fraction of ODF Villages")
plt.axvline(mn, color='r', label='Mean')
plt.plot(((mn-sd),(mn-sd)),(0,60),'m-')
plt.plot(((mn+sd),(mn+sd)),(0,60),'c-')
plt.plot(((mn-sd),(mn+sd)),(60,60),'g-')
plt.hist(odf_frac_UP,bins=15,histtype='bar',rwidth=0.7)
plt.show()
