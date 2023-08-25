# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 05:51:34 2023

@author: 91879
"""
import pandas as pd
import numpy as np


# 1Q:-Look at the data given below. Plot the data, find the outliers and find out  
df = pd.read_csv("D:/Shiva Data Science/ExcelR Assignments/Basic Statistics_Level-2/1Q_Set-1.csv")
df

df["Measure X"].mean()
df["Measure X"].std()
df["Measure X"].var()

df.boxplot(column=["Measure X"],vert=False)   # Having one outlet at 0.9

#=============================================================================>>>>>>>>>>>>

# 4Q:- AT&T was running commercials in 1990 aimed at luring back customers who had switched to one of the other long-distance phone service providers. One such commercial shows a businessman trying to reach Phoenix and mistakenly getting Fiji, where a half-naked native on a beach responds incomprehensibly in Polynesian. When asked about this advertisement, AT&T admitted that the portrayed incident did not actually take place but added that this was an enactment of something that “could happen.” Suppose that one in 200 long-distance telephone calls is misdirected. What is the probability that at least one in five attempted telephone calls reaches the wrong number? (Assume independence of attempts.)

    # Given data
    Population_size = 200
    One_in_200_misdirected = 1/200
    Sample_size = 5
 ## At least one in five attempted telephone calls reaches the wrong number??
 from scipy.stats import binom

Bi = binom(n=Sample_size, p=One_in_200_misdirected)
BI = binom(n=5, p=200/1)

# P(x>=1)=(1,2,3,4,5)
Prob = 1-Bi.cdf(0)
print("At least one in five attempted telephone calls reaches the wrong number is ",(Prob*100).round(3),"%")


#=============================================================================>>>>>>>>>>>>
# 5Q: 5.Returns on a certain business venture, to the nearest $1,000, are known to follow the following probability distribution
        ## What is the good measure of the risk involved in a venture of this kind? Compute this measure
                ## Risk may be concidered as deviation
import numpy as np

X_values = [-2000, -1000, 0, 1000, 2000, 3000]
probabilities = [0.1, 0.1, 0.2, 0.2, 0.3, 0.1]

mean = np.average(X_values, weights=probabilities)
std_dev = np.sqrt(np.average((X_values - mean) ** 2, weights=probabilities))

print("Standard Deviation:", std_dev)   
