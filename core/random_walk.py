import numpy as np
from .utils import get_bearing, get_distance, haversine


def random_walk(octal_window):
    d = get_distance(octal_window)[0][:-1]
    l = d.mean()
    ls = d.std()
    b = get_bearing(octal_window)[0][:-1]
    t = b.mean()
    ts = b.std()

    l = np.random.normal(l, ls, 1)
    t = np.radians(np.random.normal(t, ts, 1))
    pl = octal_window.iloc[3, :]

    p1 = octal_window.iloc[2, :]
    p2 = octal_window.iloc[4, :]
    dy = l * np.cos(t)
    dx = l * np.sin(t)
    r_earth = 6378000
    pi = np.pi
    new_latitude = p1.lat + (dy / r_earth) * (180 / pi);
    new_longitude = p1.lon + (dx / r_earth) * (180 / pi) / np.cos(p1.lat * pi / 180);

    pc = (new_latitude, new_longitude)
    d = float(haversine(pc, (pl.lat, pl.lon)))

    return p1, p2, pc, d
