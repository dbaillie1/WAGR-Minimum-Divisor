import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set();
from math import pi
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

#Custom function for bubbles
def bubble(df, x, y, gender, title = ''):
    df = df[df['Gender'] == gender]

    x_max = df[x].max() + np.ptp(df[x])/10
    x_min = df[x].min() - np.ptp(df[x])/10

    y_max = df[y].max() + np.ptp(df[y])/10
    y_min = df[y].min() - np.ptp(df[y])/10

    fig = px.scatter(df, x=x, y=y, animation_frame="Week", animation_group="Country", color='Country',
                size = 'Size', hover_name="Country", range_y = [y_min, y_max], range_x = [x_min, x_max],
               log_x=False, title=title)
    return fig



def bar(df, c_1, c_2, yy = 'MeanDivisor', title = ''):
    mean_snapshot = df[(df['Week'] == 201801) | (df['Week'] == 201901) | (df['Week'] == 202001) | (df['Week'] == 202101)]
    red_snapshot_m = mean_snapshot[(mean_snapshot['Country'] == c_1) | (mean_snapshot['Country'] == c_2)]
    listt = ['Count', 'Country', 'Week', 'Gender', 'MeanDivisor']
    red_snapshot_m = red_snapshot_m[listt]
    red_snapshot_m['Gend'] = 'M'
    red_snapshot_m['Gend'][red_snapshot_m['Gender'] == 2] = 'W'

    red_snapshot_m['Week'] = red_snapshot_m['Week'].astype('str')
    fig = px.bar(red_snapshot_m, x="Week", y=yy, color="Country", barmode="group", facet_col="Gend",
                 category_orders={"Week": ["201801", "201901", "202001", "202101"],
                                  "Country": [c_1, c_2],
                                  "Gend": ["M", "W"]}, title = title)
    
    return fig


def box(df, c_list, top_x, gender = 'M', title = ''):
    
    df = df[df['Rank'] <= top_x]
    
    snap_red = []
    for c in c_list:
        snap_red.append(df[df['CountryCode'] == c])

    snap_red = pd.concat(snap_red)
    snap_red['Week'] = snap_red['Ranking_Week'].astype('str')
    fig = px.box(snap_red[snap_red['Ranking_Gender'] == gender], x="Week", y='Divisor', color = 'CountryCode', title = title)

    return fig
    
    