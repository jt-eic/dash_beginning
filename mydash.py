from tkinter import Y
import pandas as pd
import psutil

import dash
from dash import html, dcc
from dash.dependencies import Output, Input  # Event was removed in v0.37
# import plotly.express as px
import plotly.graph_objs as go
import plotly
import random
from collections import deque


X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

app = dash.Dash(__name__)


def data_list():
    datalst = [psutil.cpu_percent(), psutil.datetime.datetime.now().isoformat()]
    return datalst

# my stuff, to later dump inside graph from CPU data...
df = pd.DataFrame(columns=["CPU", "TIME",])
df.loc[len(df)] = data_list()


app.layout = html.Div([
    dcc.Graph(id='live-graph', animate=True),  # the live graph
    dcc.Interval(
        id='graph-update',
        interval=2000,
        )
])

@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])  # TUT had 'Event' here rather than Input... changed, fixed

def update_graph(input_data):  ## call this ANYTHING we want, its the callback that runs this. THATS WHY we didn't see it.
    global X
    global Y  # sake of simplicity. Could be reading/updating to a DB, or reading a sensor, etc.
    df.loc[len(df)] = data_list()  # throws another line to the data element
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    data = go.Scatter(
        x = list(df.TIME),
        y = list(df.CPU),
        name = 'Scatter',
        mode = 'lines+markers',
        )
    
    return {'data': [data], 'layout': go.Layout(xaxis = dict(range=[min(df.TIME), max(df.TIME)]),
                                                yaxis = dict(range=[min(df.CPU), max(df.CPU)]),)}  # the 
    # try later, add my own stuff inside this and see what happens...
    # datalst = [psutil.cpu_percent(), psutil.datetime.datetime.now().isoformat()]
    # return datalst
    

if __name__ == "__main__":

    # simple enough...
    app.run_server(debug=True) # can pass as (host:'0.0.0.0', port=8081, debug=False)



