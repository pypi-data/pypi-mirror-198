"""
==================
Mean Qsca vs index
==================

"""


import numpy as np
from PyMieSim.experiment import SphereSet, SourceSet, Setup
from PyMieSim import measure

scatterer_set = SphereSet(
    diameter=800e-9,
    index=np.linspace(1.3, 1.9, 1500),
    n_medium=1
)

source_set = SourceSet(
    wavelength=[500e-9, 1000e-9, 1500e-9],
    polarization=30,
    amplitude=1
)

experiment = Setup(
    scatterer_set=scatterer_set,
    source_set=source_set
)

data = experiment.Get([measure.Qsca])

figure = data.plot(
    y=measure.Qsca,
    x=scatterer_set.index
)

figure.show()

# -
