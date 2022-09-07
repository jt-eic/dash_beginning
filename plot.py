import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

import psutil

app = dash.Dash()

df = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
)

def data_list():
    datalst = [psutil.cpu_percent(), psutil.datetime.datetime.now().isoformat()]
    return datalst


df = pd.DataFrame(columns=["CPU", "TIME",])


def add_dfdata():
    global df
    df.loc[len(df)] = data_list()


fig = px.line(
    df,
    x="CPU",
    y="TIME",
    log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="CPU percent", figure=fig)])

@app.callback(Output("output", "CPU"),
              Input("idInput, "))
if __name__ == "__main__":
    app.run_server(debug=True)