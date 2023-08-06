"""
===================
a1 vs core diameter
===================

"""


import numpy as np
from PyMieSim.experiment import SourceSet, Setup, CoreShellSet
from PyMieSim.materials import BK7, Silver
from PyMieSim import measure

scatterer_set = CoreShellSet(
    core_diameter=np.geomspace(100e-09, 600e-9, 400),
    shell_diameter=800e-9,
    core_material=Silver,
    shell_material=BK7,
    n_medium=1
)

sourceSet = SourceSet(
    wavelength=[800e-9, 900e-9, 1000e-9],
    polarization=0,
    amplitude=1
)

experiment = Setup(scatterer_set=scatterer_set, source_set=sourceSet)

data = experiment.Get([measure.a1])

figure = data.plot(
    y=measure.a1,
    x=scatterer_set.core_diameter,
    y_scale='log'
)

figure.show()
