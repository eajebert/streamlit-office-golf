import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def line_plot_multiple_y_vars(data, x_var, y_vars, **params):
    """Function to plot data as seaborn line plot.
    
    Parameters:
        data (Dataframe): Dataframe containing plot data.
        var_x (str): Column header key for x variable.
        var_y (str): List of y variable column headers.
        **params (dict): Dictionary containing plot parameters.
        initialise_window (int): Window (i.e. number of shots used) for estimating initial player quality.
    
    Returns:
        None
    """

    plot_data = pd.melt(data, id_vars=[x_var], value_vars=y_vars)
    fig, ax = plt.subplots(figsize=(10, 7))
    ax = sns.lineplot(
        data=plot_data,
        x=x_var,
        y='value',
        hue='variable'
    )
    ax.set(**params)