# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:44:12 2020

@author: uchih
"""

import pandas as pd
import numpy as np
import sklearn as sk

np_data = np.genfromtxt(r'C:\Users\uchih\Desktop\Project_imp\dataset.csv',delimiter = ',',names = True)
print(np_data)

df = pd.ExcelFile(r"C:\Users\uchih\Desktop\Project_imp\dataset.xls")
print(df)

