import numpy as np 
import matplotlib.pyplot as pp 
import seaborn

import urllib.request as req
req.urlretrieve('ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt', 'stations.txt')

stations = {}
for line in open('stations.txt', 'r'):
    if 'GSN' in line:
        fields = line.split()
        stations[fields[0]] = ' '.join(fields[4:])

def findstation(s):
    found = {code: name for code, name in stations.items() if s in name}
    print(found)

datastations = ['USW00022536', 'USW00023188', 'USW00014922', 'RSM00030710']

dly_delimiter = [11, 4, 2, 4] + [5, 1, 1, 1] * 31
dly_usecols = [1, 2, 3] + [4*i for i in range (1, 32)]
dly_type = [np.int32, np.int32, (np.str_,4)] +[np.int32] * 31
dly_names = ['year', 'month', 'obs'] + [str(day) for day in range()]

def parsefile(filename):
    return np.genfromtxt(filename, delimiter = dly_delimiter, usecols = dly_usecols, dtype = dly_type, names = dly_names)