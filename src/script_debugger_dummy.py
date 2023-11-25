import datetime
import gc
import json
import os
import pprint
import warnings
from io import BytesIO

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import folium
import geopandas as gpd
import h5py
import matplotlib as mpl
import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np
import optuna
import pandas as pd
import seaborn as sns
import torch
import torch.nn as nn
import torch.optim as optim
import tqdm
from folium.plugins import HeatMap
from IPython.display import display
from scipy.interpolate import griddata
from selenium import webdriver
from skimage.transform import resize
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import ParameterGrid, train_test_split
from sklearn.preprocessing import MinMaxScaler

mpl.rcParams.update(mpl.rcParamsDefault)
warnings.filterwarnings("ignore")

%matplotlib inline