def hhmm_to_min(time_hhmm):
    ''' 
    Return the number of minutes for the time in the "hhmm" format.

    Parameters:
    time_hhmm : int (in the range from 1 to 2400)

    Returns: int
    '''
    
    if time_hhmm//100 > 0:
        time_min = time_hhmm // 100 * 60 + time_hhmm % 100
    else:
        time_min = time_hhmm % 100
    return time_min



def add_round(df):
    ''' 
    Create a new column called 'round' in a DataFrame 
    based on the rounded value of crs_dep_time (rounded hour)
    '''
    #round crs_dep_time to the nearest hundred
    df['round'] = df['crs_dep_time'].astype(int).round(-2)
    #change back to string format
    df['round'] = df['round'].astype(str)
    #add leading zeros to the beginning of the string
    df['round'] = df['round'].str.zfill(4)
    #keep left most 2 characters
    df['round'] = df['round'].str[:2]
    #change 24 to 24
    df.loc[df['round'] == '24', 'round'] = '23'  
    return df
