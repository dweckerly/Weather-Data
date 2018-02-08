import numpy as np 
import matplotlib.pyplot as pp 
import seaborn

import urllib.request as req
req.urlretrieve('ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt', 'stations.txt')

open('stations.txt', 'r').readlines()[:10]