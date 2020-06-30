import pandas as pd
import numpy as np
import datetime
import glob
import time
import os
from io import BytesIO
import zipfile
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import boto3

def Parse_web(html_page):
    """
    The function scrapes all the urls of each year of election commission individual contributors and store them in a list.
    Args: url of USA Federal ELection Comission site
    Return: list of each urls of individual election contriubtors data 
    
    """
    soup = BeautifulSoup(html_page, "lxml")  
    x= soup.find_all(class_="list--flat-bordered")[21]
    links = [a["href"] for a in x.select("a[href]")]

    all_urls =[]

    for link in links:
        if '20' in link:  
            url = "https://www.fec.gov" + link
            all_urls.append(url)
        
    return all_urls
    
def To_S3(all_urls):
    """
    The function takes the list of urls of election commission data files. It uploads the data if S3 bucket is empty or if there is existing     data in S3 bucket it uploads the new election commission files of the current year. 
    has been uploaded 
    Args: List of url of files
    Return: None
    """
    files_list =[]
    client = boto3.client(
    's3',
    aws_access_key_id='ASIASM62P7A5WWYRQZEN',
    aws_secret_access_key='yozdm5nYYVEN3xKkoDytDiatfaojQ2OFANedSWgv')
    
    try:
        for obj in client.list_objects_v2(Bucket= 'dataelection')['Contents']:
            FileName = obj['Key']
            files_list.append(FileName)
    except:
        pass 
    now = datetime.datetime.now()
    current_year=now.year
    #current_year='2002'
    if len(files_list)==0:

        for yr_link in all_urls:
            req = urllib2.urlopen(yr_link)
            zip_file = zipfile.ZipFile(BytesIO(req.read()))
            zip_file.namelist()
            zip_file.extractall('files_to_upload') 
            timestr = time.strftime("%Y%m%d-%H%M%S")
            if 'files_to_upload/itcont.txt'in glob.glob("files_to_upload/*.txt"):
                #os.rename('files_to_upload/itcont.txt','files_to_upload/itcont'+timestr+'.txt')
                os.rename('files_to_upload/itcont.txt','files_to_upload/itcont'+timestr+'.txt')
            files_list = os.listdir('files_to_upload')
            for file in files_list:
                if file.endswith(".txt"):
                    print(os.path.join('files_to_upload', file))
                    client.upload_file(os.path.join('files_to_upload', file),'dataelection',file)
                    os.remove(os.path.join('files_to_upload', file))
    else:
        for url in all_urls:
            if current_year in url:
                req = urllib2.urlopen(url)
                zip_file = zipfile.ZipFile(BytesIO(req.read()))
                files_to_check=zip_file.namelist()
                files_to_extract=list(set(files_to_check)-set(files_list))
                if files_to_extract:
                        for cnt in range(0,len(files_to_extract)):
                            zip_file.extract(files_to_extract[cnt],'files_to_upload')
                if 'files_to_upload/itcont.txt'in glob.glob("files_to_upload/*.txt"):
                #os.rename('files_to_upload/itcont.txt','files_to_upload/itcont'+timestr+'.txt')
                    os.rename('files_to_upload/itcont.txt','files_to_upload/itcont'+timestr+'.txt')
                files_list = os.listdir('files_to_upload')
                for file in files_list:
                    if file.endswith(".txt"):
                        print(os.path.join('files_to_upload', file))
                        client.upload_file(os.path.join('files_to_upload', file),'dataelection',file)
                        os.remove(os.path.join('files_to_upload', file))
                        
if __name__ == "__main__":
    all_urls = Parse_web(html_page)
    To_S3(all_urls)