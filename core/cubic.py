import numpy as np
from .utils import  haversine
from scipy.interpolate import interp1d


def cubic(row_data):
    lat = row_data.lat.values
    lon = row_data.lon.values

    x3 = lat[3]
    y3 = lon[3]
    lat = np.delete(lat, 3)
    lon = np.delete(lon, 3)
    t = np.diff(row_data.index) / 1000000000
    t3 = t[3]
    t = np.delete(t, 3)
    t = np.cumsum(t)
    t = np.insert(t, 0, 0).astype(float)
    fx = interp1d(t, lat, kind='cubic')
    fy = interp1d(t, lon, kind='cubic')
    new_x = fx(t3)
    new_y = fy(t3)

    pc = (new_x, new_y)
    d = haversine(pc, (x3, y3))
    return (lat[2], lon[2]), (lat[3], lon[3]), pc, d