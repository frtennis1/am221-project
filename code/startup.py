import numpy as np
import pandas as pd
import torch
import pickle

from tqdm import tqdm_notebook as tqdm

import statsmodels.formula.api as smf
import statsmodels.api as sm
import seaborn.apionly as sns

import matplotlib
import matplotlib.pyplot as plt

plt.style.use('clean')
sns.set_palette(['#8F223A', '#505B70', '#A6A29F'])
plt.rcParams['font.sans-serif'] = 'Verdana'
plt.rcParams['figure.figsize'] = (6.5, 4)

%matplotlib inline
%config InlineBackend.figure_format = 'retina'

def ft_ax(ax=None,
          y=1.03,
          yy=1.1,
          title=None,
          subtitle=None,
          source=None,
          add_box=False,
          left_axis=False):
    """
    Format either a desired axis or the current axis as an FT plot.
    """

    if ax is None:
        ax = plt.gca()

    ax.set_axisbelow(True)
    
    if title is not None:
        title = plt.title(title, y=y, loc='left')
    if subtitle is not None:
        plt.annotate(subtitle, xy=title.get_position(),
                xycoords='axes fraction', xytext=(0,-11), 
                 textcoords='offset points', size='large') 
    
    if source is not None:
        src = plt.annotate(source, xy=(0,0), 
             xycoords='axes fraction', xytext=(0,-35), 
             textcoords='offset points', ha='left', va='top', size='small')
    
    # axes and grid-lines
    plt.grid(axis='y', linewidth=.5)
    sns.despine(left=True)
    if not left_axis:
        ax.yaxis.tick_right()
        ax.yaxis.set_label_position('right')
        ax.yaxis.set_label_coords(1,yy)
        ax.yaxis.get_label().set_rotation(0)
    ax.tick_params('y', length=0)
    
    plt.tight_layout()
    
    if add_box:
        ax2 = plt.axes(ax.get_position().bounds, facecolor=(1,1,1,0))
        ax2.xaxis.set_visible(False)
        ax2.yaxis.set_visible(False)
        x,y = np.array([[.01, 0.15], [y+.12, y+.12]])
        line = matplotlib.lines.Line2D(x, y, lw=6., color='k')
        ax2.add_line(line)
        line.set_clip_on(False)
    
    if add_box and source is not None:
        return (line, src)
    elif not add_box and source is not None:
        return (src,)
    elif add_box and source is None:
        return (line,)
    else:
        return []