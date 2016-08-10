import numpy as np
from astropy import units as u


a = np.arange(100000.)
q0 = u.Quantity(1., u.s)
q1 = u.Quantity(a, u.m)
q2 = u.Quantity(a[:10000], u.deg)


def time_quantity_creation():
    u.Quantity(a, u.m)


def time_quantity_creation_nocopy():
    u.Quantity(a, u.m, copy=False)


def time_quantity_view():
    q1.view(u.Quantity)


def time_quantity_init_scalar():
    3. * u.m / u.s


def time_quantity_init_array():
    a * u.m / u.s


def time_quantity_scalar_conversion():
    (3. * u.m / u.s).to(u.km / u.hour)


def time_quantity_array_conversion():
    (a * u.m / u.s).to(u.km / u.hour)


def time_quantity_times_unit():
    q1 * u.m


def time_quantity_times_quantity():
    q1 * q0


def time_quantity_ufunc_sin():
    np.sin(q2)
