# title:    processsing WRSM catchment water balance
# creator:  PM
# date:     16.09.2022
# no(func): 3

# complimentary workbooks:
    # WETWB_WRSM_testing.ipynb
    # WETWB_WRSM.ipynb

import pandas as pd

# ---------------------------------------------------------------
# 1. get WRSM model output for the comprehensive wetland module
# ---------------------------------------------------------------

def wetland_model_output(wl_files, files, df):      
    ''' (list of files, list of files, df) -> TS 
    Transforms and adds data from structured text file to a data frame
    
    Pre-conditions: list of files and data frame for mm data must exist
    
    wetland_model_output(file_names, wetland_files_list, mcm_var_df)
    >>> timeseries of data in a df
    '''
    # loop through all output files (in loop: file is data, files is list of files)
    for name,file in zip(wet_files, filenames):
        # load data into a df 
        x = pd.read_table(file, header=None, delim_whitespace=True)
        # transpose df 
        x = x.T
        # rename columns by year
        x.columns = x.iloc[0]
        # delete rows for year, total and average
        x.drop(x.tail(2).index, inplace = True)
        x.drop([0], inplace = True)           
        # delete column with LT month average
        x.drop(columns=['AVERAGE'], inplace = True)
        # convert from wide to long
        y = pd.melt(x)
        # add data to df for WB
        df[name + '_Mm3'] = y['value'].values
    return df.head()

# ---------------------------------------------------------------
# 2. change in storage from model output (xi -xn)
# ---------------------------------------------------------------

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

# ---------------------------------------------------------------
# 3. get hydrological years from datetime index in pd df
# ---------------------------------------------------------------

def hydro_years(df):    
    '''(df) -> TS column
    
    Adds a water year column to a df
    Pre-condition: df must have index as datetime
    
    hydro_years(mcm_var)
    >>> new df with WY column
    '''
    
    WY = []
    years = df.index.year.values.tolist()
    months = df.index.month.to_list()
    for i in range(len(years)):
            if months[i] < 10:
                year = years[i] - 1
                WY.append(year)
            else:
                year = years[i] 
                WY.append(year)
    df['WY'] = WY
    outcome_statement = 'Successfully added '+str(len(WY))+' water years to the dataframe'
    return outcome_statement
