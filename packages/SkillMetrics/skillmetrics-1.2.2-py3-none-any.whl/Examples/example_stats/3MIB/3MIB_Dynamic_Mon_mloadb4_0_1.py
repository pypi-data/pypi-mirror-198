'''
3MIB test case: create target and Taylor diagrams comparing
all voltages in a power grid network containing ?? buses and ?? nodes 
against results from a Delphi language version.

Example of how to create target and Taylor diagrams

Create a side-by-side plot of a Taylor 
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

The reference data used in this example are the voltages produced from the 
Delphi language version: 3MIB_Dynamic_Mon_mgen1_0_1.csv.

Author: Peter A. Rochford
        Xator Corporation
        www.xatorcorp.com

Created on August 14, 2022

@author: peter.rochford@xatorcorp.com
'''

from get_time_series import get_time_series
from read_element_data import read_element_data
import matplotlib.pyplot as plt
import numpy as np
#import opendss_scivis as osv
import skill_metrics as sm

if __name__ == '__main__':
    # Close any previously open graphics windows
    plt.close('all')
        
    # Read data from OpenDSS CSV files
    filename = 'DSS/3MIB_Dynamic_Mon_mloadb4_0_1'
    data_delphi = read_element_data(filename)
    filename = 'DSSX/3MIB_Dynamic_Mon_mloadb4_0_1'
    data_linux = read_element_data(filename)
    
    # Plot diagrams for voltages in file
    example = '3MIB_Dynamic_Mon_mloadb4_0_1'
    
    # State quantities to be retrieved from OpenDSS CSV files
    variables = ['V1', 'V2', 'V3']
    tsdata_delphi = get_time_series(variables,data_delphi)
    tsdata_linux = get_time_series(variables,data_linux)

    # Calculate statistics for target diagram
    target_stats_linux1 = sm.target_statistics(tsdata_linux['V1'],tsdata_delphi['V1'],'values')
    target_stats_linux2 = sm.target_statistics(tsdata_linux['V2'],tsdata_delphi['V2'],'values')
    target_stats_linux3 = sm.target_statistics(tsdata_linux['V3'],tsdata_delphi['V3'],'values')
    
    # Store statistics in arrays
    bias = np.array([target_stats_linux1['bias'], target_stats_linux2['bias'],
                     target_stats_linux3['bias']])
    center_rmsd = np.array([target_stats_linux1['crmsd'], target_stats_linux2['crmsd'],
                     target_stats_linux3['crmsd']])
    rmsd = np.array([target_stats_linux1['rmsd'], target_stats_linux2['rmsd'],
                     target_stats_linux3['rmsd']])

    # Calculate statistics for Taylor diagram
    # The first array element (e.g. taylor_stats1[0]) corresponds to the 
    # reference series while the second and subsequent elements
    # (e.g. taylor_stats1[1:]) are those for the predicted series.
    taylor_stats_linux1 = sm.taylor_statistics(tsdata_linux['V1'],tsdata_delphi['V1'],'values')
    taylor_stats_linux2 = sm.taylor_statistics(tsdata_linux['V2'],tsdata_delphi['V2'],'values')
    taylor_stats_linux3 = sm.taylor_statistics(tsdata_linux['V3'],tsdata_delphi['V3'],'values')
    
    # Store statistics in arrays
    sdev = np.array([taylor_stats_linux1['sdev'][0], taylor_stats_linux1['sdev'][1],
                     taylor_stats_linux2['sdev'][1], taylor_stats_linux3['sdev'][1]])
    crmsd = np.array([taylor_stats_linux1['crmsd'][0], taylor_stats_linux1['crmsd'][1],
                     taylor_stats_linux2['crmsd'][1], taylor_stats_linux3['crmsd'][1]])
    ccoef = np.array([taylor_stats_linux1['ccoef'][0], taylor_stats_linux1['ccoef'][1],
                     taylor_stats_linux2['ccoef'][1], taylor_stats_linux3['ccoef'][1]])

    # Define plot area as 1 row with 2 columns
    fig, ax = plt.subplots(1,2,figsize =(11,8.5))
    subplot_axis = ax.flatten()
            
    '''
    Produce the target diagram

    For an exhaustive list of options to customize your diagram, 
    please call the function at a Python command line:
    >> target_diagram
    '''
    # Specify labels for points in a list.
    label = ['V1', 'V2', 'V3']
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
    # Specify labels for points in a list (D for Delphi, L for linux, and W for Windows).
    label = ['Delphi', 'V1', 'V2', 'V3']
    plt.axes(ax[0]) # set left subplot for Taylor diagram
    sm.taylor_diagram(sdev,crmsd,ccoef, labelRMS = 'RMSE', 
                      titlermsdangle = 145.0, markerLabel = label, 
                      markerLegend = 'on', alpha = 0.0)
    
    # Adjust spacing between subplots to minimize the overlaps.
    plt.tight_layout()


    # Plot diagrams for voltage angles in file
    
    # State quantities to be retrieved from OpenDSS CSV files
    variables = ['VAngle1', 'VAngle2', 'VAngle3']
    tsdata_delphi = get_time_series(variables,data_delphi)
    tsdata_linux = get_time_series(variables,data_linux)

    # Calculate statistics for target diagram
    target_stats_linux1 = sm.target_statistics(tsdata_linux['VAngle1'],tsdata_delphi['VAngle1'],'values')
    target_stats_linux2 = sm.target_statistics(tsdata_linux['VAngle2'],tsdata_delphi['VAngle2'],'values')
    target_stats_linux3 = sm.target_statistics(tsdata_linux['VAngle3'],tsdata_delphi['VAngle3'],'values')
    
    # Store statistics in arrays
    bias = np.array([target_stats_linux1['bias'], target_stats_linux2['bias'],
                     target_stats_linux3['bias']])
    center_rmsd = np.array([target_stats_linux1['crmsd'], target_stats_linux2['crmsd'],
                     target_stats_linux3['crmsd']])
    rmsd = np.array([target_stats_linux1['rmsd'], target_stats_linux2['rmsd'],
                     target_stats_linux3['rmsd']])

    # Calculate statistics for Taylor diagram
    # The first array element (e.g. taylor_stats1[0]) corresponds to the 
    # reference series while the second and subsequent elements
    # (e.g. taylor_stats1[1:]) are those for the predicted series.
    taylor_stats_linux1 = sm.taylor_statistics(tsdata_linux['VAngle1'],tsdata_delphi['VAngle1'],'values')
    taylor_stats_linux2 = sm.taylor_statistics(tsdata_linux['VAngle2'],tsdata_delphi['VAngle2'],'values')
    taylor_stats_linux3 = sm.taylor_statistics(tsdata_linux['VAngle3'],tsdata_delphi['VAngle3'],'values')
    
    # Store statistics in arrays
    sdev = np.array([taylor_stats_linux1['sdev'][0], taylor_stats_linux1['sdev'][1],
                     taylor_stats_linux2['sdev'][1], taylor_stats_linux3['sdev'][1]])
    crmsd = np.array([taylor_stats_linux1['crmsd'][0], taylor_stats_linux1['crmsd'][1],
                     taylor_stats_linux2['crmsd'][1], taylor_stats_linux3['crmsd'][1]])
    ccoef = np.array([taylor_stats_linux1['ccoef'][0], taylor_stats_linux1['ccoef'][1],
                     taylor_stats_linux2['ccoef'][1], taylor_stats_linux3['ccoef'][1]])

    # Define plot area as 1 row with 2 columns
    fig, ax = plt.subplots(1,2,figsize =(11,8.5))
    subplot_axis = ax.flatten()
            
    '''
    Produce the target diagram

    For an exhaustive list of options to customize your diagram, 
    please call the function at a Python command line:
    >> target_diagram
    '''
    # Specify labels for points in a list.
    label = ['VAngle1', 'VAngle2', 'VAngle3']
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
    # Specify labels for points in a list (D for Delphi, L for linux, and W for Windows).
    label = ['Delphi', 'VAngle1', 'VAngle2', 'VAngle3']
    plt.axes(ax[0]) # set left subplot for Taylor diagram
    sm.taylor_diagram(sdev,crmsd,ccoef, labelRMS = 'RMSE', 
                      titlermsdangle = 145.0, markerLabel = label, 
                      markerLegend = 'on', alpha = 0.0)
    
    # Adjust spacing between subplots to minimize the overlaps.
    plt.tight_layout()

    
    # Plot diagrams for currents in file
    
    # State quantities to be retrieved from OpenDSS CSV files
    variables = ['I1', 'I2', 'I3']
    tsdata_delphi = get_time_series(variables,data_delphi)
    tsdata_linux = get_time_series(variables,data_linux)

    # Calculate statistics for target diagram
    target_stats_linux1 = sm.target_statistics(tsdata_linux['I1'],tsdata_delphi['I1'],'values')
    target_stats_linux2 = sm.target_statistics(tsdata_linux['I2'],tsdata_delphi['I2'],'values')
    target_stats_linux3 = sm.target_statistics(tsdata_linux['I3'],tsdata_delphi['I3'],'values')
    
    # Store statistics in arrays
    bias = np.array([target_stats_linux1['bias'], target_stats_linux2['bias'],
                     target_stats_linux3['bias']])
    center_rmsd = np.array([target_stats_linux1['crmsd'], target_stats_linux2['crmsd'],
                     target_stats_linux3['crmsd']])
    rmsd = np.array([target_stats_linux1['rmsd'], target_stats_linux2['rmsd'],
                     target_stats_linux3['rmsd']])

    # Calculate statistics for Taylor diagram
    # The first array element (e.g. taylor_stats1[0]) corresponds to the 
    # reference series while the second and subsequent elements
    # (e.g. taylor_stats1[1:]) are those for the predicted series.
    taylor_stats_linux1 = sm.taylor_statistics(tsdata_linux['I1'],tsdata_delphi['I1'],'values')
    taylor_stats_linux2 = sm.taylor_statistics(tsdata_linux['I2'],tsdata_delphi['I2'],'values')
    taylor_stats_linux3 = sm.taylor_statistics(tsdata_linux['I3'],tsdata_delphi['I3'],'values')
    
    # Store statistics in arrays
    sdev = np.array([taylor_stats_linux1['sdev'][0], taylor_stats_linux1['sdev'][1],
                     taylor_stats_linux2['sdev'][1], taylor_stats_linux3['sdev'][1]])
    crmsd = np.array([taylor_stats_linux1['crmsd'][0], taylor_stats_linux1['crmsd'][1],
                     taylor_stats_linux2['crmsd'][1], taylor_stats_linux3['crmsd'][1]])
    ccoef = np.array([taylor_stats_linux1['ccoef'][0], taylor_stats_linux1['ccoef'][1],
                     taylor_stats_linux2['ccoef'][1], taylor_stats_linux3['ccoef'][1]])

    # Define plot area as 1 row with 2 columns
    fig, ax = plt.subplots(1,2,figsize =(11,8.5))
    subplot_axis = ax.flatten()
            
    '''
    Produce the target diagram

    For an exhaustive list of options to customize your diagram, 
    please call the function at a Python command line:
    >> target_diagram
    '''
    # Specify labels for points in a list.
    label = ['I1', 'I2', 'I3']
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
    # Specify labels for points in a list (D for Delphi, L for linux, and W for Windows).
    label = ['Delphi', 'I1', 'I2', 'I3']
    plt.axes(ax[0]) # set left subplot for Taylor diagram
    sm.taylor_diagram(sdev,crmsd,ccoef, labelRMS = 'RMSE', 
                      titlermsdangle = 145.0, markerLabel = label, 
                      markerLegend = 'on', alpha = 0.0)
    
    # Adjust spacing between subplots to minimize the overlaps.
    plt.tight_layout()


    # Plot diagrams for current angles in file
    
    # State quantities to be retrieved from OpenDSS CSV files
    variables = ['IAngle1', 'IAngle2', 'IAngle3']
    tsdata_delphi = get_time_series(variables,data_delphi)
    tsdata_linux = get_time_series(variables,data_linux)

    # Calculate statistics for target diagram
    target_stats_linux1 = sm.target_statistics(tsdata_linux['IAngle1'],tsdata_delphi['IAngle1'],'values')
    target_stats_linux2 = sm.target_statistics(tsdata_linux['IAngle2'],tsdata_delphi['IAngle2'],'values')
    target_stats_linux3 = sm.target_statistics(tsdata_linux['IAngle3'],tsdata_delphi['IAngle3'],'values')
    
    # Store statistics in arrays
    bias = np.array([target_stats_linux1['bias'], target_stats_linux2['bias'],
                     target_stats_linux3['bias']])
    center_rmsd = np.array([target_stats_linux1['crmsd'], target_stats_linux2['crmsd'],
                     target_stats_linux3['crmsd']])
    rmsd = np.array([target_stats_linux1['rmsd'], target_stats_linux2['rmsd'],
                     target_stats_linux3['rmsd']])

    # Calculate statistics for Taylor diagram
    # The first array element (e.g. taylor_stats1[0]) corresponds to the 
    # reference series while the second and subsequent elements
    # (e.g. taylor_stats1[1:]) are those for the predicted series.
    taylor_stats_linux1 = sm.taylor_statistics(tsdata_linux['IAngle1'],tsdata_delphi['IAngle1'],'values')
    taylor_stats_linux2 = sm.taylor_statistics(tsdata_linux['IAngle2'],tsdata_delphi['IAngle2'],'values')
    taylor_stats_linux3 = sm.taylor_statistics(tsdata_linux['IAngle3'],tsdata_delphi['IAngle3'],'values')
    
    # Store statistics in arrays
    sdev = np.array([taylor_stats_linux1['sdev'][0], taylor_stats_linux1['sdev'][1],
                     taylor_stats_linux2['sdev'][1], taylor_stats_linux3['sdev'][1]])
    crmsd = np.array([taylor_stats_linux1['crmsd'][0], taylor_stats_linux1['crmsd'][1],
                     taylor_stats_linux2['crmsd'][1], taylor_stats_linux3['crmsd'][1]])
    ccoef = np.array([taylor_stats_linux1['ccoef'][0], taylor_stats_linux1['ccoef'][1],
                     taylor_stats_linux2['ccoef'][1], taylor_stats_linux3['ccoef'][1]])

    # Define plot area as 1 row with 2 columns
    fig, ax = plt.subplots(1,2,figsize =(11,8.5))
    subplot_axis = ax.flatten()
            
    '''
    Produce the target diagram

    For an exhaustive list of options to customize your diagram, 
    please call the function at a Python command line:
    >> target_diagram
    '''
    # Specify labels for points in a list.
    label = ['IAngle1', 'IAngle2', 'IAngle3']
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
    # Specify labels for points in a list (D for Delphi, L for linux, and W for Windows).
    label = ['Delphi', 'IAngle1', 'IAngle2', 'IAngle3']
    plt.axes(ax[0]) # set left subplot for Taylor diagram
    sm.taylor_diagram(sdev,crmsd,ccoef, labelRMS = 'RMSE', 
                      titlermsdangle = 145.0, markerLabel = label, 
                      markerLegend = 'on', alpha = 0.0)
    
    # Adjust spacing between subplots to minimize the overlaps.
    plt.tight_layout()

    # Write plots to Portable Network Graphic (PNG) file(s)
    sm.save_figures(example,'.png')

    # Write plots to Portable Data Format (PDF) file
    sm.save_figures(example,'.pdf')

    # Show plot
    plt.show()
