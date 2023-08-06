'''
Program to convert a pickle file to a CSV file

This program was written to convert a Matlab "mat" file containing data 
structures to a Comma, Separated, Value file (CSV) where each dataset is
stored in a separate CSV file. This was done because to provide users with
the example data in CSV, which is more widely preferred by novice Python users. 

The version of scipy.io that was available would not read 
the mat files, so I was forced to use the h5py library to read the mat file
stored in Hierarchical Data Format version 5 (HDF5), store the data structures
in corresponding dictionaries and save them in individual pickle files.

The data structures in the mat file have the format: ref.data, pred1.data, 
pred2.data, and pred3.data. Each of these data structures are written to a 
separate CSV file in column format with the first row a header containing the
name and units for the quantity. 

The reference data used in this example are cell concentrations of a
phytoplankton collected from cruise surveys at selected locations and 
time. The model predictions are from three different simulations that
have been space-time interpolated to the location and time of the sample
collection. Details on the contents of the dictionary (once loaded) can 
be obtained by simply executing the following two statements

>> key_to_value_lengths = {k:len(v) for k, v in ref.items()}
>> print(key_to_value_lengths)
{'units': 6, 'longitude': 57, 'jday': 57, 'date': 57, 'depth': 57, 
'station': 57, 'time': 57, 'latitude': 57, 'data': 57}

Author: Peter A. Rochford

Created on Jun 25, 2022
Revised on Apr 26, 2017   

@author: rochford.peter1@gmail.com
'''

import pandas
import pickle
from pprint import pprint

class Container(object): 
    
    def __init__(self, pred1, pred2, pred3, ref):
        self.pred1 = pred1
        self.pred2 = pred2
        self.pred3 = pred3
        self.ref = ref

if __name__ == '__main__':

    # Read data from pickle file
    with open('target_data.pkl3', 'rb') as f:
        object = pickle.load(f)
        
    # Report data type of object loaded from pickle file
    #print('type(object): ', type(object))

    # Print the variables of the object loaded from pickle file
    #pprint(vars(object))

    # Write each data structure to a CSV file
    df = pandas.DataFrame(object.pred1)
    df.to_csv(r'pred1.csv')
    
    # Write each data structure to a CSV file
    df = pandas.DataFrame(object.pred2)
    df.to_csv(r'pred2.csv')
    
    # Write each data structure to a CSV file
    df = pandas.DataFrame(object.pred3)
    df.to_csv(r'pred3.csv')
    
    # Write each data structure to a CSV file
    df = pandas.DataFrame(object.ref)
    df.to_csv(r'ref.csv')
    