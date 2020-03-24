import numpy as np


def haversine(p1, p2):
    lat, lon = p1
    lat2, lon2 = p2
    d_lat, d_lon, lat1, lat2 = map(np.radians, (lat2 - lat, lon2 - lon, lat, lat2))
    a = np.sin(d_lat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(d_lon / 2) ** 2
    distance_val = 2 * np.arcsin(np.sqrt(a)) * 6372.8 * 1000  # convert to meter
    return distance_val


def get_bearing(row_data):
    lat = row_data.lat.values
    lon = row_data.lon.values
    lat2 = np.append(lat[1:], lat[-1:])
    lon2 = np.append(lon[1:], lon[-1:])

    lat1, lat2, diff_long = map(np.radians, (lat, lat2, lon2 - lon))
    a = np.sin(diff_long) * np.cos(lat2)
    b = np.cos(lat1) * np.sin(lat2) - (np.sin(lat1) * np.cos(lat2) * np.cos(diff_long))
    bearing_val = np.arctan2(a, b)
    bearing_val = np.degrees(bearing_val)
    bearing_val = (bearing_val + 360) % 360
    row_data = row_data.assign(bearing=bearing_val)
    return bearing_val, row_data


def get_distance(row_data):
    lat = row_data.lat.values
    lon = row_data.lon.values
    lat2 = np.append(lat[1:], lat[-1:])
    lon2 = np.append(lon[1:], lon[-1:])
    # R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km
    r = 6372.8
    d_lat, d_lon, lat1, lat2 = map(np.radians, (lat2 - lat, lon2 - lon, lat, lat2))
    a = np.sin(d_lat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(d_lon / 2) ** 2
    distance_val = 2 * np.arcsin(np.sqrt(a)) * r * 1000  # convert to meter
    # this is the distance difference between two points not the Total distance traveled

    row_data = row_data.assign(distance=distance_val)

    return distance_val, row_data
