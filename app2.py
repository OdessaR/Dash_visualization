import dash
import dash_auth
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


fig_map = fc.get_map_figure()

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

BODY = dbc.Container(
    [
        MAP
    ],
    className="class_name",
)

app.layout = html.Div(children=[
    NAVBAR,
    BODY
])


if __name__ == '__main__':
    app.run_server(debug=True)