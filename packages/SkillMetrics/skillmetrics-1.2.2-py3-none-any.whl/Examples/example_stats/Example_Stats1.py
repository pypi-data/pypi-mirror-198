'''
How to create target and Taylor diagrams

A first example of how to create a side-by-side plot of a Taylor 
diagram (left panel) and a target diagram (right panel) given one set of
reference observations and multiple model predictions for the quantity.

This example produces a target diagram where the maximum scale for the bias 
and unnormalized RMSD (uRMSD) axis is increased, color properties are modified 
for the data points, and color & style properties are modified for the axes.

The Taylor diagram created has the RMSD label specified along with its 
orientation. 

All functions in the Skill Metrics library are designed to only work with
one-dimensional arrays, e.g. time series of observations at a selected
location. The one-dimensional data are read in as dictionaries from two 
OpenDSS CSV files. The plot is written to a file in Portable Network 
Graphics (PNG) format.

The reference data used in this example is a time series of Vd from a 
simple demonstration case: SimpleDemo_Mon_g1out_1.csv. The model data
is the same file to which random values in the range [0,1] have been added
simply to produce a difference that will yield non-zero statistics. 

Author: Peter A. Rochford
        Xator Corporation
        www.xatorcorp.com

Created on June 19, 2022

@author: peter.rochford@xatorcorp.com
'''

from get_time_series import get_time_series
from read_element_data import read_element_data
import matplotlib.pyplot as plt
import numpy as np
import skill_metrics as sm

if __name__ == '__main__':
    example = 'Example_stats1'
    
    # Close any previously open graphics windows
    # ToDo: fails to work within Eclipse
    plt.close('all')
        
    # Read data from OpenDSS CSV files
    filename = 'test_cases_delphi/SimpleDemo_Mon_g1out_1'
    data_delphi = read_element_data(filename)
    filename = 'test_cases_linux/SimpleDemo_Mon_g1out_1'
    data_linux = read_element_data(filename)
    filename = 'test_cases_windows/SimpleDemo_Mon_g1out_1'
    data_windows = read_element_data(filename)
    
    # State quantities to be retrieved from OpenDSS CSV files
    variables = ['Theta (Deg)']
    tsdata_delphi = get_time_series(variables,data_delphi)
    tsdata_linux = get_time_series(variables,data_linux)
    tsdata_windows = get_time_series(variables,data_windows)

    # Calculate statistics for Taylor diagram
    # The first array element (e.g. taylor_stats1[0]) corresponds to the 
    # reference series while the second and subsequent elements
    # (e.g. taylor_stats1[1:]) are those for the predicted series.
    target_stats_linux = sm.target_statistics(tsdata_linux['Theta'],tsdata_delphi['Theta'],'values')
    target_stats_windows = sm.target_statistics(tsdata_windows['Theta'],tsdata_delphi['Theta'],'values')
    
    # Store statistics in arrays
    bias = np.array([target_stats_linux['bias'], target_stats_windows['bias']])
    center_rmsd = np.array([target_stats_linux['crmsd'], target_stats_windows['crmsd']])
    rmsd = np.array([target_stats_linux['rmsd'], target_stats_windows['rmsd']])

    # Calculate statistics for Taylor diagram
    # The first array element (e.g. taylor_stats1[0]) corresponds to the 
    # reference series while the second and subsequent elements
    # (e.g. taylor_stats1[1:]) are those for the predicted series.
    taylor_stats_linux = sm.taylor_statistics(tsdata_linux['Theta'],tsdata_delphi['Theta'],'values')
    taylor_stats_windows = sm.taylor_statistics(tsdata_windows['Theta'],tsdata_delphi['Theta'],'values')
    
    # Store statistics in arrays
    sdev = np.array([taylor_stats_linux['sdev'][0], taylor_stats_linux['sdev'][1],
                     taylor_stats_windows['sdev'][1]])
    crmsd = np.array([taylor_stats_linux['crmsd'][0], taylor_stats_linux['crmsd'][1],
                     taylor_stats_windows['crmsd'][1]])
    ccoef = np.array([taylor_stats_linux['ccoef'][0], taylor_stats_linux['ccoef'][1],
                     taylor_stats_windows['ccoef'][1]])

    # Define plot area as 1 row with 2 columns
    fig, ax = plt.subplots(1,2,figsize =(11,8.5))
    subplot_axis = ax.flatten()
            
    '''
    Produce the target diagram

    For an exhaustive list of options to customize your diagram, 
    please call the function at a Python command line:
    >> target_diagram
    '''
    # Specify labels for points in a list
    label = ['Linux', 'Windows']
    plt.axes(ax[1]) # set right subplot for target diagram
    sm.target_diagram(bias,center_rmsd,rmsd, markerLabel = label, 
                      markerLegend = 'on', alpha = 0.0, circleLineSpec = '--b')

    '''
    Produce the Taylor diagram

    Label the points and change the axis options for SDEV, CRMSD, and CCOEF.

    For an exhaustive list of options to customize your diagram, 
    please call the function at a Python command line:
    >> taylor_diagram
    '''
    # Specify labels for points in a list
    label = ['Delphi', 'Linux', 'Windows']
    plt.axes(ax[0]) # set left subplot for Taylor diagram
    sm.taylor_diagram(sdev,crmsd,ccoef, labelRMS = 'RMSE', 
                      titlermsdangle = 145.0, markerobs = 'd',
                      titleobs = 'Ref', markerLabel = label, 
                      markerLegend = 'on', alpha = 0.0)
    
    # Adjust spacing between subplots to minimize the overlaps.
    plt.tight_layout()

    # Write plot to file
    plt.savefig(example + '.png')

    # Write plot to Portable Data Format (PDF) file
    # plt.savefig(example + '.pdf')

    # Show plot
    plt.show()
