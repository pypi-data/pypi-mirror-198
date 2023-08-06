# title:    processsing WRSM catchment water balance
# creator:  PM
# date:     12.09.2022
# no(func): 8

# complimentary workbooks:
    # CATWB_processing_WRSM.ipynb
    # testing_processing.ipynb

import pandas as pd 

# ----------------------------------------------------------
# 1. get net catchment runoff from parent modules
# ----------------------------------------------------------

def monthly_runoff(files):   
    ''' (list of files) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and data frame must exist
    
    monthly_runoff(files)
    >>> timeseries of data in a df
    '''
    # substitute to loop through parent runoff modules
    i = 0
    for i in range(2):
        # load data into a df 
        RU_x = pd.read_table(files[i], header=None, delim_whitespace=True)
        # transpose df 
        RU_x = RU_x.T
        # rename columns by year
        RU_x.columns = RU_x.iloc[0]
        # delete rows for year, total and average
        RU_x.drop([0,13,14], inplace = True)
        # delete column with LT month average
        RU_x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        # RU_1 = pd.melt(RU_x, value_name= files[i][29:-7] + '_NCR_Mm3')
        RU_1 = pd.melt(RU_x)
        # add data to df for WB
        data[runoff_filenames[i][29:-7] + '_NCR_Mm3'] = RU_1['value'].values
    return data

# ----------------------------------------------------------
# 2. get interflow from parent & child modules
# ----------------------------------------------------------

def monthly_interflow(files):   
    ''' (list of files) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and end data frame must exist
    
    monthly_interflow(files)
    >>> timeseries of data in a df
    '''
    # loop through parent and child modules (in loop: file is data, files is list of files)
    for file in files:
        # load data into a df 
        RU_x = pd.read_table(file, header=None, delim_whitespace=True)
        # transpose df 
        RU_x = RU_x.T
        # rename columns by year
        RU_x.columns = RU_x.iloc[0]
        # delete rows for year, total and average
        # refactored: RU_x.drop([0,13,14], inplace = True)
        RU_x.drop(RU_x.tail(2).index, inplace = True)
        RU_x.drop([0], inplace = True)           
        # delete column with LT month average
        RU_x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        RU_1 = pd.melt(RU_x)
        # add data to df for WB
        data[file[29:-7] + '_GWI_Mm3'] = RU_1['value'].values
    return data


# ----------------------------------------------------------
# 3. get baseflow from parent & child modules
# ----------------------------------------------------------

def monthly_baseflow(files):   
    ''' (list of files) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and end data frame must exist
    
    monthly_baseflow(files)
    >>> timeseries of data in a df
    '''
    # loop through parent and child modules (in loop: file is data, files is list of files)
    for file in files:
        # load data into a df 
        RU_x = pd.read_table(file, header=None, delim_whitespace=True)
        # transpose df 
        RU_x = RU_x.T
        # rename columns by year
        RU_x.columns = RU_x.iloc[0]
        # delete rows for year, total and average
        # refactored: RU_x.drop([0,13,14], inplace = True)
        RU_x.drop(RU_x.tail(2).index, inplace = True)
        RU_x.drop([0], inplace = True)           
        # delete column with LT month average
        RU_x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        RU_1 = pd.melt(RU_x)
        # add data to df for WB
        data[file[29:-7] + '_GWB_Mm3'] = RU_1['value'].values
    return data

# ----------------------------------------------------------
# 4. get soil moisture from parent modules
# ----------------------------------------------------------

def monthly_sm_mm(files):      
    ''' (list of files) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and data frame for mm data must exist
    
    monthly_monthly_sm_mm(files)
    >>> timeseries of data in a df
    '''
    # substitute to loop through parent runoff modules
    i = 0
    for i in range(2):
        # load data into a df 
        RU_x = pd.read_table(files[i], header=None, delim_whitespace=True)
        # transpose df 
        RU_x = RU_x.T
        # rename columns by year
        RU_x.columns = RU_x.iloc[0]
        # delete rows for year, total and average
        RU_x.drop(RU_x.tail(2).index, inplace = True)
        RU_x.drop([0], inplace = True) 
        # delete column with LT month average
        RU_x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        RU_1 = pd.melt(RU_x)
        # add data to df for WB
        mm_var[files[i][29:-8] + '_WGST_mm'] = RU_1['value'].values
    return mm_var

# ----------------------------------------------------------
# 5. get GW storage from parent modules
# ----------------------------------------------------------

def monthly_aqs_mm(files):      
    ''' (list of files) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and data frame for mm data must exist
    
    monthly_monthly_aqs_mm(files)
    >>> timeseries of data in a df
    '''
    # substitute to loop through parent runoff modules
    i = 0
    for i in range(2):
        # load data into a df 
        RU_x = pd.read_table(files[i], header=None, delim_whitespace=True)
        # transpose df 
        RU_x = RU_x.T
        # rename columns by year
        RU_x.columns = RU_x.iloc[0]
        # delete rows for year, total and average
        RU_x.drop(RU_x.tail(2).index, inplace = True)
        RU_x.drop([0], inplace = True) 
        # delete column with LT month average
        RU_x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        RU_1 = pd.melt(RU_x)
        # add data to df for WB
        mm_var[files[i][29:-7] + '_AQS_mm'] = RU_1['value'].values
    return mm_var

# ----------------------------------------------------------
# 5. get GW recharge from parent modules
# ----------------------------------------------------------

def monthly_gwr_mm(files):      
    ''' (list of files) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and data frame for mm data must exist
    
    monthly_monthly_gwr_mm(files)
    >>> timeseries of data in a df
    '''
    # substitute to loop through parent runoff modules
    i = 0
    for i in range(2):
        # load data into a df 
        RU_x = pd.read_table(files[i], header=None, delim_whitespace=True)
        # transpose df 
        RU_x = RU_x.T
        # rename columns by year
        RU_x.columns = RU_x.iloc[0]
        # delete rows for year, total and average
        RU_x.drop(RU_x.tail(2).index, inplace = True)
        RU_x.drop([0], inplace = True) 
        # delete column with LT month average
        RU_x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        RU_1 = pd.melt(RU_x)
        # add data to df for WB
        mm_var[files[i][29:-7] + '_GWR_mm'] = RU_1['value'].values
    return mm_var


# ----------------------------------------------------------
# 5. get percolation from parent modules
# ----------------------------------------------------------

def monthly_gtr_mm(files):      
    ''' (list of files) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and data frame for mm data must exist
    
    monthly_monthly_gtr_mm(files)
    >>> timeseries of data in a df
    '''
    # substitute to loop through parent runoff modules
    i = 0
    for i in range(2):
        # load data into a df 
        RU_x = pd.read_table(files[i], header=None, delim_whitespace=True)
        # transpose df 
        RU_x = RU_x.T
        # rename columns by year
        RU_x.columns = RU_x.iloc[0]
        # delete rows for year, total and average
        RU_x.drop(RU_x.tail(2).index, inplace = True)
        RU_x.drop([0], inplace = True) 
        # delete column with LT month average
        RU_x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        RU_1 = pd.melt(RU_x)
        # add data to df for WB
        mm_var[files[i][29:-7] + '_GTR_mm'] = RU_1['value'].values
    return mm_var


# ----------------------------------------------------------
# 6. convert output mm to Mm3 based on subcathment #
# ----------------------------------------------------------


# update


# ----------------------------------------------------------
# 7. get dS soil moisture and GW storage
# ----------------------------------------------------------

def change_in_var(search_term, df):
    ''' (string, df) -> TS
    Calculates the monthly time step, change in a variable
    
    Preconditions:
    1. df must exist 
    2. Search term is greedy so df must contain relevant parent/child modules only 
    3. list of 
    change_in_var("WGST", WB_Mm3)
    >>> timeseries of variable (current - previous) in df
    '''
    df['dS_'+search_term] = df[search_term].diff().fillna(df[search_term])
    
    return df.head()

# ----------------------------------------------------------
# 8. get monthly total of a variable
# ----------------------------------------------------------

def var_total_month(search_term, df):    
    ''' (string, df) -> TS
    Sums variable and adds it to the WB df
    
    Pre-conditions: 
    1. df must exist and 
    2. Search term is greedy so df must contain relevant parent/child modules only 
    
    var_total_month(search_term):
    >>> timeseries summation of variable in a df 
    '''
    
    # get mask from search term 
    col_array = df.columns.str.contains(search_term)
                                        
    # find matching columns & sum
    df.columns[col_array] # add a pause here to check that the correct variables are summed
    
    # add summed values to the df
    val_total = round(df[df.columns[col_array]].sum(axis=1), 2)
    df[(search_term)] = val_total
    
    return df.head()








