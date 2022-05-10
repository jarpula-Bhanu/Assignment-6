import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem, xlabel, ylabel

#Probability of doctor choosing transport
train = 3/10
bus = 1/5
scooter = 1/10
other = 2/5

#Probability thet he will be late
by_train = 1/4
by_bus = 1/3
by_scooter = 1/12
by_other = 0

#Total sum of events
sum_of_events = train*by_train+bus*by_bus+scooter*by_scooter+other*by_other

#From bayes theorem finding late by each situation
Pr_train = (train*by_train)/sum_of_events
Pr_bus = (bus*by_bus)/sum_of_events
Pr_scooter = (scooter*by_scooter)/sum_of_events
Pr_other = (other*by_other)/sum_of_events

#Displaying probability
print("Probability  of doctor getting late by train",Pr_train)

#Plotting pmf
X = (['Train','Bus','Scooter','Other'])
Y = np.array([Pr_train,Pr_bus,Pr_scooter,Pr_other])
fig = stem(X,Y,linefmt='k-',markerfmt='ro',basefmt='k-')
plt.title('PMF graph')
plt.xlabel('Mode of transport')
plt.ylabel('Probability of getting late')
plt.grid('minor')
plt.show()