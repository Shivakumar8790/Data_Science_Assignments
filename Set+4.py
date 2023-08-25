# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 22:47:46 2023

@author: 91879
"""

# 3.Auditors at a small community bank randomly sample 100 withdrawal transactions made during the week at an ATM machine located near the bank’s main branch. Over the past 2 years, the average withdrawal amount has been $50 with a standard deviation of $40. Since audit investigations are typically expensive, the auditors decide to not initiate further investigations if the mean transaction amount of the sample is between $45 and $55. What is the probability that in any given week, there will be an investigation?

# Given Data 
mean = 50
std = 40
sample_size = 100

standard_error = std/ (sample_size)**0.5

# Z scores for lower and upper 
Z1 = (45-mean)/standard_error
Z2 = (55-mean)/standard_error

# Probability
import scipy.stats as stats
P = stats.norm.cdf(Z1)+(1-stats.norm.cdf(Z2))
P
print("Probability of investigation is",(P*100).round(2),"%")



## 4.	The auditors from the above example would like to maintain the probability of investigation to 5%. Which of the following represents the minimum number transactions that they should sample if they do not want to change the thresholds of 45 and 55? Assume that the sample statistics remain unchanged.

# Given Data 
mean1 = 45 
mean2 = 55

std = 40
sample_size = 100

standard_error = std/ (sample_size)**0.5

# Z scores for lower and upper 
Z1 = (50-mean1)/standard_error
Z1

Z2 = (50-mean2)/standard_error
Z2

# Probability
import scipy.stats as stats
P = stats.norm.cdf(Z2)+(1-stats.norm.cdf(Z1))
P
print("Probability of investigation is",(P*100).round(2),"%")

required_prob = 0.05
sample_size_required = ((std*(1.96))/(50-mean1)) ** 2
sample_size_required
