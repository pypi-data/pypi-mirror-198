"""
===================
b1 vs core diameter
===================

"""

import numpy as np
from PyMieSim.experiment import SourceSet, Setup, CoreShellSet
from PyMieSim.materials import BK7
from PyMieSim import measure

scatterer_set = CoreShellSet(
    core_diameter=np.geomspace(100e-09, 3000e-9, 5000),
    shell_diameter=800e-9,
    core_index=1.6,
    shell_material=BK7,
    n_medium=1
)

source_set = SourceSet(
    wavelength=[800e-9],
    polarization=0,
    amplitude=1
)

experiment = Setup(scatterer_set=scatterer_set, source_set=source_set)

data = experiment.Get([measure.a1])

figure = data.plot(
    y=measure.a1,
    x=scatterer_set.core_diameter,
    y_scale='linear'
)

figure.show()
