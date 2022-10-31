



# Definimos una función que nos muestre los valores de la variable objetivo, su porcentaje y conteo dentro del dataframe seleccionado

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import warnings

# Definimos una función que nos muestre los valores de la variable objetivo, su porcentaje y conteo dentro del dataframe seleccionado

def classes_overview(df=None, obj_val=""):
    '''
    Returns a dataframe with percentage and absolute values of the variable.
    :param df: Dataset to analyze
    :param obj_val: Objective variable
    :return: Dataframe
    '''
    temp = df[obj_val].value_counts(normalize=True).mul(100).rename('porcentaje').reset_index()
    temp_cont = df[obj_val].value_counts().reset_index()
    return pd.merge(temp, temp_cont, on=['index'], how='inner')



# Definimos una función que nos permita graficar las variables categóricas en función de la variable objetivo.

def plot_feature(df, col_name, target):
    """
    Visualize a variable with and without faceting on the loan status.
    - df dataframe
    - col_name is the variable name in the dataframe
    - full_name is the full variable name
    - continuous is True if the variable is continuous, False otherwise
    """
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(18,5), dpi=90)
    
    df_n = df.groupby([target, col_name]).size().reset_index()
    df_n = df_n.rename(columns={0:"conteo"})
    df_n["porcentajes"] = df_n['conteo'] / df_n.groupby(target)['conteo'].transform('sum') * 100
      
    sns.countplot(df[col_name], order=sorted(df[col_name].unique()), color='#5975A4', saturation=1, ax=ax1)
    ax1.set_xlabel(col_name)
    ax1.set_ylabel('Count')
    plt.xticks(rotation = 90)
    
    
    sns.barplot(data=df_n, y="porcentajes", x=col_name, hue=target, ax=ax2)
    ax2.set_xlabel(col_name)
    ax2.set_ylabel('Distribución')
    plt.xticks(rotation = 90)
    plt.tight_layout()
    
    
# Definimos función que nos permita sacar los histográmas de cada variable numérica.

def plot_histograms(df, columns):
    # keep total number of subplot
    k = len(df.columns)
    # n = number of chart columns
    n = columns
    m = (k - 1) // n + 1
    
    # Create figure
    fig, axes = plt.subplots(m, n, figsize=(n * 5, m * 3))

    # Iterate through columns, tracking the column name and 
    # which number we are at i. Within each iteration, plot
    for i, (name, col) in enumerate(df.iteritems()):
        r, c = i // n, i % n
        ax = axes[r, c]
        # the histogram
        col.hist(ax=ax)
        # kde = Kernel Density Estimate plot
        ax2 = col.plot.kde(ax=ax, secondary_y=True, title=name)
        ax2.set_ylim(0)

    # Use tight_layout() as an easy way to sharpen up the layout spacing
    fig.tight_layout()
