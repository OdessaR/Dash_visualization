import plotly.graph_objects as go
import constants
from plotly.subplots import make_subplots
import pandas as pd
from colors import *

def get_stream_chart():
    df = pd.read_csv('data/event_sample.csv')

    fig = go.Figure()
    # event A
    fig.add_trace(go.Scatter(x=list(df.date), y=df['event_A_a'],
    fill= None, showlegend = False,  hoverinfo='skip',
    mode='lines+text', line_color=stream_graph_colors['eventA'],line_shape='spline',
    ))
    fig.add_trace(go.Scatter(x=list(df.date), y=df['event_A_b'],
    fill= 'tonexty', name = 'event A',fillcolor=stream_graph_colors['eventA'],
    mode='lines', line_color=stream_graph_colors['eventA'],line_shape='spline',
    ))
    # event B
    fig.add_trace(go.Scatter(x=list(df.date), y=df['event_B_a'],
    fill= None, showlegend = False,hoverinfo='skip',
    mode='lines+text', line_color=stream_graph_colors['eventB'],line_shape='spline',
    ))
    fig.add_trace(go.Scatter(x=list(df.date), y=df['event_B_b'],
    fill= 'tonexty', name = 'event B', fillcolor=stream_graph_colors['eventB'],
    mode='lines', line_color=stream_graph_colors['eventB'],line_shape='spline',
    ))
    # event C
    fig.add_trace(go.Scatter(x=list(df.date), y=df['event_C_a'],
    fill= None, showlegend = False,hoverinfo='skip',
    mode='lines+text', line_color=stream_graph_colors['eventC'],line_shape='spline',
    ))
    fig.add_trace(go.Scatter(x=list(df.date), y=df['event_C_b'],
    fill= 'tonexty', name = 'event C', fillcolor=stream_graph_colors['eventC'],
    mode='lines', line_color=stream_graph_colors['eventC'],line_shape='spline',
    ))

    # Set title
    fig.update_layout(
        title_text="Time series for events with range slider and selectors",
        hovermode="x unified",
        xaxis=dict(
            showspikes=False,
        )
    )

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1y",
                        step="year",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    return fig

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