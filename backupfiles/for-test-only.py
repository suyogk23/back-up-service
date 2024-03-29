
import requests
import numpy as np
import pandas as pd
def fetch_earthquake_data():
    earthquake_data = []  # Initialize a list to store earthquake data
    
    # Define parameters for the earthquake query
    parameters = {
        "format": "geojson",
        "starttime": "2024-01-01",
        "endtime": "2024-01-31",
        "minmagnitude": 4.0,
        "maxmagnitude": 9.0,
        "minlatitude": -90,
        "maxlatitude": 90,
        "minlongitude": -180,
        "maxlongitude": 180,
        "orderby": "time",
        "limit": 10  # Adjust limit as needed
    }

    # URL for USGS Earthquake API
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    # Make the request to the API
    response = requests.get(url, params=parameters)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information from the response
        for feature in data['features']:
            properties = feature['properties']
            magnitude = properties['mag']
            cdi = properties.get('cdi')
            if cdi is None:  # Check if CDI value is None
                cdi = 5
            mmi = properties.get('mmi')
            if mmi is None:
                mmi=5
            sig = properties.get('sig')
            nst = properties.get('nst')
            dmin = properties.get('dmin')
            gap = properties.get('gap')
            depth = feature['geometry']['coordinates'][2]
            latitude = feature['geometry']['coordinates'][1]
            longitude = feature['geometry']['coordinates'][0]
            year = str(properties['time'])[:4]
            month = str(properties['time'])[5:7]
            mag_type = properties['magType']
            
            # Append earthquake data to the list
            earthquake_data.append({
                "magnitude": magnitude,
                "cdi": cdi,
                "mmi": mmi,
                "sig": sig,
                "nst": nst,
                "dmin": dmin,
                "gap": gap,
                "depth": depth,
                "latitude": latitude,
                "longitude": longitude,
                "year": year,
                "month": month,
                "mag_type": mag_type
            })
    else:
        print("Failed to fetch earthquake data")

    l = earthquake_data  # Return the earthquake data list
    df=pd.DataFrame(l)
    obj=df.select_dtypes(include=['object'])
    df.drop(['mag_type'],axis=1,inplace=True)
    from sklearn.preprocessing import LabelEncoder
    lr=LabelEncoder()
    obj_lbl=obj.apply(lr.fit_transform)
    df=pd.concat([df,obj_lbl],axis=1)

    non_object_cols = df.select_dtypes(exclude='object')

    # Drop object type columns from the DataFrame
    df = df[non_object_cols.columns]

    X=df.values
    # mask = np.array([[not isinstance(element, str) for element in row] for row in X])
    # X = X[mask]
    #print(df)
    return X

fetch_earthquake_data()
