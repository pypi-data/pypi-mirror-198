import warnings
from typing import List, Tuple, Union

import numpy as np
import pandas as pd
from pandas.api.types import is_list_like






def make_multistep_target(df, var,steps):
    """
    Given a dataframe and a variable, it creates a multistep target. It creates
    a new column for each step, with the value of the variable shifted by the
    
    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the variable.
    var : str
        The name of the variable.
    steps : int
        The number of steps to shift the variable.

    Returns
    -------
    df : pd.DataFrame
        The dataframe with the new columns.
    
    """

    ts=df[var]
    ts=pd.concat(
        {f'{var}_step_{i + 1}': ts.shift(-i)
         for i in range(steps)},
        axis=1)
    df=pd.concat([df,ts],axis=1)
    df=df.drop(var,axis=1)
    df.dropna(inplace=True,axis=0)
    return df