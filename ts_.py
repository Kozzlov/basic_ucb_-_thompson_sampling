#ucb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

import random as r 

N = 2000
d = 10
selected_ads = []
number_of_rewards_1 = [0] * d
number_of_rewards_0 = [0] * d 
total_reward = 0

for n in range(0, N):
    ad = 0 
    max_random_beta = 0
    for i in range(0, d):
        random_beta = r.betavariate(number_of_rewards_1[i] + 1,  number_of_rewards_0[i] + 1)
        if( random_beta > max_random_beta):
            max_random_beta = random_beta
            ad = i
            
    selected_ads.append(ad) 
    reward = dataset.values[n, ad]
    
    if(reward == 1):
        number_of_rewards_1[ad] += 1
    else:
        number_of_rewards_0[ad] += 1
        
    total_reward = total_reward + reward
     
plt.hist(selected_ads)
plt.title(' add selection histogram ')
plt.xlabel('ads')
plt.ylabel('number of times add was selected')