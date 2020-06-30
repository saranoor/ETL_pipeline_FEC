import pandas as pd
import numpy as np
def ProcessFiles(df):
    """
    This function cleaned the data by removing NAN values, removing ineligible zip codes, changing date time format, etc.
    
    Args: data in dataframe that needs to be cleaned
    Return: cleaned dataframe
    """

    new_df =df[0].str.split('|', expand=True)
        new_df.columns =['Committee_ID','Amendment_Indic','Report_Type','Election_Type','Image_Number','Transaction_Type',
                     'Entity_Type','Name','City','State','ZipCode','Employer','Occupation','Transaction_Date',
                     'Transaction_Amount','FEC_ID','Transaction_ID','Report_ID','Memo_Code','Memo_Txt','SUB_ID']
    #replce blank spaces with NaN
    new_df= new_df.replace(r'^\s*$', np.NaN, regex=True)
    
    #how to drop rows with Nan
    new_df = new_df.dropna(how='all')

    #reset index:
    new_df=new_df.reset_index(drop=True)

    new_df['ZipCode'] =new_df['ZipCode'].astype('str')
    mask_filter = (new_df['ZipCode'].str.len() != 5)
    Notvalid_zipcode = new_df.loc[mask_filter]
    #fetch out data with zip coes not equal to 5
    mask = (new_df['ZipCode'].str.len() == 5)
    new_df = new_df.loc[mask]

    #replace NaN with 0
    new_df=new_df.fillna(0)

    #change datatypes of columns
    new_df['Transaction_Type']=new_df['Transaction_Type'].astype(str)

    #change date string to datetime
    new_df['Transaction_Date']=pd.to_datetime(new_df['Transaction_Date'], format ="%m%d%Y",errors='coerce')
    new_df['Transaction_Date']=new_df['Transaction_Date'].dt.strftime('%Y-%m-%d')
    new_df['Transaction_Date']= new_df['Transaction_Date'].astype('datetime64[ns]')

    #new_df[['Last_Name','First_Name']]=new_df.Name.str.split(',', expand=True)
    #new_df.drop('Name', axis=1, inplace=True)


    return new_df


