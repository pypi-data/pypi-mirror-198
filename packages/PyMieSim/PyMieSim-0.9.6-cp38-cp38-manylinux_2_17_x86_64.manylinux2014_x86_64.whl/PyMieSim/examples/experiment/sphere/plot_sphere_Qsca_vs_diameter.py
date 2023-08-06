"""
=====================
Mean Qsca vs diameter
=====================

"""


import numpy as np
from PyMieSim.experiment import SphereSet, SourceSet, Setup
from PyMieSim import measure

diameter = np.geomspace(6.36e-09, 10000e-9, 200500)
wavelength = [500e-9, 1000e-9, 1500e-9]

scatterer_set = SphereSet(
    diameter=diameter,
    index=[1.4],
    n_medium=1
)

sourceSet = SourceSet(
    wavelength=wavelength,
    polarization=30,
    amplitude=1
)

experiment = Setup(
    scatterer_set=scatterer_set,
    source_set=sourceSet
)

data = experiment.Get(measure.Qsca)

figure = data.plot(
    y=measure.Qsca,
    x=scatterer_set.diameter
)

figure.show()

# -

