# Neftali Eunice Romero
''' Last updated: August 12, 2016
 this program converts the blued data to an hdf5 structure.
 the structure will have two files with multiple groups.
 the first file will contain the source data.
 the second file will contain the parsed data.
 the structure for the sourcedata wil contain the groups: events, signal, &sourcefiles
 the structure for the parsedata will contain the groups: appliance 1 through #
 each appliance will have a subgroup that contains each intstance, using the header to describe the instance.
 the data sets will contain the timestamps, currentA and CurrentB '''
# Variable library;
#    timestamps
#
#inputfile: location_001_iv_data_###.txt
#
#-------------------------------------------------------------------------------
import h5py
import numpy as np

FILE_HDF5_EVENTS = 'external_events.hdf5'
FILE_HDF5_SIGNAL = 'external_signal.hdf5'
#-------------------------------------------------------------------------------

# making ana array of the events list
events = np.genfromtxt("location_001_eventslist.txt", delimiter = ',',skip_header=0, names=True,usecols=(0,1,2), dtype=[('a25'),(np.uint8), ('a2')])
#print(events)
# creating the hdf5 file for the event list
with h5py.File(FILE_HDF5_EVENTS, 'w') as hf:
    g1 = hf.create_group('EVENTS')
    g1.create_dataset('event_list', data = events[:], compression= 'gzip', compression_opts=9)

# creating the hdf5 file for the master file of all signals
files = np.loadtxt('location_001_ivdata_129.txt', delimiter =',', skiprows=23, usecols=(0,1,2,3),dtype=float).T
X_Values = files[0]
Current_A = np.asarray(files[1],'f8')
Current_B = np.asarray(files[2],'f8')
Voltage_A = np.asarray(files[3], 'f8')

#print(X_Values)
#rint(Current_A)
#print(Current_B)
#print(Voltage_A)

with h5py.File(FILE_HDF5_SIGNAL, 'w') as hf:
    g1 = hf.create_group('SIGNAL')
    g1.attrs['Instances'] = 'NXinstance'
    g1.create_dataset('timestamps', data = X_Values)
    g1.create_dataset( 'CurrentA', data = Current_A)
    g1.create_dataset('CurrentB', data = Current_B)
    g1.create_dataset('VoltageA', data = Voltage_A)
