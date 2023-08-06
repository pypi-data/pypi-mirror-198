"""
=======================
Qsca vs wavelength Mean
=======================

"""


import numpy as np
from PyMieSim.experiment import SphereSet, SourceSet, Setup
from PyMieSim import measure

scatterer_set = SphereSet(
    diameter=[200e-9, 150e-9, 100e-9],
    index=[2, 3, 4],
    n_medium=1
)

source_set = SourceSet(
    wavelength=np.linspace(400e-9, 1000e-9, 500),
    polarization=0,
    amplitude=1
)

experiment = Setup(
    scatterer_set=scatterer_set,
    source_set=source_set
)

data = experiment.Get(Input=[measure.Qsca])

data = data.Mean(scatterer_set.index)

figure = data.plot(
    y=measure.Qsca,
    x=source_set.wavelength
)

figure.show()

# -
