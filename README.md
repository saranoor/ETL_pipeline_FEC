## Title
ETL Pipeline for Federal Election Commission (USA) Data

## Description
Election Committees receive contributions all year round. There are four main sources of funding: Small Individual Contributors, Large Individual Contributors, Political Committees and Candidates own money. My project will help the data analysts to analyze and understand the distribution of these contributions with respect to location and time.
In this project, I have engineered a pipeline to store FEC data in S3 bucket, extract and transform the data in S3 using Python and loads the data into MySQL hosted on AMAZON Redshift. 

## Demo
![Demo](demo/FEC_Analyzer_demo.gif =250x250)

## Technologies 
- AWS: S3, EC2, Redshift
- Database: MySQL
- Python3.6: Jupyter Notebook/Anaconda

## Technical Description 

### Installation/Setup
Use the following guide on AWS to setup EC2 instance, S3 bucket, and Redshift
https://docs.aws.amazon.com/ec2/index.html?nc2=h_ql_doc_ec2
https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
### How to run:
Use run.sh from src folder to run the ETL pipeline or simply run python3 datapipelin.py on EC2 instance
 
