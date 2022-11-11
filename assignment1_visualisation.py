# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 18:12:40 2022

@author: HP
"""
#importing all required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#defining functions that would be called later
def transaction_rate(transaction):
    """This function returns the total transaction rate and online transaction
    rate of first 10 weeks"""    
    trans_data = (transaction/np.sum(data['Transactions – total']))*1000
    return trans_data

def completion_rate(rate):
    """This function cleans the data by removing % from the values and setting
    the datatype as numeric"""
    #creating a list to store values from the column completion rate 
    #after cleaning
    data2 = []
    for values in rate:    
        values = values.replace('%','')
        data2.append(values)
    #creating a Dataframe from the list data2 which contains the 
    #completion rate of each week
    data2 = pd.DataFrame(data2, columns=['Completion_rate'])
    #setting  Data Frame type as integer
    data2 = data2.astype('int')      
    return data2['Completion_rate']

def completed_trans(percent):
    """This function returns the number of completed transactions
    in each week"""
    cmplt_trans = (percent/100)*data['Transactions – total']
    return cmplt_trans

def satisfaction_perc(satisfaction):
    """This function returns the satisfaction rates of  
    the total transactions in 10 weeks"""
    satisfaction_data = (np.sum(satisfaction)/
                         np.sum(data['Transactions – total']))*100
    return satisfaction_data

#Reading the first 10 rows of the data into a Data Frame
data = pd.read_csv('performance-data.csv', nrows=10)
                 
#Plotting the total transaction rate and online transaction rate of 
#of each week using line plot
plt.figure(figsize=(13,7))
#Calling the function transaction_rate  as an argument
plt.plot(data['Week commencing'], 
         transaction_rate(data['Transactions – total']), 
         label="total transaction")
plt.plot(data['Week commencing'],
         transaction_rate(data['Transactions – online']), 
         label="online transaction")
plt.legend()
plt.xlim('2021-11-08','2022-01-10')
plt.xlabel("week comencing")
plt.ylabel("transaction rate")
plt.title("Total  and Online transaction rates (08-11-2021 to 10-01-2022)")
plt.savefig("lineplot.png")
plt.show()  

#Creating a bar plot to compare total number of transaction and 
#number of completed transactions each week
plt.figure(figsize=(15,7))
x_axis = np.arange(len(data['Week commencing']))
plt.bar(x_axis - 0.15, data['Transactions – total'], width=0.3, 
        label="Total Transaction")
#Calling the function completion_rate inside another function completed_trans
#so that the data returned by the first function will be used by the 
#second function
plt.bar(x_axis + 0.15, 
        completed_trans(completion_rate(data['Completion rate'])), 
        width=0.3, label="Completed transaction")
plt.xticks(x_axis, data['Week commencing'])
plt.title("Total transactions Vs Completed transactions")
plt.legend()
plt.xlabel("Week comencing")
plt.ylabel("Number of Transaction")
plt.savefig("barchart.png")
plt.show()

#Creating a pie chart for comparing the rate of satisfaction
#in the total number transactions in the first 10 weeks
plt.figure(figsize=(13,10))
#Calling the function satisfaction_perc as an argument
plt.pie([satisfaction_perc(data['Very dissatisfied']),  
         satisfaction_perc(data['Neither satisfied or dissatisfied']), 
         satisfaction_perc(data['Satisfied']),
         satisfaction_perc(data['Very satisfied'])], 
         autopct=lambda p:'{:.0f}%'.format(p), shadow=True)
plt.legend( ['Very dissatisfied', 'Neither satisfied or dissatisfied', 
             'Satisfied', 'Very satisfied'],loc='best')
plt.axis('equal')
plt.title("Customer Satisfaction")
plt.savefig("piechart.png")
plt.show()
