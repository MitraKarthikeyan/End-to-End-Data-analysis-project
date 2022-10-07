'''This is the automation script that I used to run in my EC2 virtual machine to keep the data 
collection process running 24 hours a day, seven days a week. The air pollution data is updated 
once every 5 hours. As a result, data from all days is critical. I used Amazon RDS to store the 
collected data from the API, which runs every hour --> collects the data and appends it to the 
existing data in the database.''' 

''' Then, I connected my RDS to --> MySql workbench to view, query, and track the data that was collected.'''
#script.py and script_file.ipynb are the same files, please reffer to main_file.ipynb for code explanation


import requests
import pandas as pd
import io
import pygsheets
import datetime as dt
import sqlalchemy 
from sqlalchemy import create_engine
from datetime import timedelta

url_data = requests.get("https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001fc815e771f3a46e162d44e8e5b3ff2ab&format=csv&offset=0").content

rawData = pd.read_csv(io.StringIO(url_data.decode('utf-8')))
rawData = rawData.replace(to_replace="Andhra_Pradesh", value ="Andhra Pradesh")
rawData = rawData.replace(to_replace ="West_Bengal", value ="West Bengal")
rawData = rawData.replace(to_replace ="Uttar_Pradesh", value ="Uttar Pradesh")
rawData = rawData.replace(to_replace ="Jammu_&_Kashmir", value ="Jammu & Kashmir")
rawData = rawData.replace(to_replace ="Arunachal_Pradesh", value ="Arunachal Pradesh")


rawData = rawData.append(pd.Series(), ignore_index=True)
now = dt.datetime.utcnow()+timedelta(hours=4, minutes=30)
now = now.strftime('%d-%m-%Y %H:00:00')
rawData['Measure_time'] = now

rawData.columns = ['Id', 'Country', 'State', 'City', 
                'Station', 'Last_Update', 'Pollution_ID','Pollutant_Min', 'Pollutant_Max', 
                'Pollutant_Avg', 'Pollutant_Unit', 'Measure_Time']

engine = sqlalchemy.create_engine('mysql+mysqlconnector://admin:8098282280@gokultest.crip17huxagt.ap-south-1.rds.amazonaws.com:3306/air_pollution')

rawData.to_sql(name='hourly_air_pollution', con=engine, if_exists='append', index=False)
