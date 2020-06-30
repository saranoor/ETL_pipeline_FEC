import os
import sys
import csv
import pymysql
import sqlalchemy
import sqlalchemy.types as sqltypes
from sqlalchemy import create_engine

def ToSQL(df):
    """
    Save the dataframe to MySQL
    
    Args: data in datafram that has to be uploaded
    """
    df.to_sql(name ='Contribution_dataset_staging', con=engine, if_exists ='append', index=False, chunksize=50000,
              dtype={'Committee_ID': sqlalchemy.types.NVARCHAR(length=9),
                     'Amendment_Indic': sqlalchemy.types.NVARCHAR(length=1),
                     'Report_Type':sqlalchemy.types.NVARCHAR(length=3),
                     'Election_Type':sqlalchemy.types.NVARCHAR(length=5),
                     'Image_Number':sqlalchemy.types.NVARCHAR(length=20),
                     'Transaction_Type':sqlalchemy.types.NVARCHAR(length=3),
                     'Entity_Type':sqlalchemy.types.NVARCHAR(length=3),
                     'Name':sqlalchemy.types.NVARCHAR(length=200),
                     'City':sqlalchemy.types.NVARCHAR(length=30),
                     'State':sqlalchemy.types.NVARCHAR(length=2),
                     'ZipCode':sqlalchemy.types.NVARCHAR(length=9),
                     'Employer':sqlalchemy.types.NVARCHAR(length=38),
                     'Occupation':sqlalchemy.types.NVARCHAR(length=38),
                     'Transaction_Date':sqlalchemy.types.DATE,
                     'Transaction_Amount':sqlalchemy.DECIMAL,
                     'FEC_ID':sqlalchemy.types.NVARCHAR(length=9),
                     'Transaction_ID':sqlalchemy.types.NVARCHAR(length=32),
                     'Report_ID':sqlalchemy.types.NVARCHAR(length=22),
                     'Memo_Code':sqlalchemy.types.NVARCHAR(length=1),
                     'Memo_Txt':sqlalchemy.types.NVARCHAR(length=100),
                     'SUB_ID':sqlalchemy.types.NVARCHAR(length=19),
                     }
              )