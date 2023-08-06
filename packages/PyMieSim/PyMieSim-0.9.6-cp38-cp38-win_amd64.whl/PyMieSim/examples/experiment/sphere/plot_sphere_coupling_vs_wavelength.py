"""
======================
Coupling vs wavelength
======================
"""


import numpy as np
from PyMieSim.experiment import SphereSet, SourceSet, Setup, LPModeSet
from PyMieSim import measure
from PyMieSim.materials import BK7

wavelength = np.linspace(950e-9, 1050e-9, 300)
diameter = np.linspace(100e-9, 8000e-9, 5)

detector_set = LPModeSet(
    Mode="1-1",
    NA=[0.05, 0.01],
    phi_offset=-180,
    gamma_offset=0,
    filter=None,
    sampling=300
)

scatterer_set = SphereSet(
    diameter=diameter,
    material=BK7,
    n_medium=1
)

source_set = SourceSet(
    wavelength=wavelength,
    polarization=0,
    amplitude=1
)

experiment = Setup(scatterer_set, source_set, detector_set)

data = experiment.Get(measure.coupling)

figure = data.plot(
    y=measure.coupling,
    x=source_set.wavelength,
    std=scatterer_set.diameter
)

figure.show()

# -
