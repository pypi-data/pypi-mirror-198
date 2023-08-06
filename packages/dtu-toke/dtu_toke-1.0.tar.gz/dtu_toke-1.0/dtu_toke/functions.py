# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:30:00 2023

@author: Toke Schäffer
"""

import numpy as np

def x_mask(x, start=None, end=None):
    
    """Function that creates a boolean mask/filter for plots etc.
    The mask/filter is based on x-values and some start value and
    end value of x, which is specified by the user. This functions
    was created to remove the transient part of a time series,
    but can also be used for other x-values e.g. frequencies etc.
    Instead of using this funtions, one can also just set the
    xlim of a plt.plot, but then the ylim will be set based on
    y-values corresponding to all x-values and not just the ones,
    that are actually plotted. This makes it difficult to
    find good values for ylim. When using this filter, matplotlib
    will automatically set the ylim only based on the values
    that are actually plottet.
    
    Parameters
    ----------
    start : integer or real, optional
    All values smaller than start is false in the mask
    
    end : integer or real, optional
    All values larger than end is false in the mask
    
    Returns
    -------
    mask : ndarray
    Array filled with true, expect for values smaller than start
    and values larger than end
    """
    
    # If both a start value and an end value is given
    if start is not None and end is not None:
        mask = (x >= start) & (x <= end)
    
    # If only a start value is given
    elif start is None and end is not None:
        mask = x <= end  
    
    # If only an end value is given
    elif start is not None and end is None:
        mask = x >= start
    
    # If neither start value nor end value is given,
    # return an array filled with True
    else:
        mask = np.full(len(x), True)
    
    return mask