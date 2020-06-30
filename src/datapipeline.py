from data_cleaning import *
from load_to_database import *
from load_to_S3 import *
import boto3
import pandas as pd
import numpy as np
import datetime
import time
import sqlalchemy
import sqlalchemy.types as sqltypes
import pymysql
from sqlalchemy import create_engine

if __name__ == "__main__":
    
    client = boto3.client(
    's3',
    aws_access_key_id='ASIASM62P7A5WWYRQZEN',
    aws_secret_access_key='yozdm5nYYVEN3xKkoDytDiatfaojQ2OFANedSWgv')

    host="database-1.cgbyduz3lnxb.us-east-1.rds.amazonaws.com"
    port=3306
    dbname="FECData"
    user="admin"
    password="physiology62A"
    
    # creaitng connection to engine
    engine = create_engine('mysql+pymysql://' + user + ':'+ password + '@' + host + ':' + str(port) +'/' + dbname, echo=False)
    conn = engine.connect()
        
    html_page = urllib2.urlopen("https://www.fec.gov/data/browse-data/?tab=bulk-data")
    
    #extracting urls of files containing FEC data
    all_urls = Parse_web(html_page)
    #uploading the files to S3 bucket
    To_S3(all_urls)
    
    #finding names of the files already in S3 
    indivfile_list =[]
    for obj in client.list_objects_v2(Bucket= 'dataelection')['Contents']:
        FileName = obj['Key']
        indivfile_list.append(FileName)
        
    #processing data in the files and storing in MySQL database
    for i in range(0,len(indivfile_list)):
        obj = client.get_object(Bucket='dataelection', Key=indivfile_list[i])
        df = pd.read_csv(obj['Body'],header= None, sep='\t', error_bad_lines=False,encoding='latin-1')
        new_df = ProcessFiles(df)
        ToSQL(new_df)
    conn.close()       