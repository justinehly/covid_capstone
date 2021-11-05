import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sbs
import copy

# change OS
os.chdir(r'C:\Users\justi\OneDrive - Southern Methodist University\Capstone\data')
df = pd.read_csv('OxCGRT_latest.csv', low_memory=False)
covid = copy.deepcopy(df[df.CountryCode == 'USA'])

covid.Date