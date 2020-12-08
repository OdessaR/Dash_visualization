import plotly.graph_objects as go
import constants
from plotly.subplots import make_subplots
import pandas as pd

def get_map_figure():
    df = pd.read_csv('data/president_county_candidate.csv')

    for col in df.columns:
        df[col] = df[col].astype(str)

    df['text'] = df['State'] + '<br>' + \
        'Donald Trump ' + df['Trump Rate'] + '<br>' + \
        'Joe Biden ' + df['Biden Rate'] + '<br>' + \
        'Grand Total ' + df['Grand Total']

    fig = go.Figure(data=go.Choropleth(
        locations=df['Code'],
        z=df['color'],
        locationmode='USA-states',
        colorscale='bluered', # check colorscales: https://plotly.com/python/colorscales/
        autocolorscale=False,
        text=df['text'], # hover text
        marker_line_color='white', # line markers between states
        colorbar_title="Trump Votes"
    ))
    
    fig.update_layout(
        # title_text='2011 US Agriculture Exports by State<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa'),
            showlakes=True, # lakes
            lakecolor='rgb(255, 255, 255)'),
    )
    fig.update_layout(clickmode='event+select')
    
    return fig