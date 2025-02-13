import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Games\DA Project\MM_Price Analysis.csv")
df.dtypes

# mean
mean = df['Price_Aluminium_per_Ton'].mean() #2518.15478
print(mean)

mean = df['Price_Tin_per_Ounce'].mean() #2502.21636
print(mean)

mean = df['Price_Copper_per_Ton'].mean() #2504.96502
print(mean)

mean = df['Price_Iron_per_Ounce'].mean() #2533.41027
print(mean)

mean = df['Price_Steel_per_Ton'].mean() #2534.98675
print(mean)

mean = df['Inflation_Rate_Percentage'].mean() #2489.16407
print(mean)

mean = df['Aluminium_Price_Inflation_Adjusted'].mean() #2438.13546
print(mean)

mean = df['Tin_Price_Inflation_Adjusted'].mean() #2477.11036
print(mean)

mean = df['Copper_Price_Inflation_Adjusted'].mean() #2626.28827
print(mean)

mean = df['Iron_Price_Inflation_Adjusted'].mean() #2569.26441
print(mean)

mean = df['Steel_Price_Inflation_Adjusted'].mean() #2434.05624
print(mean)

mean = df['Price_Chromium_Adjusted'].mean() #2469.82900
print(mean)

#--------------------------------------------------------------------------------------------#
#Median

median = df['Price_Aluminium_per_Ton'].median() #2553.16
print(median)

median = df['Price_Tin_per_Ounce'].median() #2517.68
print(median)

median = df['Price_Copper_per_Ton'].median() #2499.735
print(median)

median = df['Price_Iron_per_Ounce'].median() #2592.76
print(median)

median = df['Price_Steel_per_Ton'].median() #2522.8
print(median)

median = df['Inflation_Rate_Percentage'].median() #2503.47500
print(median)

median = df['Aluminium_Price_Inflation_Adjusted'].median() #2393.885
print(median)

median = df['Tin_Price_Inflation_Adjusted'].median() #2402.61
print(median)

median = df['Copper_Price_Inflation_Adjusted'].median() #2578.39
print(median)

median = df['Iron_Price_Inflation_Adjusted'].median() #2661.19
print(median)

median = df['Steel_Price_Inflation_Adjusted'].median() #2442.17
print(median)

median = df['Price_Chromium_Adjusted'].median() #2417.81
print(median)

#--------------------------------------------------------------------------------------------#
# mode

mode = df['Price_Aluminium_per_Ton'].mode()
print(mode)

mode  = df['Price_Tin_per_Ounce'].mode()
print(mode)

mode  = df['Price_Copper_per_Ton'].mode()
print(mode)

mode  = df['Price_Iron_per_Ounce'].mode()
print(mode)

mode  = df['Price_Steel_per_Ton'].mode()
print(mode)

mode  = df['Inflation_Rate_Percentage'].mode()
print(mode)

mode  = df['Aluminium_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Tin_Price_Inflation_Adjusted'].mode()
print(mode) 

mode  = df['Copper_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Iron_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Steel_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Price_Chromium_Adjusted'].mode()
print(mode)

#--------------------------------------------------------------------------------------------#
# Standard Deviation 

df = pd.read_csv(r"C:\Games\DA Project\MM_Price Analysis.csv")

Price_Aluminium_per_Ton_stddev = df['Price_Aluminium_per_Ton'].std()
print("Standard Deviation of Price_Aluminium_per_Ton:", Price_Aluminium_per_Ton_stddev) # 1450.348617

Price_Tin_per_Ounce_stddev = df['Price_Tin_per_Ounce'].std()
print("Standard Deviation of Price_Tin_per_Ounce:", Price_Tin_per_Ounce_stddev) #1446.575290

Price_Copper_per_Ton_stddev = df['Price_Copper_per_Ton'].std()
print("Standard Deviation of Price_Copper_per_Ton:", Price_Copper_per_Ton_stddev) #1437.954209

Price_Iron_per_Ounce_stddev = df['Price_Iron_per_Ounce'].std()
print("Standard Deviation of Price_Iron_per_Ounce:", Price_Iron_per_Ounce_stddev) #1434.785939

Price_Steel_per_Ton_stddev = df['Price_Steel_per_Ton'].std()
print("Standard Deviation of Price_Steel_per_Ton:", Price_Steel_per_Ton_stddev) #1418.879415

Inflation_Rate_Percentage_stddev = df['Inflation_Rate_Percentage'].std()
print("Standard Deviation of Inflation_Rate_Percentage:", Inflation_Rate_Percentage_stddev) #1440.956309

Aluminium_Price_Inflation_Adjusted_stddev = df['Aluminium_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Aluminium_Price_Inflation_Adjusted:", Aluminium_Price_Inflation_Adjusted_stddev) #1400.362937

Tin_Price_Inflation_Adjusted_stddev = df['Tin_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Tin_Price_Inflation_Adjusted:", Tin_Price_Inflation_Adjusted_stddev) #1407.023348

Copper_Price_Inflation_Adjusted_stddev = df['Copper_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Copper_Price_Inflation_Adjusted:", Copper_Price_Inflation_Adjusted_stddev) #2710.395402

Iron_Price_Inflation_Adjusted_stddev = df['Iron_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Iron_Price_Inflation_Adjusted:",Iron_Price_Inflation_Adjusted_stddev) #1443.489069

Steel_Price_Inflation_Adjusted_stddev = df['Steel_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Steel_Price_Inflation_Adjusted:", Steel_Price_Inflation_Adjusted_stddev) #1422.483354

Price_Chromium_Adjusted_stddev = df['Price_Chromium_Adjusted'].std()
print("Standard Deviation of Price_Chromium_Adjusted:", Price_Chromium_Adjusted_stddev) # 1447.522929


#--------------------------------------------------------------------------------------------#
# Range 
Price_Aluminium_per_Ton_range = df['Price_Aluminium_per_Ton'].max() - df['Price_Aluminium_per_Ton'].min() #4983.3
print("Range of Price_Aluminium_per_Ton:", Price_Aluminium_per_Ton_range)
    
Price_Tin_per_Ounce_range = df['Price_Tin_per_Ounce'].max() - df['Price_Tin_per_Ounce'].min() #4983.03
print("Range of Price_Tin_per_Ounce:", Price_Tin_per_Ounce_range)

Price_Copper_per_Ton_range = df['Price_Copper_per_Ton'].max() - df['Price_Copper_per_Ton'].min() #4967.54
print("Range of Price_Copper_per_Ton:", Price_Copper_per_Ton_range)

Price_Iron_per_Ounce_range = df['Price_Iron_per_Ounce'].max() - df['Price_Iron_per_Ounce'].min() #4958.65
print("Range of Price_Iron_per_Ounce:", Price_Iron_per_Ounce_range)

Price_Steel_per_Ton_range = df['Price_Steel_per_Ton'].max() - df['Price_Steel_per_Ton'].min() #4982.45
print("Range of Price_Steel_per_Ton:", Price_Steel_per_Ton_range)

Inflation_Rate_Percentage_range = df['Inflation_Rate_Percentage'].max() - df['Inflation_Rate_Percentage'].min() #4965.16
print("Range of Inflation_Rate_Percentage:",Inflation_Rate_Percentage_range)

Aluminium_Price_Inflation_Adjusted_range = df['Aluminium_Price_Inflation_Adjusted'].max() - df['Aluminium_Price_Inflation_Adjusted'].min() #4965.16
print("Range of Aluminium_Price_Inflation_Adjusted:",Aluminium_Price_Inflation_Adjusted_range)

Tin_Price_Inflation_Adjusted_range = df['Tin_Price_Inflation_Adjusted'].max() - df['Tin_Price_Inflation_Adjusted'].min() #4960.5599
print("Range of Tin_Price_Inflation_Adjusted:", Tin_Price_Inflation_Adjusted_range)

Copper_Price_Inflation_Adjusted_range = df['Copper_Price_Inflation_Adjusted'].max() - df['Copper_Price_Inflation_Adjusted'].min() #43562.8176
print("Range of Copper_Price_Inflation_Adjusted:",Copper_Price_Inflation_Adjusted_range)

Iron_Price_Inflation_Adjusted_range = df['Iron_Price_Inflation_Adjusted'].max() - df['Iron_Price_Inflation_Adjusted'].min() #4967.61000
print("Range of Iron_Price_Inflation_Adjusted:",Iron_Price_Inflation_Adjusted_range)

Steel_Price_Inflation_Adjusted_range = df['Steel_Price_Inflation_Adjusted'].max() - df['Steel_Price_Inflation_Adjusted'].min() #4976.38999
print("Range of Steel_Price_Inflation_Adjusted:", Steel_Price_Inflation_Adjusted_range)

Price_Chromium_Adjusted_range = df['Price_Chromium_Adjusted'].max() - df['Price_Chromium_Adjusted'].min() #4984.88
print("Range of Price_Chromium_Adjusted:", Price_Chromium_Adjusted_range)

#-------------------------------------------------------------------------------------------------------#
# Variance 
Price_Aluminium_per_Ton_variance = df['Price_Aluminium_per_Ton'].var()
print("Variance of  Price_Aluminium_per_Ton:",Price_Aluminium_per_Ton_variance) #2103511.1095

Price_Tin_per_Ounce_variance = df['Price_Tin_per_Ounce'].var()
print("Variance of  Price_Tin_per_Ounce:",Price_Tin_per_Ounce_variance) #2092580.0685

Price_Copper_per_Ton_variance = df['Price_Copper_per_Ton'].var()
print("Variance of  Price_Copper_per_Ton:",Price_Copper_per_Ton_variance) #2067712.3082

Price_Iron_per_Ounce_variance = df['Price_Iron_per_Ounce'].var()
print("Variance of  Price_Iron_per_Ounce:",Price_Iron_per_Ounce_variance) #2058610.69084

Price_Steel_per_Ton_variance = df['Price_Steel_per_Ton'].var()
print("Variance of  Price_Steel_per_Ton:",Price_Steel_per_Ton_variance) #2013218.7931

Inflation_Rate_Percentage_variance = df['Inflation_Rate_Percentage'].var()
print("Variance of   Inflation_Rate_Percentage:",Inflation_Rate_Percentage_variance) #2076355.0843

Aluminium_Price_Inflation_Adjusted_variance = df['Aluminium_Price_Inflation_Adjusted'].var()
print("Variance of  Aluminium_Price_Inflation_Adjusted:",Aluminium_Price_Inflation_Adjusted_variance) #1961016.3547

Tin_Price_Inflation_Adjusted_variance = df['Tin_Price_Inflation_Adjusted'].var()
print("Variance of  Tin_Price_Inflation_Adjusted:",Tin_Price_Inflation_Adjusted_variance) #1979714.7012

Copper_Price_Inflation_Adjusted_variance = df['Copper_Price_Inflation_Adjusted'].var()
print("Variance of  Copper_Price_Inflation_Adjusted:",Copper_Price_Inflation_Adjusted_variance) #7346243.23299

Iron_Price_Inflation_Adjusted_variance = df['Iron_Price_Inflation_Adjusted'].var()
print("Variance of  Iron_Price_Inflation_Adjusted:",Iron_Price_Inflation_Adjusted_variance) #2083660.69302

Steel_Price_Inflation_Adjusted_variance = df['Steel_Price_Inflation_Adjusted'].var()
print("Variance of  Steel_Price_Inflation_Adjusted:",Steel_Price_Inflation_Adjusted_variance) #2023458.8912

Price_Chromium_Adjusted_variance = df['Price_Chromium_Adjusted'].var()
print("Variance of  Price_Chromium_Adjusted:",Price_Chromium_Adjusted_variance) #2095322.6299

#-------------------------------------------------------------------------------------------------------#
#Skewness
skewness = df['Price_Aluminium_per_Ton'].skew() #-0.0383148
print(skewness)

skewness = df['Price_Tin_per_Ounce'].skew() #0.01694657
print(skewness)


skewness = df['Price_Copper_per_Ton'].skew() #0.001250150
print(skewness)


skewness = df['Price_Iron_per_Ounce'].skew() #-0.04725249
print(skewness)


skewness = df['Price_Steel_per_Ton'].skew() #0.00396943
print(skewness)


skewness = df['Inflation_Rate_Percentage'].skew() #0.017444392
print(skewness)


skewness = df['Aluminium_Price_Inflation_Adjusted'].skew() #0.07129939
print(skewness)


skewness = df['Tin_Price_Inflation_Adjusted'].skew() #0.03984119
print(skewness)


skewness = df['Copper_Price_Inflation_Adjusted'].skew() #9.19106734
print(skewness)


skewness = df['Iron_Price_Inflation_Adjusted'].skew() #-0.10244472
print(skewness)


skewness = df['Steel_Price_Inflation_Adjusted'].skew() #0.034369200
print(skewness)


skewness = df['Price_Chromium_Adjusted'].skew() #0.03703385
print(skewness)

#-------------------------------------------------------------------------------------------------------#
#Kurtosis
kurtosis = df['Price_Aluminium_per_Ton'].kurtosis() #-1.19978349
print(kurtosis)

kurtosis = df['Price_Tin_per_Ounce'].kurtosis() #-1.22655353
print(kurtosis)


kurtosis = df['Price_Copper_per_Ton'].kurtosis() #-1.17217812
print(kurtosis)


kurtosis = df['Price_Iron_per_Ounce'].kurtosis() #-1.157848272
print(kurtosis)


kurtosis = df['Price_Steel_per_Ton'].kurtosis() #-1.17268793
print(kurtosis)


kurtosis = df['Inflation_Rate_Percentage'].kurtosis() #-1.20127732
print(kurtosis)


kurtosis = df['Aluminium_Price_Inflation_Adjusted'].kurtosis() #-1.1919817006
print(kurtosis)


kurtosis = df['Tin_Price_Inflation_Adjusted'].kurtosis() #-1.18474732
print(kurtosis)


kurtosis = df['Copper_Price_Inflation_Adjusted'].kurtosis() #120.3685670
print(kurtosis)


kurtosis = df['Iron_Price_Inflation_Adjusted'].kurtosis() #-1.181144544
print(kurtosis)


kurtosis = df['Steel_Price_Inflation_Adjusted'].kurtosis() #-1.16664339
print(kurtosis)


kurtosis = df['Price_Chromium_Adjusted'].kurtosis() #-1.1847323396
print(kurtosis)


#-----------------------------------------------------------------------------------------------------#

# GRAPHICAL REPRESENTATION - data without year and month column

import matplotlib.pyplot as plt

# Plot histograms for each column
df.hist(figsize=(10, 10))


#-------------------------------------------------------------------------------------------------------#
#Data Preprocessing#

# Handling Duplicates

### Identify duplicate records in the data ###
import pandas as pd


# Identify duplicate records in the data 
# Duplicates in rows

df.duplicated().sum()  # Returns Boolean Series denoting duplicate rows.

#There are 48 duplicate records in df.

df.drop_duplicates(inplace = True)

df.shape

# Duplicates Removed from the data.

#-------------------------------------------------------------------------------------------------------#
# Variance & Zero Variance
variance=df[['Price_Aluminium_per_Ton','Price_Tin_per_Ounce',
'Price_Copper_per_Ton','Price_Iron_per_Ounce','Price_Steel_per_Ton',
'Inflation_Rate_Percentage','Aluminium_Price_Inflation_Adjusted', 
'Tin_Price_Inflation_Adjusted','Copper_Price_Inflation_Adjusted',
'Iron_Price_Inflation_Adjusted','Steel_Price_Inflation_Adjusted',
'Price_Chromium_Adjusted']].var()
    

near_zero_variance=variance[variance<0.01]
print(near_zero_variance)


###### We can see that there are  no Zero or near zero variance columns in the dataset #######
#----------------------------------------------------------------------------------------------------#

#Missing Values

df.isna().sum()

# Count of null values for the respective columns 
"""
Price_Aluminium_per_Ton               60
Price_Tin_per_Ounce                   35
Price_Copper_per_Ton                  49
Price_Iron_per_Ounce                  92
Price_Steel_per_Ton                   70
Inflation_Rate_Percentage             19
Aluminium_Price_Inflation_Adjusted    56
Tin_Price_Inflation_Adjusted          14
Copper_Price_Inflation_Adjusted       59
Iron_Price_Inflation_Adjusted         80
Steel_Price_Inflation_Adjusted        21
Price_Chromium_Adjusted               60
"""

""" Imputing the data with Average of the respective columns to fill up the null records """

from sklearn.impute import SimpleImputer

help(SimpleImputer)

imputer = SimpleImputer(strategy = 'mean', missing_values = np.nan)

df.columns

df[['Price_Aluminium_per_Ton', 'Price_Tin_per_Ounce',
'Price_Copper_per_Ton', 'Price_Iron_per_Ounce', 'Price_Steel_per_Ton',
'Inflation_Rate_Percentage', 'Aluminium_Price_Inflation_Adjusted',
'Tin_Price_Inflation_Adjusted', 'Copper_Price_Inflation_Adjusted',
'Iron_Price_Inflation_Adjusted', 'Steel_Price_Inflation_Adjusted',
'Price_Chromium_Adjusted']] =  imputer.fit_transform(df[['Price_Aluminium_per_Ton', 'Price_Tin_per_Ounce',
'Price_Copper_per_Ton', 'Price_Iron_per_Ounce', 'Price_Steel_per_Ton',
'Inflation_Rate_Percentage', 'Aluminium_Price_Inflation_Adjusted',
'Tin_Price_Inflation_Adjusted', 'Copper_Price_Inflation_Adjusted',
'Iron_Price_Inflation_Adjusted', 'Steel_Price_Inflation_Adjusted',
'Price_Chromium_Adjusted']])

df.isna().sum() # No missing Values left

df.shape

df.info()

#------------------------------------------------------------------------------------------------------#

#Outlier Treatment#

df.columns

# Plot boxplot for each column
df.boxplot(figsize=(10, 10)) # Outliers present in Copper_Price_Inflation_Adjusted
plt.xticks(rotation=45, ha = 'right') 


"""Outliers exist in Copper_Price_Inflation_Adjusted"""


from feature_engine.outliers import Winsorizer


winsor = Winsorizer(capping_method = "iqr",
                    fold = 1.5,
                    tail = 'both',
                    variables = ['Copper_Price_Inflation_Adjusted'])

df[['Copper_Price_Inflation_Adjusted']] = winsor.fit_transform(df[['Copper_Price_Inflation_Adjusted']])

                                                                               
# outliers was removed for Copper_Price_Inflation_Adjusted

#----------------------------------------------------------------------------------------------------#
#Eda After Pre Processing#
 
#Mean
mean = df['Price_Aluminium_per_Ton'].mean() #2499.66072
print(mean)

mean = df['Price_Tin_per_Ounce'].mean() #2482.932977
print(mean)

mean = df['Price_Copper_per_Ton'].mean() #2508.53598
print(mean)

mean = df['Price_Iron_per_Ounce'].mean() #2549.70430
print(mean)

mean = df['Price_Steel_per_Ton'].mean() #2535.46678
print(mean)

mean = df['Inflation_Rate_Percentage'].mean() #2479.45445
print(mean)

mean = df['Aluminium_Price_Inflation_Adjusted'].mean() #2439.17883
print(mean)

mean = df['Tin_Price_Inflation_Adjusted'].mean() #2465.76778
print(mean)

mean = df['Copper_Price_Inflation_Adjusted'].mean() #2504.97155
print(mean)

mean = df['Iron_Price_Inflation_Adjusted'].mean() #2568.16791
print(mean)

mean = df['Steel_Price_Inflation_Adjusted'].mean() #2438.04366
print(mean)

mean = df['Price_Chromium_Adjusted'].mean() #2464.95930
print(mean)


#----------------------------------------------------
#Median
median = df['Price_Aluminium_per_Ton'].median()
print(median)

median = df['Price_Tin_per_Ounce'].median()
print(median)

median = df['Price_Copper_per_Ton'].median()
print(median)

median = df['Price_Iron_per_Ounce'].median()
print(median)

median = df['Price_Steel_per_Ton'].median()
print(median)

median = df['Inflation_Rate_Percentage'].median()
print(median)

median = df['Aluminium_Price_Inflation_Adjusted'].median()
print(median)

median = df['Tin_Price_Inflation_Adjusted'].median()
print(median)

median = df['Copper_Price_Inflation_Adjusted'].median()
print(median)

median = df['Iron_Price_Inflation_Adjusted'].median()
print(median)

median = df['Steel_Price_Inflation_Adjusted'].median()
print(median)

median = df['Price_Chromium_Adjusted'].median()
print(median)
#---------------------------------------------------------------

#Mode
mode = df['Price_Aluminium_per_Ton'].mode()
print(mode)

mode  = df['Price_Tin_per_Ounce'].mode()
print(mode)

mode  = df['Price_Copper_per_Ton'].mode()
print(mode)

mode  = df['Price_Iron_per_Ounce'].mode()
print(mode)

mode  = df['Price_Steel_per_Ton'].mode()
print(mode)

mode  = df['Inflation_Rate_Percentage'].mode()
print(mode)

mode  = df['Aluminium_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Tin_Price_Inflation_Adjusted'].mode()
print(mode) 

mode  = df['Copper_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Iron_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Steel_Price_Inflation_Adjusted'].mode()
print(mode)

mode  = df['Price_Chromium_Adjusted'].mode()
print(mode)
#-------------------------------------------------

#Standard Deviation
df = pd.read_csv(r"C:\Games\DA Project\MM_Price Analysis.csv")

Price_Aluminium_per_Ton_stddev = df['Price_Aluminium_per_Ton'].std()
print("Standard Deviation of Price_Aluminium_per_Ton:", Price_Aluminium_per_Ton_stddev) # 1402.20220

Price_Tin_per_Ounce_stddev = df['Price_Tin_per_Ounce'].std()
print("Standard Deviation of Price_Tin_per_Ounce:", Price_Tin_per_Ounce_stddev) #1417.30439

Price_Copper_per_Ton_stddev = df['Price_Copper_per_Ton'].std()
print("Standard Deviation of Price_Copper_per_Ton:", Price_Copper_per_Ton_stddev) #1396.92928

Price_Iron_per_Ounce_stddev = df['Price_Iron_per_Ounce'].std()
print("Standard Deviation of Price_Iron_per_Ounce:", Price_Iron_per_Ounce_stddev) #1360.46374

Price_Steel_per_Ton_stddev = df['Price_Steel_per_Ton'].std()
print("Standard Deviation of Price_Steel_per_Ton:", Price_Steel_per_Ton_stddev) #1363.10968

Inflation_Rate_Percentage_stddev = df['Inflation_Rate_Percentage'].std()
print("Standard Deviation of Inflation_Rate_Percentage:", Inflation_Rate_Percentage_stddev) #1431.96394

Aluminium_Price_Inflation_Adjusted_stddev = df['Aluminium_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Aluminium_Price_Inflation_Adjusted:", Aluminium_Price_Inflation_Adjusted_stddev) # 1349.44226

Tin_Price_Inflation_Adjusted_stddev = df['Tin_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Tin_Price_Inflation_Adjusted:", Tin_Price_Inflation_Adjusted_stddev) #1403.46621

Copper_Price_Inflation_Adjusted_stddev = df['Copper_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Copper_Price_Inflation_Adjusted:", Copper_Price_Inflation_Adjusted_stddev) #1456.43958

Iron_Price_Inflation_Adjusted_stddev = df['Iron_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Iron_Price_Inflation_Adjusted:",Iron_Price_Inflation_Adjusted_stddev) #1386.22541

Steel_Price_Inflation_Adjusted_stddev = df['Steel_Price_Inflation_Adjusted'].std()
print("Standard Deviation of Steel_Price_Inflation_Adjusted:", Steel_Price_Inflation_Adjusted_stddev) #1401.0134

Price_Chromium_Adjusted_stddev = df['Price_Chromium_Adjusted'].std()
print("Standard Deviation of Price_Chromium_Adjusted:", Price_Chromium_Adjusted_stddev) #1396.86734

#-----------------------------------------------------

#Range#
Price_Aluminium_per_Ton_range = df['Price_Aluminium_per_Ton'].max() - df['Price_Aluminium_per_Ton'].min()
print("Range of Price_Aluminium_per_Ton:", Price_Aluminium_per_Ton_range)
    
Price_Tin_per_Ounce_range = df['Price_Tin_per_Ounce'].max() - df['Price_Tin_per_Ounce'].min()
print("Range of Price_Tin_per_Ounce:", Price_Tin_per_Ounce_range)

Price_Copper_per_Ton_range = df['Price_Copper_per_Ton'].max() - df['Price_Copper_per_Ton'].min()
print("Range of Price_Copper_per_Ton:", Price_Copper_per_Ton_range)

Price_Iron_per_Ounce_range = df['Price_Iron_per_Ounce'].max() - df['Price_Iron_per_Ounce'].min()
print("Range of Price_Iron_per_Ounce:", Price_Iron_per_Ounce_range)

Price_Steel_per_Ton_range = df['Price_Steel_per_Ton'].max() - df['Price_Steel_per_Ton'].min()
print("Range of Price_Steel_per_Ton:", Price_Steel_per_Ton_range)

Inflation_Rate_Percentage_range = df['Inflation_Rate_Percentage'].max() - df['Inflation_Rate_Percentage'].min()
print("Range of Inflation_Rate_Percentage:",Inflation_Rate_Percentage_range)

Tin_Price_Inflation_Adjusted_range = df['Tin_Price_Inflation_Adjusted'].max() - df['Tin_Price_Inflation_Adjusted'].min()
print("Range of Tin_Price_Inflation_Adjusted:", Tin_Price_Inflation_Adjusted_range)

Copper_Price_Inflation_Adjusted_range = df['Copper_Price_Inflation_Adjusted'].max() - df['Copper_Price_Inflation_Adjusted'].min()
print("Range of Copper_Price_Inflation_Adjusted:",Copper_Price_Inflation_Adjusted_range)

Iron_Price_Inflation_Adjusted_range = df['Iron_Price_Inflation_Adjusted'].max() - df['Iron_Price_Inflation_Adjusted'].min()
print("Range of Iron_Price_Inflation_Adjusted:",Iron_Price_Inflation_Adjusted_range)

Steel_Price_Inflation_Adjusted_range = df['Steel_Price_Inflation_Adjusted'].max() - df['Steel_Price_Inflation_Adjusted'].min()
print("Range of Steel_Price_Inflation_Adjusted:", Steel_Price_Inflation_Adjusted_range)

Price_Chromium_Adjusted_range = df['Price_Chromium_Adjusted'].max() - df['Price_Chromium_Adjusted'].min()
print("Range of Price_Chromium_Adjusted:", Price_Chromium_Adjusted_range)

#-----------------------------------------------------------------------------------
#Variance
Price_Aluminium_per_Ton_variance = df['Price_Aluminium_per_Ton'].var()
print("Variance of  Price_Aluminium_per_Ton:",Price_Aluminium_per_Ton_variance) #1966171.03606

Price_Tin_per_Ounce_variance = df['Price_Tin_per_Ounce'].var()
print("Variance of  Price_Tin_per_Ounce:",Price_Tin_per_Ounce_variance) #2008751.75233

Price_Copper_per_Ton_variance = df['Price_Copper_per_Ton'].var()
print("Variance of  Price_Copper_per_Ton:",Price_Copper_per_Ton_variance) #1951411.43481

Price_Iron_per_Ounce_variance = df['Price_Iron_per_Ounce'].var()
print("Variance of  Price_Iron_per_Ounce:",Price_Iron_per_Ounce_variance) #1850861.58804

Price_Steel_per_Ton_variance = df['Price_Steel_per_Ton'].var()
print("Variance of  Price_Steel_per_Ton:",Price_Steel_per_Ton_variance) #1858068.00850

Inflation_Rate_Percentage_variance = df['Inflation_Rate_Percentage'].var()
print("Variance of   Inflation_Rate_Percentage:",Inflation_Rate_Percentage_variance) #2050520.72955

Aluminium_Price_Inflation_Adjusted_variance = df['Aluminium_Price_Inflation_Adjusted'].var()
print("Variance of  Aluminium_Price_Inflation_Adjusted:",Aluminium_Price_Inflation_Adjusted_variance) #1820994.43712

Tin_Price_Inflation_Adjusted_variance = df['Tin_Price_Inflation_Adjusted'].var()
print("Variance of  Tin_Price_Inflation_Adjusted:",Tin_Price_Inflation_Adjusted_variance) #1969717.41363

Copper_Price_Inflation_Adjusted_variance = df['Copper_Price_Inflation_Adjusted'].var()
print("Variance of  Copper_Price_Inflation_Adjusted:",Copper_Price_Inflation_Adjusted_variance) #2121216.26278

Iron_Price_Inflation_Adjusted_variance = df['Iron_Price_Inflation_Adjusted'].var()
print("Variance of  Iron_Price_Inflation_Adjusted:",Iron_Price_Inflation_Adjusted_variance) #1921620.91375

Steel_Price_Inflation_Adjusted_variance = df['Steel_Price_Inflation_Adjusted'].var()
print("Variance of  Steel_Price_Inflation_Adjusted:",Steel_Price_Inflation_Adjusted_variance) #1962838.58901

Price_Chromium_Adjusted_variance = df['Price_Chromium_Adjusted'].var()
print("Variance of  Price_Chromium_Adjusted:",Price_Chromium_Adjusted_variance) #1951238.39229

#-------------------------------------------------------------------------------------------------------#
#Skewness
skewness = df['Price_Aluminium_per_Ton'].skew() #-0.018730200
print(skewness)

skewness = df['Price_Tin_per_Ounce'].skew() #0.031713544
print(skewness)


skewness = df['Price_Copper_per_Ton'].skew() #0.00181016890
print(skewness)


skewness = df['Price_Iron_per_Ounce'].skew() #-0.0706164417
print(skewness)


skewness = df['Price_Steel_per_Ton'].skew() #0.00291421107
print(skewness)


skewness = df['Inflation_Rate_Percentage'].skew() #0.03197126328
print(skewness)


skewness = df['Aluminium_Price_Inflation_Adjusted'].skew() #0.0793496376
print(skewness)


skewness = df['Tin_Price_Inflation_Adjusted'].skew() #0.0456137156
print(skewness)


skewness = df['Copper_Price_Inflation_Adjusted'].skew() #0.08548726902
print(skewness)


skewness = df['Iron_Price_Inflation_Adjusted'].skew() #-0.101335557
print(skewness)


skewness = df['Steel_Price_Inflation_Adjusted'].skew() #0.0389558397
print(skewness)


skewness = df['Price_Chromium_Adjusted'].skew() #0.0390187922
print(skewness)

#-------------------------------------------------------------------------------------------------------#
#Kurtosis
kurtosis = df['Price_Aluminium_per_Ton'].kurtosis() #-1.08185973
print(kurtosis)

kurtosis = df['Price_Tin_per_Ounce'].kurtosis() #-1.15769487
print(kurtosis)


kurtosis = df['Price_Copper_per_Ton'].kurtosis() #-1.069227259
print(kurtosis)


kurtosis = df['Price_Iron_per_Ounce'].kurtosis() #-0.951071068
print(kurtosis)


kurtosis = df['Price_Steel_per_Ton'].kurtosis() #-1.025161006
print(kurtosis)


kurtosis = df['Inflation_Rate_Percentage'].kurtosis() #-1.172781353
print(kurtosis)


kurtosis = df['Aluminium_Price_Inflation_Adjusted'].kurtosis() #-1.0566552623
print(kurtosis)


kurtosis = df['Tin_Price_Inflation_Adjusted'].kurtosis() #-1.1719678484
print(kurtosis)


kurtosis = df['Copper_Price_Inflation_Adjusted'].kurtosis() #-0.7561264979
print(kurtosis)


kurtosis = df['Iron_Price_Inflation_Adjusted'].kurtosis() #-1.0252498810
print(kurtosis)


kurtosis = df['Steel_Price_Inflation_Adjusted'].kurtosis() #-1.1186758016
print(kurtosis)


kurtosis = df['Price_Chromium_Adjusted'].kurtosis() #-1.0502174548
print(kurtosis)



#-------------------------------------------------------------------------------------------------------#
#Correlation Matrix
plt.figure(figsize = (15,8))
sns.heatmap(df.corr(), annot = True, cmap = sns.color_palette("flare", as_cmap=True))

#There's no correlation between the features before transformation#

#------------------------------------------------------------------------------------------------------#

# Boxplot #
sns.boxplot(x=df['Price_Aluminium_per_Ton'])
sns.boxplot(x=df['Price_Tin_per_Ounce'])
sns.boxplot(x=df['Price_Copper_per_Ton'])
sns.boxplot(x=df['Price_Iron_per_Ounce'])
sns.boxplot(x=df['Price_Steel_per_Ton'])
sns.boxplot(x=df['Inflation_Rate_Percentage'])
sns.boxplot(x=df['Aluminium_Price_Inflation_Adjusted'])
sns.boxplot(x=df['Tin_Price_Inflation_Adjusted'])
sns.boxplot(x=df['Copper_Price_Inflation_Adjusted'])
sns.boxplot(x=df['Iron_Price_Inflation_Adjusted'])
sns.boxplot(x=df['Steel_Price_Inflation_Adjusted'])
sns.boxplot(x=df['Price_Chromium_Adjusted'])

#-------------------------------------------------------------------------------------------------------#
# Histogram #

df.columns

sns.distplot(df.Price_Aluminium_per_Ton)
sns.distplot(df.Price_Tin_per_Ounce)
sns.distplot(df.Price_Copper_per_Ton)
sns.distplot(df.Price_Iron_per_Ounce)
sns.distplot(df.Price_Steel_per_Ton)
sns.distplot(df.Inflation_Rate_Percentage)
sns.distplot(df.Aluminium_Price_Inflation_Adjusted)
sns.distplot(df.Tin_Price_Inflation_Adjusted)
sns.distplot(df.Copper_Price_Inflation_Adjusted)
sns.distplot(df.Iron_Price_Inflation_Adjusted)
sns.distplot(df.Steel_Price_Inflation_Adjusted)
sns.distplot(df.Price_Chromium_Adjusted)

#------------------------------------------------------------------------------------------------------#
# Density Plot

sns.kdeplot(df.Price_Aluminium_per_Ton) # Density plot
sns.kdeplot(df.Price_Aluminium_per_Ton, bw = 0.5 , fill = True)

sns.kdeplot(df.Price_Tin_per_Ounce) # Density plot
sns.kdeplot(df.Price_Tin_per_Ounce, bw = 0.5 , fill = True)

sns.kdeplot(df.Price_Copper_per_Ton) # Density plot
sns.kdeplot(df.Price_Copper_per_Ton, bw = 0.5 , fill = True)

sns.kdeplot(df.Price_Iron_per_Ounce) # Density plot
sns.kdeplot(df.Price_Iron_per_Ounce, bw = 0.5 , fill = True)

sns.kdeplot(df.Price_Steel_per_Ton) # Density plot
sns.kdeplot(df.Price_Steel_per_Ton, bw = 0.5 , fill = True)

sns.kdeplot(df.Inflation_Rate_Percentage) # Density plot
sns.kdeplot(df.Inflation_Rate_Percentage, bw = 0.5 , fill = True)

sns.kdeplot(df.Aluminium_Price_Inflation_Adjusted) # Density plot
sns.kdeplot(df.Aluminium_Price_Inflation_Adjusted, bw = 0.5 , fill = True)

sns.kdeplot(df.Tin_Price_Inflation_Adjusted) # Density plot
sns.kdeplot(df.Tin_Price_Inflation_Adjusted, bw = 0.5 , fill = True)

sns.kdeplot(df.Copper_Price_Inflation_Adjusted) # Density plot
sns.kdeplot(df.Copper_Price_Inflation_Adjusted, bw = 0.5 , fill = True)

sns.kdeplot(df.Iron_Price_Inflation_Adjusted) # Density plot
sns.kdeplot(df.Iron_Price_Inflation_Adjusted, bw = 0.5 , fill = True)

sns.kdeplot(df.Steel_Price_Inflation_Adjusted) # Density plot
sns.kdeplot(df.Steel_Price_Inflation_Adjusted, bw = 0.5 , fill = True)

sns.kdeplot(df.Price_Chromium_Adjusted) # Density plot
sns.kdeplot(df.Price_Chromium_Adjusted, bw = 0.5 , fill = True)


#-------------------------------------------------------------------------------------------------------#
df.to_csv("C:\Games\DA Project\Processed MM file.csv", index=False)
