# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://[your-ip-or-domain-name]:8080/ in your web browser.

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server  # <== ADD THIS LINE
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(
    df,
    x="Fruit", y="Amount", color="City", barmode="group"
)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python. Customized right here!
    '''),  # <== ADDED SOME TEXT HERE

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    # app.run_server(debug=True)  # <== THIS MAY NOT DEPLOY
    # USE DIFFERENT ARGUMENTS FOR run_server METHOD
    app.run_server(debug=True, host='0.0.0.0', port=8080)