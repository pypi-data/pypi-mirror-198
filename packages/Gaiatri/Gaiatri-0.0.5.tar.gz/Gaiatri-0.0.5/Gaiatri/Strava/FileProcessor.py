import os
import pandas as pd
import numpy as np
from pandas import json_normalize
from math import sin, cos, sqrt, atan2, radians

# Universal file saving path
cwd = os.getcwd()

# ACTIVITIES LIST
def activitiesList (filepath):

  global activities_list

  # File saving preps
  file_name = 'activities-list.csv'
  file_path = os.path.join(cwd,file_name)
  
  data = pd.read_json(filepath)

  # Convert from JSON Pandas Dataframe
  df = pd.DataFrame.from_dict(data)

  # Convert lat-lon to string
  df['start_latlng'] = df['start_latlng'].astype(str)

  # Extract the latitude and longitude values from 'start_latlng' column, then put in separate columns
  df[['latitude', 'longitude']] = df['start_latlng'].str.extract(r'\[(.*),(.*)\]')

  # Convert latitude and longitude data type into float
  df['latitude'] = df['latitude'].astype(float)
  df['longitude'] = df['longitude'].astype(float)

  activities_list = df.drop(['resource_state'], axis=1)

  df.to_csv(file_path) # Save table as CSV with default name "activities-list"

  return activities_list # Display result


# ACTIVITY STREAM
def activityStream(filepath):

  global datastream

  # File saving preps
  file_name = 'activity-stream.csv'
  file_path = os.path.join(cwd,file_name)

  # Read the JSON file
  stream_data_df = pd.read_json(filepath)

  # Convert from JSON to Pandas Dataframe
  a = pd.DataFrame.from_dict(stream_data_df)

  # Explode the arrays into rows
  b = a.apply(pd.Series.explode).reset_index()

  # Convert those fuckers
  b['latlng'] = b['latlng'].astype(str)

  b[['latitude', 'longitude']] = b['latlng'].str.extract(r'\[(.*),(.*)\]')

  # Remove unused columns
  b.drop(b.tail(3).index, inplace=True)
  datastream = b.drop(['latlng','index'], axis=1)

  # Convert the data types
  datastream = datastream.astype({
    'velocity_smooth': 'float',
    'distance': 'float',
    'altitude': 'float',
    'time':'int',
    'latitude': 'float',
    'longitude': 'float', 
    })
  
  datastream.to_csv(file_name)

  return datastream