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
        Symplectic, LLC
        www.thesymplectic.com

Created on Nov 23, 2016
Revised on Apr 26, 2017   

@author: prochford@thesymplectic.com
'''

# from Container import Container
import csv
import pickle
from pprint import pprint

class Container(object): 
    
    def __init__(self, pred1, pred2, pred3, ref):
        self.pred1 = pred1
        self.pred2 = pred2
        self.pred3 = pred3
        self.ref = ref

def save_pred_csv(name, data):
    
    header = ['latitude (deg)', 'longitude (deg)', 'depth (m)', 'julian day (day)', \
              'cell concentration (' + data['units'] +')']

    # open the file in the write mode
    file = open(name, 'w')
    
    # create the csv writer
    writer = csv.writer(file)
    
    # write the header
    writer.writerow(header)
    
    # Loop through data
    for i in range(len(data['latitude'])):
        writer.writerow([data['latitude'][i], data['longitude'][i], data['depth'][i], \
                         data['jday'][i], data['data'][i]])
    
    file.close()

def save_ref_csv(name, data):

    header = ['station', 'latitude (deg)', 'longitude (deg)', 'depth (m)', 'time', \
              'julian day (day)', 'cell concentration (' + data['units'] + ')']

    # open the file in the write mode
    file = open(name, 'w')
    
    # create the csv writer
    writer = csv.writer(file)
    
    # write the header
    writer.writerow(header)
    
    # Loop through data
    for i in range(len(data['latitude'])):
        writer.writerow([data['station'][i], data['latitude'][i], data['longitude'][i], \
                         data['depth'][i], data['time'][i], data['jday'][i], data['data'][i]])
    
    file.close()

if __name__ == '__main__':

    # Read data from pickle file
    with open('target_data.pkl3', 'rb') as f:
        data = pickle.load(f)
    
    # Report data type of object loaded from pickle file
    print('type(data): ', type(data))

    # Print the variables of the object loaded from pickle file
    pprint(vars(data))
    
    # Write data structures to CSV files
    save_pred_csv('pred1.csv',data.pred1)
    save_pred_csv('pred2.csv',data.pred2)
    save_pred_csv('pred3.csv',data.pred3)
    save_ref_csv('ref.csv',data.ref)
    