def main():
    pass

if __name__ == '__main__':
    main()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pow

# reading the .csv files for unemployment rates and crime rates

unemployment_f = pd.read_csv("unemploymentrate.csv")
crime_f = pd.read_csv("crimerate.csv")

#Storing relevant data for unemp rates and crime rates in separate dictionaries

size = len(unemployment_f["State/UTs"])-1

unemp_states = [unemployment_f["State/UTs"][i] for i in range(size)]
unemp_rates = [unemployment_f["2015-16"][i] for i in range(size)]
unemp_data_dict = {unemp_states[i]: unemp_rates[i] for i in range(len(unemp_states))}
unemp_data = [[i,unemp_data_dict[i]] for i in unemp_data_dict]
unemp_data.sort()
unemp_states = [i[0] for i in unemp_data]
unemp_rates = [i[1] for i in unemp_data]

crime_states = [crime_f["State/UT (Col.3)"][i] for i in range(size+1)]
crime_rates = [crime_f["Rate of Cognizable Crimes (IPC) (2016)++ (Col.10)"][i] for i in range(size+1)]
i = crime_states.index("Total (States)")
crime_rates.pop(i)
crime_states.pop(i)
crime_data_dict = {crime_states[i]:crime_rates[i] for i in range(size)}
crime_data = [[i,crime_data_dict[i]] for i in crime_data_dict]
crime_data.sort()
crime_states = [i[0] for i in crime_data]
crime_rates = [i[1] for i in crime_data]



#note that the data has not been normalised
#calculating mean rates
mean_unemp,mean_crime = 0,0

for i in unemp_rates:
    mean_unemp += i

for i in crime_rates:
    mean_crime += i
mean_unemp/= size
mean_crime/= size
mean_crime = round(mean_crime,4)
mean_unemp = round(mean_unemp,4)

print("Mean unemployment rate = ",mean_unemp,"%")
print("Mean crime rate = ",mean_crime," per lakh people")

# calculating variance (and stand. deviation)
var_unemp,var_crime = 0,0

for i in unemp_data:
    var_unemp += pow(i[1] - mean_unemp, 2)

for j in crime_data:
    var_crime +=pow(i[1] - mean_crime,2)
var_crime /= size-1
var_unemp /= size-1

std_unemp = sqrt(var_unemp)
std_crime = sqrt(var_crime)

std_unemp = round(std_unemp,4)
std_crime = round(std_crime,4)
print("Standard deviation in unemployment rate = ",std_unemp, "%")
print("Standard deviation in crime rate = ",std_crime, " per lakh people.")

# Plotting Histograms
plt.title("Crime Rate Distribution")
plt.xlabel('Crime Rate (per lakh population)')
plt.ylabel('Frequency')
plt.grid()
plt.axvline(mean_crime, color='b', label='Mean')
plt.plot(((mean_crime-std_crime),(mean_crime-std_crime)),(0,4.4),'g-')
plt.plot(((mean_crime+std_crime),(mean_crime+std_crime)),(0,4.4),'g-')
plt.plot(((mean_crime-std_crime),(mean_crime+std_crime)),(4.4,4.4),'g-')
plt.hist(crime_rates, bins = 'auto', rwidth = 0.96,color = 'r')
plt.show()

plt.title("Unemployment Rate Distribution")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.grid()
plt.axvline(mean_unemp, color='r', label='Mean')
plt.plot(((mean_unemp-std_unemp),(mean_unemp-std_unemp)),(0,3.2),'g-')
plt.plot(((mean_unemp+std_unemp),(mean_unemp+std_unemp)),(0,3.2),'g-')
plt.plot(((mean_unemp-std_unemp),(mean_unemp+std_unemp)),(3.2,3.2),'g-')
plt.hist(unemp_rates, bins = 20, rwidth =0.96,  color = 'b')
plt.show()

#scatter plot
plt.scatter(unemp_rates, crime_rates)
plt.title("State/UT wise scatter plot of unemployment rate versus crime rate")
plt.grid()
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Crime Rate (per lakh population)")
plt.show()


# 2D histogram
#NOTE------------------------------------------
#Unemployment rates have been normalize to per lakh people

unemp_rates_normed = [i*pow(10,3) for i in unemp_rates]
plt.hist2d(unemp_rates_normed, crime_rates, bins = 50)
plt.xlabel("Unemployment Rate (per lakh popultion)")
plt.ylabel("Crime Rate (per lakh population)")
plt.colorbar(label = 'Frequency/Occurence')
plt.show()

#Estimating the correlation
correlation = 0
for i in range(size):
    correlation += (mean_unemp-unemp_rates[i])*(mean_crime-crime_rates[i])
correlation/=size-1
correlation = round(correlation, 4)
print("Correlation = ",correlation)
correlation_coefficient = sqrt(correlation)/sqrt(std_crime*std_unemp)
print("Correlation Coefficient = ",correlation_coefficient)
