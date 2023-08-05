"""Module for plotting wafermaps."""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns 

from numbers import Real
from enum import IntEnum
from matplotlib.patches import Ellipse

from typing import Literal

class WaferSize(IntEnum):
    """Enum for standard wafer sizes (in mm)."""
    W300 = 300
    W200 = 200
    W150 = 150
    W100 = 100

def wafermap(
    data : pd.DataFrame,
    diesize : tuple[float, float],
    threshold : float = None,
    center : tuple[float, float] = None,
    kind : Literal["indexed", "mm"] = "indexed",
    ax : mpl.axes.Axes = None,
    mask : pd.DataFrame = None,
    cmap = None,
    wafersize : WaferSize = WaferSize.W300,
    linewidth : float = 0.5,
    notch : Literal["top", "bottom", "left", "right"] = "bottom",
    **kwargs
) -> mpl.axes.Axes:
    """
    Seaborn like function for plotting wafermaps.

    Two kind of plots:

    - indexed: plot characteristics with indices of the different dies (seaborn's heatmap is used under the hood)
    - mm: plot characteristics in absolute position (mm)

    The data can be categorized by passing a threshold:

    - if threshold is a float, the data is categorized as pass/fail
    - if threshold is a tuple (low, high), the data is categorized as invalid (< low), fail (> high), pass (everything inbetween)

    Parameters
    ----------
    data : DataFrame
        Data to plot
    diesize : tuple[float, float]
        Size of one die in mm (x-size, y-size)
    threshold : float or tuple[float, float], default None
        Threshold to use for categorizing the data
    center : tuple[float, float], default (0, 0)
        Center of the center die (0, 0) in mm (kind = "indexed" only)
    kind : {"indexed", "mm"}, default "indexed"
        Kind of plot to do
    ax : Axes, default None
        Axes to plot on
    mask : DataFrame, default None
        Mask that can be used to narrow the amount of dies to show
    cmap : default None
        Automatic colormap is used if None, can be overwritten
    wafersize : :class:`WaferSize`, default WaferSize.W300
        Size of the wafer
    linewidth : float, default 0.5
        Width of the lines seperating the dies (kind = "indexed" only)
    notch : {"top", "bottom", "left", "right"}, default "bottom"
        Notch location

    Returns
    -------
    ax : mpl.axes.Axes
        Axes with the plot

    See Also
    --------
    heatmap :
        Seaborn's heatmap function 

    Examples
    --------
    >>> import semicond as sc
    >>> sc.wafermap(data = df, diesize = (16, 8), threshold = 0.5, kind = "indexed")
    ... 
    """
    # retrieve axes to work on
    ax = ax or plt.gca()

    # deconstruct inputs
    xc, yc = center or (0, 0)
    dsx, dsy = diesize
    ydies, xdies = data.shape

    # prepare data
    data = data.copy()
    data.columns = data.columns.astype(int)
    data = data.sort_index(axis = 0).sort_index(axis = 1)

    if kind == "indexed":
        xdim, ydim = (wafersize.value / dsx, wafersize.value / dsy)         # size of the wafer in "die index"
        wcx = (xdies / 2) - (xc / dsx)                                      # wafer center x
        wcy = (ydies / 2) - (yc / dsy)                                      # wafer center y
        
        in_wafer = in_wafer_like(data, diesize, (xc, yc), wafersize)
        mask = (mask or data.isna()) | (~in_wafer)

        if isinstance(threshold, Real):
            # preprocess data
            data = data > threshold
            # determine colormap
            cmap = cmap or sns.blend_palette(["#f44", "#4f4"], n_colors = 2, as_cmap = False)
            # plot heatmap
            sns.heatmap(data, ax = ax, mask = mask, cmap = cmap, linewidth = linewidth, **kwargs)
            # overwrite colorbar
            cax = ax.collections[0].colorbar.ax
            cax.set_yticks([0.25, 0.75])
            cax.set_yticklabels(["Fail", "Pass"])
        elif isinstance(threshold, tuple):
            # preprocess data
            mask_invalid = data < threshold[0]
            mask_fail = data > threshold[1]
            mask_passed = ~(mask_invalid ^ mask_fail)
            data = data.copy()
            data[mask_passed] = 6.0
            data[mask_fail] = 3.0
            data[mask_invalid] = 0.0
            # determine colormap
            cmap = cmap or sns.blend_palette(["#444", "#f44", "#4f4"], n_colors = 3, as_cmap = False)
            # plot heatmap
            sns.heatmap(data, ax = ax, mask = mask, cmap = cmap, vmin = 0, vmax = 6, linewidth = linewidth, **kwargs)
            # overwrite colorbar
            cax = ax.collections[0].colorbar.ax
            cax.set_yticks([1, 3, 5])
            cax.set_yticklabels(["Invalid", "Fail", "Pass"])
        else:
            cmap = cmap or "Spectral"
            sns.heatmap(data, ax = ax, mask = mask, cmap = cmap, linewidth = linewidth, **kwargs)
    elif kind == "mm":
        xdim, ydim = wafersize.value, wafersize.value
        wcx, wcy = (0, 0)
    else:
        raise ValueError(f"Unknown kind: {kind}, should be 'indexed' or 'mm'")
    
    # add wafer background
    main_circ = Ellipse(xy = (wcx, wcy), width = xdim, height = ydim, color = "#999", zorder = -2)
    ax.add_patch(main_circ)

    # add notch
    if notch == "bottom":
        nc = (wcx, wcy - ydim / 2)
    elif notch == "top":
        nc = (wcx, wcy + ydim / 2)
    elif notch == "left":
        nc = (wcx - xdim / 2, wcy)
    elif notch == "right":
        nc = (wcx + xdim / 2, wcy)
    else:
        raise ValueError(f"Unknown notch location: {notch}, should be 'top', 'bottom', 'left' or 'right'")
    notch_circ = Ellipse(xy = nc, width = xdim / 50, height = ydim / 50, color = "#fff", zorder = -1)
    ax.add_patch(notch_circ)

    # set fixed limits
    ax.set_xlim(wcx - xdim / 1.9, wcx + xdim / 1.9)
    ax.set_ylim(wcy - ydim / 1.9, wcy + ydim / 1.9)

    # return axes
    return ax

def in_wafer_like(
    df : pd.DataFrame, 
    diesize : tuple[float, float],
    center : tuple[float, float] = (0, 0),
    wafersize : WaferSize = WaferSize.W300
) -> pd.DataFrame:
    """
    Returns a boolean mask for every valid die that is with the wafer (not crossing the boundary).

    Parameters
    ----------
    df : DataFrame
        Dataframe with the die index as index and columns do determine output shape
    diesize : tuple[float, float]
        Size of the dies in mm
    center : tuple[float, float], default (0, 0)
        Center of the wafer in mm
    wafersize : :class:`WaferSize`, default WaferSize.W300
        Size of the wafer

    Returns
    -------
    DataFrame
        Boolean mask with the same shape as the input DataFrame
    """
    data = df.copy()
    dsx, dsy = diesize
    xc, yc = center
    radius = wafersize.value / 2

    xpos, ypos = np.meshgrid(
        data.columns.values.astype(int) * dsx,
        data.index.values.astype(int) * dsy,
    )

    return pd.DataFrame(
        data = np.sqrt((xpos + xc) ** 2 + (ypos + yc) ** 2) < (radius - np.hypot(dsx / 2, dsy / 2)),
        index = data.index,
        columns = data.columns,
    )
