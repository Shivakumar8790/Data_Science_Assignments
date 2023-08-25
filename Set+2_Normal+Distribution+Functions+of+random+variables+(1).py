# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 14:34:01 2023

@author: 91879
"""
#======================================================================================================>>>>>>>>>>>>>>>
# 1.The time required for servicing transmissions is normally distributed with  = 45 minutes and  = 8 minutes. The service manager plans to have work begin on the transmission of a customer’s car 10 minutes after the car is dropped off and the customer is told that the car will be ready within 1 hour from drop-off. What is the probability that the service manager cannot meet his commitment? 
        # Given Data
        Sample_size = 45
        Standard_div = 8
        probability that the service manager cannot meet his commitment (>60)??


from scipy.stats import norm

nd =norm(45,8)
 ##P(x>60)

x =1-nd.cdf(60)
x

#======================================================================================================>>>>>>>>>>>>>>>

# 2.The current age (in years) of 400 clerical employees at an insurance claims processing center is normally distributed with mean  = 38 and Standard deviation  =6. For each statement below, please specify True/False. If false, briefly explain why.
        ## Given data 
        Total_size = 400
        mean = 38
        standard_div = 6
    
        ## A.More employees at the processing center are older than 44 than between 38 and 44.
       
        # X1 = older than 44
        # X2 = Between 38 to 44
       
        from scipy.stats import norm
        
       nor_dis = norm(38,6)
       #P(X1>44)
       X1 = 1- nor_dis.cdf(44)
       X1 
       
       #P(38>X2<44)
       X2 = nor_dis.cdf(44)-nor_dis.cdf(38)
       X2        
       
if X2 > X1:
    print("The statement is True")
else:
    print("The statement is false")
           
        
       ## B.A training program for employees under the age of 30 at the center would be expected to attract about 36 employees.
       
        nd = norm(38,6)
        # P(X<30)
        X = nd.cdf(30)
        X
# Number_of_employees_<_30(Y) = Prob(<30)*Sample size
Y = (X * Total_size)
Y 
if Y > 36:
    print("The statement is True")
else:
    print("The statement is false")
#======================================================================================================>>>>>>>>>>>>>>>

# 4.Let X ~ N(100, 202). Find two values, a and b, symmetric about the mean, such that the probability of the random variable taking a value between them is 0.99. 
    # Given Data 
    mean = 100
    var = 20**2
    Probability = 0.99
    # Find Min(a) and max(b) values in nor dis
    
    std_div = var**0.5
    std_div
# Finding Z-Scores
import scipy.stats as stats
Z1 = stats.norm.ppf((1-Probability)/2)
Z1

Z2 = stats.norm.ppf((1+Probability)/2)
Z2  

 # Finding Min(a) and max(b) values
 
 a = (Z1*std_div)+mean
 b = (Z2*std_div)+mean

print("Outputs are",a,"and",b)

#======================================================================================================>>>>>>>>>>>>>>>
# 5.Consider a company that has two different divisions. The annual profits from the two divisions are independent and have distributions Profit1 ~ N(5, 3^2) and Profit2 ~ N(7, 4^2) respectively. Both the profits are in $ Million. Answer the following questions about the total profit of the company in Rupees. Assume that $1 = Rs. 45

         # Given Data
         # Profit1 = P1
         # Profit2 = P2
         # Profits are in $ Million($1 = Rs. 45) Convert million to rs
         P1_mean = 5*45
         P1_Var = (3**2)
         P2_mean = 7*45
         P2_Var = (4**2)
         
         P1_std = (P1_Var**0.5)*45
         P1_std
         P2_std = (P2_Var**0.5)*45
         P2_std

    # A.Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
    Probability = 0.95
  import scipy.stats as stats
Range_P1 =  stats.norm.interval(Probability,P1_mean,P1_std)
Range_P1
Range_P2 =  stats.norm.interval(Probability,P2_mean,P2_std)
Range_P2    

    # B.Specify the 5th percentile of profit (in Rupees) for the company
    Total_mean = P1_mean+P2_mean
    Total_mean
    Total_std =((P1_std**2)+(P2_std**2))**0.5
    Total_std
    
    Percentile = stats.norm.ppf(0.05,Total_mean,Total_std)
    Percentile
                                         
    # C.Which of the two divisions has a larger probability of making a loss in a given year?