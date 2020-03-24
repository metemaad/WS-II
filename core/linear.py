
from .utils import haversine


def linear(row_data):
    lat = row_data.lat.values
    lon = row_data.lon.values
    pc = ((lat[2] + lat[4]) / 2, (lon[2] + lon[4]) / 2)
    d = haversine(pc, (lat[3], lon[3]))
    return (lat[2], lon[2]), (lat[4], lon[4]), pc, d
