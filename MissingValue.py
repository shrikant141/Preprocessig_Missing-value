# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:53:23 2021

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


claimants = pd.read_csv('F:/DataSets/claimants.csv')

# check for count of NA value
claimants.isna().sum()

##### Mean and Median imputer are used for numeric data. 

from sklearn.impute import SimpleImputer

##### Mean Imputer 
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
claimants["CLMSEX"] = pd.DataFrame(mean_imputer.fit_transform(claimants[["CLMSEX"]]))
claimants["CLMSEX"].isna().sum()  

claimants["CLMINSUR"] = pd.DataFrame(mean_imputer.fit_transform(claimants[["CLMINSUR"]]))
claimants["CLMINSUR"].isna().sum()  

##### Median Imputer
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
claimants["SEATBELT"] = pd.DataFrame(median_imputer.fit_transform(claimants[["SEATBELT"]]))
claimants["SEATBELT"].isna().sum() 

claimants["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(claimants[["CLMAGE"]]))
claimants["CLMAGE"].isna().sum() 
