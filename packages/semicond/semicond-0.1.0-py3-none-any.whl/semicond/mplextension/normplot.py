from __future__ import annotations

from ..stats import benard_estimator, estimator
from .NormalScale import *

from functools import partial

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def normplot(
    data,
    x : str,
    hue : str = None,
    estimator_args : tuple[float, float] = None,
    ax : mpl.axes.Axes = None,
) -> mpl.axes.Axes:
    """
    Make a normal probability plot.

    Parameters
    ----------
    data : DataFrame
        Data to plot.
    x : str
        Column name of the data to plot.
    hue : str, optional
        Column name of the data to use for color.
    estimator_args : tuple[float, float], optional
        Arguments to pass to the estimator function.
    ax : Axes, optional
        Axes to plot on, otherwise uses the current Axes.

    Returns
    -------
    Axes
        Axes object with the plot.
    """
    ax = ax or plt.gca()

    estimator_func = partial(estimator, *estimator_args) if estimator_args else benard_estimator

    tdata = data.sort_values(x)
    if hue:
        for _, tdf in tdata.groupby(hue):
            _, vals = estimator_func(tdf[x])
            tdata.loc[tdf.index, "prob"] = vals
    else:
        _, vals = estimator_func(tdata[x])
        tdata.loc[tdata.index, "prob"] = vals

    ax.set_yscale("normal")
    sns.scatterplot(data = tdata, x = x, y = "prob", hue = hue, ax = ax)
    ax.set(xlabel = x, ylabel = "Probability (%)")

    return ax
    


