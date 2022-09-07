# v1 from pythonprogramming.net

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

import pandas_datareader.data as web
import datetime


stock = "^DJI"

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
             symbol to graph:
    '''),
    
    dcc.Input(
        id='input', value='DIA', type='text'),
        html.Div(id='output-graph')
])


## This part here is how it calls the below funcion, so THE NEXT FUNCTION doesn't matter what its called!
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )

def update_graph(input_data):
    start = datetime.datetime(2022,1,1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, "stooq", start, end)
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': f" This is the title: {input_data}"
            }
        }
    )
    
if __name__ == "__main__":
    app.run_server(debug=True)