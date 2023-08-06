import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import json_normalize
from math import sin, cos, sqrt, atan2, radians

def queryByActivityExactName(name):

  # Query the rows with the name
  result = activities_list.loc[activities_list['name'] == name]

  return result

def queryByActivityApproximateName(word):
 
  # Query the rows with the name
  results = activities_list[activities_list['name'].str.contains(word)]

  return results

# Find the Lat Lon of velocity of interest

def queryBySingleVelocity(velocity):

  search_string = str(velocity)[:3]

  try:
    result = datastream.loc[datastream['velocity_smooth'].astype(str).str[:3] == search_string]
  except ValueError:
    print("Error: Non-numeric values found in 'values' column.")

  return result

# Find the Lat Lon of a range of velocities of interest

def queryByVelocityRange(velocity_min, velocity_max):
  # Minimum velocity

  v1 = str(velocity_min)[:3]

  # Maximum velocity

  v2 = str(velocity_max)[:3]

  try:
    result = datastream.loc[
        (datastream['velocity_smooth'].astype(str).str[:3] >= v1)
        &
        (datastream['velocity_smooth'] .astype(str).str[:3] <= v2)]
  except ValueError:
    print("Error: Non-numeric values found in 'values' column.")

  return result

def queryByRadius(lat, lon, radius):

  # Define a function to calculate the distance between two points using the Haversine formula
  def haversine(lat1, lon1, lat2, lon2):
      R = 6371  # Earth's radius in kilometers
      d_lat = radians(lat2 - lat1)
      d_lon = radians(lon2 - lon1)
      a = sin(d_lat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon/2)**2
      c = 2 * atan2(sqrt(a), sqrt(1-a))
      distance = R * c
      return distance

  # Query the rows where the distance to the center point is less than the radius
  activities_list['distance'] = activities_list.apply(lambda row: haversine(lat, lon, row['latitude'], row['longitude']), axis=1)
  result = activities_list[activities_list['distance'] <= radius]

  # Display the result
  df_filtered = activities_list.loc[activities_list['distance'] <= radius]

  print(df_filtered.loc[:, ['name','id','latitude','longitude']])