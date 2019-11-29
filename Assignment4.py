import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import array as arr
import dis
from scipy.integrate import quad

# extracting full data to numpy array
data = pd.read_csv('recoilenergydata_EP219.csv')
data_array = data.values

# Taking values of datasheet columns in arrays
number_of_events = data[' Number of events'].values
E_rvalues = data['#E_R (KeV)'].values
k = 0
i = 0

# defining other array to get the number of events for a particular E_r
energy = np.zeros((10171, 1), float)
t_number_of_events = number_of_events[0]

# making n copies of E_r in energy where n is the number of events for that particular E_r
while(i < 39):
    while(k < t_number_of_events):
        energy[k] = E_rvalues[i]
        k += 1

    t_number_of_events += number_of_events[i + 1]
    i += 1
while (k < t_number_of_events):
    energy[k] = E_rvalues[i]
    k += 1

# plotting n vs energy
plt.xlabel("Values of recoil energy")
plt.ylabel("Number of events")
plt.title("Number of events v/s recoil energy data")
plt.hist(energy, bins=range(0, 41, 1))
plt.show()

# b)
# defining function for number of events due to background


def integrand(x):
    return 1000 * np.exp(-x / 10)


nmean_background = np.zeros((40, 1), int)

# Calculating mean by integrating
i = 0

total_backgroundevents = 0
while(i < 40):
    nmean_background[i], err = quad(integrand, i, i + 1)
    i += 1
    total_backgroundevents += nmean_background[i - 1]


# defining variable to make n copies of a particular energy where n is mean number of events due to background radiation
energy_backgroundevents = np.zeros((total_backgroundevents[0], 1), float)

# making n copies of energy_backgroundevents
t_backgroundevents = nmean_background[0][0]
i = 0
k = 0
while(i < 39):
    while(k < t_backgroundevents):
        energy_backgroundevents[k] = E_rvalues[i]
        k += 1

    t_backgroundevents += nmean_background[i + 1]
    i += 1
while (k < t_backgroundevents):
    energy_backgroundevents[k] = E_rvalues[i]
    k += 1

# plotting number of events due to background vs energy
plt.xlabel("Values of recoil energy")
plt.ylabel("Number of events due to background")
plt.title("Number of events due to background v/s recoil energy data")
plt.hist(energy_backgroundevents, bins=range(0, 41, 1))
plt.show()

# c)
# defining function for number of events due to darkmatter


def darkmatter(x):
    if 5 <= x < 15:
        return 20 * (x - 5)
    elif 15 <= x < 25:
        return 20 * (25 - x)
    else:
        return 0


# calculating mean via integration
nmean_darkmatter = np.zeros((5, 40), int)
i = 0
j = 0
f = 0.01
while(j < 5):
    i = 0
    while(i < 40):
        nmean_darkmatter[j, i], err = quad(darkmatter, i, i + 1)[0] * f, quad(darkmatter, i, i + 1)[1] * f
        i += 1
    f *= 10
    j += 1
# defining array for sum of events
sumofevents = np.zeros((5, 40), int)

i = 0
j = 0
while(j < 5):
    i = 0
    while(i < 40):
        sumofevents[j, i] = nmean_darkmatter[j, i] + nmean_background[i]
        i += 1

    j += 1

# Histograms were getting complicated so I used bar charts

# plotting graphs
# for sigma= 0.01
plt.xlabel("Values of recoil energy")
plt.ylabel("Total number of events")
plt.title("Total number of events v/s recoil energy data($\sigma=0.01$)")
plt.bar(E_rvalues, sumofevents[0], width=1)
plt.show()
# for sigma=0.1
plt.xlabel("Values of recoil energy")
plt.ylabel("Total number of events")
plt.title("Total number of events v/s recoil energy data($\sigma=0.1$)")
plt.bar(E_rvalues, sumofevents[1], width=1)
plt.show()
# for sigma=1
plt.xlabel("Values of recoil energy")
plt.ylabel("Total number of events")
plt.title("Total number of events v/s recoil energy data($\sigma=1$)")
plt.bar(E_rvalues, sumofevents[2], width=1)
plt.show()
# for sigma=10
plt.xlabel("Values of recoil energy")
plt.ylabel("Total number of events")
plt.title("Total number of events v/s recoil energy data($\sigma=10$)")
plt.bar(E_rvalues, sumofevents[3], width=1)
plt.show()
# for sigma=100
plt.xlabel("Values of recoil energy")
plt.ylabel("Total number of events")
plt.title("Total number of events v/s recoil energy data($\sigma=100$)")
plt.bar(E_rvalues, sumofevents[4], width=1)
plt.show()

# d)Calculating log likelihood function
# we ignored logk! where k is number of observed events
i = 0
loglikelihoodarray = []
sigma_arr = np.arange(0, 1, 0.0001)
mean_total = np.zeros((40, 1), int)

for sigma in np.arange(0, 1, 0.0001):
    for i in range(0, 40, 1):
        mean_total[i] = nmean_background[i] + nmean_darkmatter[2, i] * sigma
    loglikelihoodarray = np.append(loglikelihoodarray, np.dot(number_of_events, np.log(mean_total)) - np.sum(nmean_darkmatter[2]) * sigma - total_backgroundevents)
plt.xlabel("$\sigma$")
plt.ylabel("Log Likelihood")
plt.title("Log likelihood function")
plt.plot(sigma_arr, loglikelihoodarray)
plt.show()

# part e)
# getting max likelihood
maxlikelihood = np.max(loglikelihoodarray)
print(maxlikelihood)
# getting sigma corresponding to max likelihood
sigmaatmaxlikelihood = sigma_arr[np.argmax(loglikelihoodarray)]
print(sigmaatmaxlikelihood)
# calculating sigma for (max loglikelihood - 0.5) and thus delta
sigma_arg = []
for i in range(0, loglikelihoodarray.size):
    if(loglikelihoodarray[i] - maxlikelihood - 0.5 < 0.0001):
        sigma_arg.append(i)

minsigma_arg = np.min(sigma_arg)
minsigma = sigma_arr[minsigma_arg]
maxsigma_arg = np.max(sigma_arg)
maxsigma = sigma_arr[maxsigma_arg]
delta_left = sigmaatmaxlikelihood - minsigma
delta_right = maxsigma - sigmaatmaxlikelihood
print(maxsigma)
print(minsigma)
print(delta_left)
print(delta_right)
