import numpy as np
import pandas as pd
import pylab
import matplotlib
from statsmodels.stats.weightstats import _zconfint_generic, _tconfint_generic, stats
    %pylab inline
data = pd.read_csv('input/water.txt', sep='\t')
data.shape