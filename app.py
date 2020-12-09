import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import figure_creator as fc
from colors import *

df = pd.read_csv('data/president_county_candidate.csv')
external_stylesheets = ['/assets/style.css']

external_stylesheets = [
    dbc.themes.YETI,
    #'https://use.fontawesome.com/releases/v5.9.0/css/all.css',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

fig_map = fc.get_map_figure()
fig_stream_chart = fc.get_stream_chart()

NAVBAR = dbc.NavbarSimple(
    brand="Interactive Social Media Analysis: Twitter Sentiment to the 2020 US election",
    #brand_href="#",
    color="primary",
    dark=True,
)

MAP = dbc.Card(
    [   
        dbc.CardHeader("2020 US election result map"),
        dbc.CardBody(
            [
                dcc.Graph(
                    id='map',
                    figure=fig_map,
                    config={
                        'displayModeBar': False,
                        #'staticPlot': True
                    }
                )
            ]
        ),
    ], 
    className="map_card",
    # style={"width":"1200px"} # set style seperately
)

TEMP_CARD = dbc.Card(
    [
        dbc.CardHeader("clicked state"),
        dbc.CardBody(
            [html.Div(id = 'out-put')]
        ),
        dbc.CardBody([
            dcc.Graph(
                id = 'stream_chart',
                figure = fig_stream_chart,
                config={
                    "displayModeBar": False,
                }
            )
        ])
    ]
)

BODY = dbc.Container(
    [
        MAP,
        TEMP_CARD
    ],
    className="class_name",
)

app.layout = html.Div(children=[
    NAVBAR,
    BODY
])

@app.callback(
    Output('out-put','children'),
    Input('map','clickData'))
def display_click_data(clickData):
    if clickData is not None:
        output = clickData['points'][0]['location']
        return format(output)
    return None

if __name__ == '__main__':
    app.run_server(debug=False)